from requests_oauthlib import OAuth1Session
import settings
from datetime import date


twitter = OAuth1Session(
    settings.CONSUMER_KEY,
    settings.CONSUMER_SECRET,
    settings.ACCESS_TOKEN,
    settings.ACCESS_TOKEN_SECRET)
date = date.today()
class TweetController:
    def post_start_tweet(self, categoly):
        text = "タスク" + categoly + "を開始しました\n 現在時刻：" + date.now()
        params = {"status": text}
        req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)

    def post_finish_tweet(self, categoly, time):
        text = "タスク" + categoly + "を終了しました\n 時間："+ time
        params = {"status": text}
        req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)
