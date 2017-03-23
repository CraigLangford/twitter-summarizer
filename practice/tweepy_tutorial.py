import tweepy
from pprint import pprint

consumer_key = 'AME1iqfrYjkrbNrz587MIhbxQ'
consumer_secret = 'Z17xrkPm1J4sNIrIR85wmxdLlZSUjFd74Jl9mucwFGUrmQeTA5'
access_token = '294751529-Cj9QCFb6ODQN09xiWsSKmHzORb9VnwqFwlG3Ufwf'
access_token_secret = 'ZbGUxEaOW89kmS3x5uWZsFKlJnyyPTpaJLM0YeId5C7xi'

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
