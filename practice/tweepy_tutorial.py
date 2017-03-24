import tweepy
from pprint import pprint

consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_token_secret = 'secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

me = api.me()
print(type(me))
pprint([method for method in dir(me) if not method.startswith('_')])

public_tweets = api.home_timeline()
first_tweet = public_tweets[0]
pprint(type(first_tweet))
pprint([method for method in dir(first_tweet) if not method.startswith('_')])
