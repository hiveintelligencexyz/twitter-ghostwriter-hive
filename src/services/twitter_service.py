import os
import logging
import tweepy
from dotenv import load_dotenv

class TwitterService:
    def __init__(self):
        # Ensure .env file is loaded
        load_dotenv(override=True)
        
        # Load Twitter credentials from environment variables
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.api_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.api_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        
        # Validate credentials
        if not all([self.bearer_token, self.api_key, self.api_secret, self.access_token, self.access_token_secret]):
            missing = []
            if not self.bearer_token: missing.append('TWITTER_BEARER_TOKEN')
            if not self.api_key: missing.append('TWITTER_CONSUMER_KEY')
            if not self.api_secret: missing.append('TWITTER_CONSUMER_SECRET')
            if not self.access_token: missing.append('TWITTER_ACCESS_TOKEN')
            if not self.access_token_secret: missing.append('TWITTER_ACCESS_TOKEN_SECRET')
            raise ValueError(f"Missing required Twitter credentials: {', '.join(missing)}")
        
        # Initialize Twitter API client
        self.client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )
    
    def post_tweet(self, tweet_content):
        """Post tweet to Twitter using v2 API"""
        try:
            # Check tweet length
            if len(tweet_content) > 280:
                logging.warning(f"Tweet too long ({len(tweet_content)} chars), truncating")
                tweet_content = tweet_content[:277] + "..."
            
            response = self.client.create_tweet(text=tweet_content)
            logging.info(f"Tweet posted successfully: {response.data['id']}")
            return True
            
        except tweepy.TweepyException as e:
            logging.error(f"Error posting tweet: {e}")
            return False
        except Exception as e:
            logging.error(f"Unexpected error posting tweet: {e}")
            return False 