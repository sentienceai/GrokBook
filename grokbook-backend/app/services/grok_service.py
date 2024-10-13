# app/services/grok_service.py
import os
import asyncio
import xai_sdk
import pandas as pd

class GrokService:
    @staticmethod
    def analyze_text(text):
        # Initialize the xAI client
        client = xai_sdk.Client()

        # Define the prompt for text analysis
        prompt = f"Provide a detailed summary and key points for the following text:\n\n{text}\n\nSummary and Key Points:"

        async def fetch_analysis():
            result = ""
            # Use the sampler to generate the analysis
            async for token in client.sampler.sample(prompt=prompt, max_len=500):
                result += token.token_str
            return result

        # Run the async function
        analysis_result = asyncio.run(fetch_analysis())

        # Process the result to extract summary and key points
        # This is a simplistic parsing; you may need to adjust based on the actual response format
        summary, key_points = GrokService.parse_analysis_result(analysis_result)

        return {
            'summary': summary,
            'key_points': key_points
        }

    @staticmethod
    def parse_analysis_result(analysis_result):
        # Simple parsing logic
        # Assuming the response is in the format: "Summary: ... Key Points: ..."
        if "Key Points:" in analysis_result:
            summary_part, key_points_part = analysis_result.split("Key Points:", 1)
            summary = summary_part.strip().replace("Summary:", "").strip()
            key_points = [kp.strip('- ').strip() for kp in key_points_part.strip().split('\n') if kp.strip()]
        else:
            summary = analysis_result.strip()
            key_points = []
        return summary, key_points

    # Existing analyze_dataset method or updated one will be added here

    @staticmethod
    def analyze_dataset(df):
        # Convert DataFrame to a CSV string
        data_csv = df.to_csv(index=False)

        # Due to token limits, we may need to sample or summarize the dataset
        # For the purpose of this example, we'll take the first few rows
        sample_df = df.head(5)
        sample_csv = sample_df.to_csv(index=False)

        # Define the prompt for dataset analysis
        prompt = f"""You are a data analyst assistant. Provide an executive summary and suggest potential analyses for the following dataset sample:

        Dataset Sample:
        {sample_csv}

        Executive Summary and Analysis Suggestions:"""

        async def fetch_analysis():
            client = xai_sdk.Client()
            result = ""
            async for token in client.sampler.sample(prompt=prompt, max_len=500):
                result += token.token_str
            return result

        analysis_result = asyncio.run(fetch_analysis())

        # Process the result to extract summary and suggestions
        summary, analysis_suggestions = GrokService.parse_dataset_analysis_result(analysis_result)

        return {
            'summary': summary,
            'analysis_suggestions': analysis_suggestions
        }

    @staticmethod
    def parse_dataset_analysis_result(analysis_result):
        # Simple parsing logic
        # Assuming the response is in the format: "Executive Summary: ... Analysis Suggestions: ..."
        if "Analysis Suggestions:" in analysis_result:
            summary_part, suggestions_part = analysis_result.split("Analysis Suggestions:", 1)
            summary = summary_part.strip().replace("Executive Summary:", "").strip()
            suggestions = [s.strip('- ').strip() for s in suggestions_part.strip().split('\n') if s.strip()]
        else:
            summary = analysis_result.strip()
            suggestions = []
        return summary, suggestions
