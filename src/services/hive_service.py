import os
import logging
import requests

class HiveIntelligenceService:
    def __init__(self):
        self.api_key = os.getenv('HIVE_API_KEY')
        self.api_url = "https://api.hiveintelligence.xyz/v1/search"
    
    def generate_tweet(self, topic):
        """Use Hive Intelligence API to generate a tweet about the given topic"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        prompt = f"""Create a tweet about the topic given below. 
        Requirements:
        - Keep it under 2 sentences and 250 characters
        - Make it informative, approachable and engaging
        - Make it a question, or a prediction wherever possible
        - Include relevant hashtags
        - Don't promote any specific product or service
        - Don't use any emojis
        Topic: {topic}"""
        
        payload = {
            "prompt": prompt,
            "temperature": 0.7,
            "include_data_sources": False
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            tweet_content = data.get('response', '').strip()
            
            # Remove quotes if present
            if tweet_content.startswith('"') and tweet_content.endswith('"'):
                tweet_content = tweet_content[1:-1]
                
            return tweet_content

        except requests.exceptions.RequestException as e:
            logging.error(f"Error calling Hive Intelligence API: {e}")
            return None
        except (KeyError, IndexError) as e:
            logging.error(f"Error parsing Hive Intelligence API response: {e}")
            return None 