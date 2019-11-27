import tweepy
import sched
from datetime import datetime
import time
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler
import json
import csv


consumer_key = 'mbl6Q3aBRRza7uiQyWEzAqSco'
consumer_secret = 'UGH3ynJusNDiK1TECBUnfZo0iuJfYyedEMA6HYJ6eqNKINJWkJ'
access_token = '1157709279379386368-UPh9LIvUHVHlpWwrm1l4m48H9fvHTN'
access_secret = 'rYdzATZpZn2R7th9I0j8uzhs0oFE8LCfE1SClJvoayjh2'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
#
# # Status() is the data model for a tweet
# tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

class MyListener(StreamListener):

    def on_data(self, data):
        now = datetime.now()
        timestr = now.strftime("%Y%m%d%H%M")
        try:
            # with open('GetTweetUS.json', 'a') as f:
            #  G   f.write(data)
            #     f.write(',')
            #     return True
            with open('GetTweet' + timestr + '.csv', mode='a') as csv_file:
                data = json.loads(data)
                csv_file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_file_writer.writerow([data["created_at"], data["id_str"], data["text"],
                                              data["user"]["id_str"], data["user"]["location"],
                                              data["source"], data["geo"], data["user"]["description"],
                                              data["user"]["name"], data["user"]["created_at"],
                                              data["coordinates"], data["place"]["id"],
                                              data["place"]["name"], data["place"]["full_name"],
                                              data["place"]["country_code"], data["place"]["bounding_box"]["coordinates"]])
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True


    def on_error(self, status):
        print(status)
        if status == 420:
            return false

s = sched.scheduler(time.time, time.sleep)

def wait_run():
    print("Running...")
    t_end = time.time() + 60 * 3
    while time.time() < t_end:
        #Set the hashtag to be searched
        twitter_stream = Stream(auth, MyListener())
        # twitter_stream.filter(locations=["-74,40,-73,41], language='en-US')
        twitter_stream.filter(locations=[-125.1032803826,25.1247457393,-66.7383322529,48.9812801846])
        twitter_stream.filter(language='en')
    s.enter(60 * 2, 1, wait_run, ())

s.enter(60 * 2, 1, wait_run,())
s.run()
