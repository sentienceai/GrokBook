# app/services/x_service.py
import os
import tweepy
import asyncio
from dotenv import load_dotenv

load_dotenv()

class XService:
    @staticmethod
    def get_api():
        x_api_key = os.getenv('X_API_KEY')
        x_api_secret = os.getenv('X_API_SECRET')
        x_access_token = os.getenv('X_ACCESS_TOKEN')
        x_access_token_secret = os.getenv('X_ACCESS_TOKEN_SECRET')

        if not all([x_api_key, x_api_secret, x_access_token, x_access_token_secret]):
            raise ValueError("Missing X API credentials. Please check your environment variables.")

        auth = tweepy.OAuthHandler(x_api_key, x_api_secret)
        auth.set_access_token(x_access_token, x_access_token_secret)
        return tweepy.API(auth)

    @staticmethod
    async def get_relevant_posts(key_points):
        api = XService.get_api()
        query = ' OR '.join(key_points)
        
        # Run the synchronous Twitter API call in a separate thread
        loop = asyncio.get_running_loop()
        tweets = await loop.run_in_executor(None, lambda: api.search_tweets(q=query, lang='en', result_type='recent', count=10))
        
        return [{'text': tweet.text, 'user': tweet.user.screen_name} for tweet in tweets]
