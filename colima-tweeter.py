import requests
import tweepy
import os
import datetime
import random

tweet = []

breakfast = []
breakfast.append("Eggs: ranchero, tocino, jamon, chorizo, chirozo con papas, Mexicana. Omeletes: español, Jamon y Queso, Tocino y Queso, Chorizo, Queso y Jalapeños. Chilaquiles and Menudo. Our entire breakfast line up @ColimaMexican")
breakfast.append("Eggs, Omeletes, Chilaquiles and Menudo for breakfast @ColimaMexican restaurant. Phone: 559-627-2197")
breakfast.append("Have a great mexican breakfast at @ColimaMexican restaurant. We have a variety of eggs, omeletes, chilaquiles and menudo to start this great day.")
breakfast.append("Eat great breakfast at @ColimaMexican to start your day. We have eggs, omeletes, chilaquiles and menudo to start this great day.")
breakfast.append("Start your day in pleasure by having a good breakfast. @ColimaMexican restaurant has a variety of eggs, omeletes, chilaquiles and menudo to please you.")
breakfast.append("Breakfast is the most important meal of the day. Start with a good berakfast at @ColimaMexican. We have varieties of eggs, omeletes, chilaquiles and menudo on our breakfast menu")
breakfast.append("Enjoy the fragrance and taste of a great breakfast at @ColimaMexican. Eggs, omeletes, chilaquiles and menudo. 559-627-2197")
breakfast.append("Who wants eggs, omeletes, chilaquiles or menudo for breakfast? You do! @ColimaMexican restaurant has great breakfast items on our menu.")

lunch = []
lunch.append("Breakfast is the most important meal of the day. Lunch is next. Check out our weekly lunch specials @ColimaMexican restaurant. 559-627-2197")
lunch.append("All our weekly lunch specials are served with rice and beans at @ColimaMexican restaurant at 500 S Linwood St, Visalia, CA. Phone: 559-627-2197")
lunch.append("All our weekly lunch specials are served with rice and beans at @ColimaMexican restaurant. Phone: 559-627-2197")
lunch.append("All our weekly lunch specials are served with rice and beans at @ColimaMexican restaurant. Phone: 559-627-2197")
lunch.append("Two enchiladas with chicken, beef or cheese - is one of our weekly lunch specials dish at @ColimaMexican restaurant. Phone: 559-627-2197")
lunch.append("")

snack = []

dinner = []

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


