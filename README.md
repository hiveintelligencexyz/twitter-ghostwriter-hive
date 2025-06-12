# Twitter AI Agent Powered by Hive Intelligence

This project is a Twitter AI Agent that interacts with the Twitter API and Hive Intelligence API to post tweets on behalf of user.

## Prerequisites

- Python 3.8 or higher
- Twitter Developer Account
- Hive Intelligence Account

## Setup Instructions

### 1. Twitter API Setup

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new project and app
3. Generate the following credentials:
   - API Key (Consumer Key)
   - API Secret Key (Consumer Secret)
   - Access Token
   - Access Token Secret
4. Create a `.env` file in the project root and add your Twitter credentials:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

### 2. Hive Intelligence Setup

1. Visit [Hive Intelligence Dashboard](https://dashboard.hiveintelligence.xyz)
2. Create an account or log in
3. Generate your API keys
4. Add your Hive API key to the `.env` file:
   ```
   HIVE_API_KEY=your_hive_api_key
   ```

### 3. Python Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Running the Bot

To start the bot, run:
```bash
python main.py
```

The bot will create a log file `tweet_bot.log` to track its activities.

## Project Structure

- `main.py`: Main bot script
- `src/`: Source code directory
- `topics.csv`: Topics data file
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (create this file with your API keys)

## Dependencies

- python-dotenv==1.0.0
- tweepy==4.14.0
- requests==2.31.0

## Logging

The bot maintains a log file `tweet_bot.log` that records all activities and any errors that occur during execution.

## Notes

- Make sure to keep your API keys secure and never commit them to version control
- The bot uses a `last_topic_index.txt` file to keep track of progress
- Ensure you have proper internet connectivity for API calls 