from requests_oauthlib import OAuth1Session
import json
import settings
class TweetText:
    twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    def create_tweet(self, tweet_text):  
        params = {"status": tweet_text}
        req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)