import requests
import tweepy
import os
from datetime import datetime
import random

tweet = []

breakfast = []
breakfast.append("Eggs: ranchero, tocino, jamon, chorizo, chirozo con papas, Mexicana. Omeletes: espanol, Jamon y Queso, Tocino y Queso, Chorizo, Queso y Jalapenos. Chilaquiles and Menudo. Our entire breakfast line up @ColimaMexican")
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

tweet = []
tweet.append("Chorizo @ColimaMexican")
tweet.append("Relleno @ColimaMexican")
tweet.append("Frijoles @ColimaMexican")
tweet.append("Queso @ColimaMexican")
tweet.append("Camarones @ColimaMexican")
tweet.append("Ostiones @ColimaMexican")

eleven = []
eleven.append("Good morning @_VisaliaCA it is the best time of the day at everybody "
              "favorite restaurant. It is breakfast and lunch time here at @ColimaMexican "
              "open from 11am to 7:30pm for #togo orders only. We have breakfast all day and lunch starting 11am. "
              "Please order #togo at 559-627-2197"
              );

eleven.append("It is the best time of the day. Breakfast and lunch time. At @ColimaMexican breakfast is "
              "served #togo all day and lunch starts at 11am. Please order #togo by calling 559-627-2197")
eleven.append("It is exactly 11am and we opened our doors to customers @ColimaMexican at "
              "500 S Linwood st, @_VisaliaCA for #togo orders of food and alcohol. Please call 559-627-2197 to order.")

eleven.append("Ring-ding-ring-ding-ring-ding. It is the best time of the day in @_VisaliaCA. It is 11AM, lunch time "
              "and @ColimaMexican restaurant at 500 S Linwood St, is now open. Please call ahead 559-627-2197 "
              "for #ToGo orders only (for now).")

eleven.append("Buenos dias people of @_VisaliaCA If you haven't had your breakfast yet, no problem. We open at 11AM taking "
              "#TOGO orders. Breakfast all day, lunch at lunch time and dinner at dinner time. Then it is alcohol time "
              "because you can take it #Togo @ColimaMexican order at 559-627-2197")


five = []
five.append("A good read about Enchiladas - it seems enchiladas were food for the Aztec royalty - "
                       "Come to @ColimaMexican for yummy enchiladas and feel like a king, queen, prince or "
                       "princess - https://www.historytoday.com/archive/historians-cookbook/enchiladas-culinary-monument-colonialism")

five.append("It is 5:00 PM and it is time to start  thinking about some good Mexican food @ColimaMexican "
            "at 500 S Linwood St, @_VisaliaCA #ToGo orders only. Please call ahead 559-627-2197")
five.append("Dinner time! Think of your favorite dish from @ColimaMexican like our juicy chicken tacos. "
            "We are taking #TOGO orders from 11AM to to 7:30PM. Please call us at 559-627-2197 to place an order.  "
            "Beer and wine can be taken #TOGO from restaurants. Please ask for anything you'd like.")
five.append("Tequila! To get some inspiration, please listen to the #Tequila song youtu.be/MDD21ZJF3mI. "
            "Alcohol products can now be taken #togo @ColimaMexican  We close at 7:30 PM. "
            "Please call 559-627-2197 to order #Togo")
five.append("It is 5:00 PM and it is time to start  thinking about some good Mexican food @ColimaMexican "
            "at 500 S Linwood St, @_VisaliaCA #ToGo orders only. Please call ahead 559-627-2197")

six = []
six.append("There is still time to order some excellent #mexicanfood from @ColimaMexican "
            "at 500 S Linwood st @_VisaliaCA. We are open till 7:30pm. Think about Chimichangas "
            "right now, call 559-627-2197 to order food and beer #togo. We will have it ready to go.")
six.append("We close at 7:30pm. Order some flavorful Mexican food #togo from @ColimaMexican at"
           " 500 S Linwood st, @_VisaliaCA. Please call 559-627-2197 to order food and alcohol.")
six.append("We are closing at 7:30 pm tonight based on our temporary hours of operation. "
           "Please order as soon as possible if you would like some delicious Mexican "
           "food @ColimaMexican please call 559-627-2197 to order")

nine = []
nine.append("Wakey Wakey, Eggs and Bakey. It is almost time for lunch. This song will get you going. "
            "https://www.youtube.com/watch?v=ig3GaDGPVj4 @ColimaMexican opens at 11AM for #ToGo orders. "
            "Please call ahead 559-627-2197 to place your order. #BreakfastAllDay, lunch, snack, dinner, alcohol $toGo and dessert.")
nine.append("Here's something to start your day. Puerto Vallarta Squeeze By Willy and Lobo - youtu.be/V0-I-2HFTjM "
            "ok, now get some great #MexicanFood from @ColimaMexican at 500 S Linwood @_VisaliaCA #ToGo. "
            "Call 559-627-2197 to order food and alcohol #ToGo. We open at 11am.")

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

now = datetime.now()

current_hour = now.strftime("%H")
randomTweet = ""

if int(current_hour) == 11:
    randomTweet=eleven[random.randint(0, len(eleven)-1)];
    print(randomTweet)
    exit(0)

if int(current_hour) == 9:
    randomTweet=nine[random.randint(0, len(nine)-1)];
    print(randomTweet)
    exit(0)

if int(current_hour) == 5:
    randomTweet=five[random.randint(0, len(five)-1)];
    print(randomTweet)
    exit(0)

if int(current_hour) == 6:
    randomTweet=six[random.randint(0, len(six)-1)];
    print(randomTweet)
    exit(0)


# update the status 
# api.update_status(status ="Testing random tweet: " + randomTweet)


