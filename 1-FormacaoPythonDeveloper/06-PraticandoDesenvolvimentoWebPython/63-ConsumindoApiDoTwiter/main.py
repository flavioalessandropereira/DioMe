from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import sys
sys.path.append(r'c:\users\fap2\anaconda3\lib\site-packages')
import tweepy

BRAZIL_WOE_ID = 23424768

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

trends = api.get_place_trends(id=BRAZIL_WOE_ID)

if trends:
    for trend in trends[0]["trends"]:
        print(trend["name"])
else:
    print("Não foi possível obter os tópicos do momento.")

# for tweet in trends:
#     print(tweet)
