import requests
import tweepy
import os
import datetime
import random

tweet = []
tweet.append("Chorizo")
tweet.append("Relleno")
tweet.append("Frijoles")
tweet.append("Queso")
tweet.append("Camaron")
tweet.append("Ostiones")

# personal details 
consumer_key=os.getenv('CONSUMER_KEY')
consumer_secret=os.getenv('CONSUMER_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
    
randomTweet=tweet[random.randint(0, 5)];
print(randomTweet)

# update the status 
# api.update_status(status ="Testing random tweet: " + randomTweet)


