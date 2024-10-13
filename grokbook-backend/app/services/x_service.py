# app/services/x_service.py
import os
import tweepy

class XService:
    auth = tweepy.OAuthHandler(os.getenv('X_API_KEY'), os.getenv('X_API_SECRET'))
    auth.set_access_token(os.getenv('X_ACCESS_TOKEN'), os.getenv('X_ACCESS_TOKEN_SECRET'))
    api = tweepy.API(auth)

    @staticmethod
    def get_relevant_posts(key_points):
        query = ' OR '.join(key_points)
        tweets = XService.api.search_tweets(q=query, lang='en', result_type='recent', count=10)
        return [{'text': tweet.text, 'user': tweet.user.screen_name} for tweet in tweets]
