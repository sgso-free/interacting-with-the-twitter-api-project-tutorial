######################################
#Code to get tweets using dde API
######################################

import os
from dotenv import load_dotenv
import tweepy
import requests
import pandas as pd

# load the .env file variables
load_dotenv()

# set the variable use to conect
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

#conect to the api
client = tweepy.Client(bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        return_type = requests.Response,
        wait_on_rate_limit=True)

#if not especify start_time return the last seven days
query = "#100daysofcode (python OR pandas)"
data = client.search_recent_tweets(query,max_results=100, tweet_fields=['author_id', 'created_at','lang'])
print(data)
 
# Save data as dictionary
tweets_dict = data.json() 

# Extract "data" value from dictionary
tweets_data = tweets_dict['data'] 

# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data) 

print(df.head())

df.to_csv('assets/tweets.csv')

#I will use explore.ipynb to explorer the data save to csv