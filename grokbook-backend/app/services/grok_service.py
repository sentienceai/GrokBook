# app/services/grok_service.py
import os
import asyncio
import logging
from app.services.x_service import XService
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GrokService:
    def __init__(self):
        logger.info("Initializing GrokService")
        load_dotenv()
        self.client = AsyncOpenAI(
            api_key=os.getenv("XAI_API_KEY"),
            base_url="https://api.x.ai/v1"
        )
        self.x_service = XService()

    async def analyze_text(self, text):
        logger.info("Starting text analysis")
        try:
            summary = await self.summarize(text)
            logger.info("Text summarized successfully")
            key_points = await self.extract_key_points(summary)
            logger.info("Key points extracted successfully")
            
            # Handle X service separately
            relevant_posts = []
            x_service_error = None
            try:
                relevant_posts = await self.x_service.get_relevant_posts(key_points)
                logger.info("Retrieved relevant posts from X service")
            except Exception as e:
                x_service_error = str(e)
                logger.error(f"Error in X service: {x_service_error}")

            return {
                'summary': summary,
                'key_points': key_points,
                'relevant_posts': relevant_posts,
                'x_service_error': x_service_error
            }
        except Exception as e:
            logger.error(f"Error in analyze_text: {str(e)}")
            raise

    async def summarize(self, text):
        logger.info("Starting text summarization")
        prompt = f"Summarize the following text:\n\n{text}"
        return await self.fetch_ai_response(prompt)

    async def extract_key_points(self, summary):
        logger.info("Starting key point extraction")
        prompt = f"Extract key points from this summary:\n\n{summary}"
        result = await self.fetch_ai_response(prompt)
        return [kp.strip('- ').strip() for kp in result.split('\n') if kp.strip()]

    async def fetch_ai_response(self, prompt):
        logger.info("Fetching AI response")
        try:
            completion = await self.client.chat.completions.create(
                model="grok-2-public",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=500
            )
            result = completion.choices[0].message.content
            logger.info("AI response fetched successfully")
            return result
        except Exception as e:
            logger.error(f"Error fetching AI response: {str(e)}")
            raise

    async def analyze_dataset(self, df):
        logger.info("Starting dataset analysis")
        try:
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

            analysis_result = await self.fetch_ai_response(prompt)
            logger.info("Dataset analysis completed")

            # Process the result to extract summary and suggestions
            summary, analysis_suggestions = self.parse_dataset_analysis_result(analysis_result)

            return {
                'summary': summary,
                'analysis_suggestions': analysis_suggestions
            }
        except Exception as e:
            logger.error(f"Error in analyze_dataset: {str(e)}")
            raise

    @staticmethod
    def parse_dataset_analysis_result(analysis_result):
        logger.info("Parsing dataset analysis result")
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
