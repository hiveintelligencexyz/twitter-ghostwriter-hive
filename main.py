#!/usr/bin/env python3
"""
Tech Tweet Bot - Automatically generates and posts tweets about tech topics
"""

import os
import logging
from dotenv import load_dotenv

# Load environment variables first
load_dotenv(override=True)

from src.services.twitter_service import TwitterService
from src.services.hive_service import HiveIntelligenceService
from src.utils.topic_manager import TopicManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tweet_bot.log'),
        logging.StreamHandler()
    ]
)

def main():
    """Main entry point"""
    try:
        # Initialize services
        twitter_service = TwitterService()
        hive_intelligence_service = HiveIntelligenceService()
        
        # Get CSV file path from environment variable
        csv_file = os.getenv('TOPICS_CSV', 'topics.csv')
        topic_manager = TopicManager(csv_file)
        
        # Get next topic
        topic, _ = topic_manager.get_next_topic()
        if not topic:
            logging.error("Failed to get topic")
            return False
        
        logging.info(f"Selected topic: {topic}")
        
        # Generate tweet with Hive Intelligence
        tweet_content = hive_intelligence_service.generate_tweet(topic)
        if not tweet_content:
            logging.error("Failed to generate tweet content")
            return False
        
        logging.info(f"Generated tweet: {tweet_content}")
        
        # Post tweet
        success = twitter_service.post_tweet(tweet_content)
        if success:
            logging.info("Tweet posted successfully!")
            return True
        else:
            logging.error("Failed to post tweet")
            return False
            
    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    main()
