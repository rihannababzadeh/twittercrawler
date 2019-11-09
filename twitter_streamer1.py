import tweepy
import json
from twitter_credentials import *
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display

CONSUMER_KEY = '9Q3bQh65hKM97dyKOOZmvDC71'
CONSUMER_SECRET = 'acPt76bEcsaV91DcDKLuUGaUkTQ7EPm8hNwY8uDyAV8lLr2kpx'
ACCESS_TOKEN = '793785768493875200-Z58rfMssxOtGD6f7J9RHBpChCq3cHT6'
ACCESS_SECRET = '1WD2T3Z4bTIMEtShnX60bCgE1U9BzPSKgE2Ed7ZRWy9Ej'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

new_tweets = api.user_timeline(screen_name = "realdonaldtrump",count=25)
print(len(new_tweets))
print(new_tweets)



for tweet in new_tweets:
    outtweets=tweet._json
    with open('Trumpstweets.json', 'a') as f:
        print(outtweets)
        f.write(json.dumps(outtweets))