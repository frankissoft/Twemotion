import tweepy
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler
import json


consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

class MyListener(StreamListener):

    def on_data(self, data,):
        try:
            with open('GetTweetUS.json', 'a') as f:
                f.write(data)
                f.write(',')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            return false

#Set the hashtag to be searched
twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(locations=[-74,40,-73,41], language='en-US')
twitter_stream.filter(locations=[-125.1032803826,25.1247457393,-66.7383322529,48.9812801846], language='en-US')

# (-171.791110603, 18.91619, -66.96466, 71.3577635769)
# <gmd:EX_GeographicBoundingBox><gmd:westBoundLongitude><gco:Decimal>-125.1032803826</gco:Decimal></gmd:westBoundLongitude><gmd:eastBoundLongitude><gco:Decimal>-66.7383322529</gco:Decimal></gmd:eastBoundLongitude><gmd:southBoundLatitude><gco:Decimal>25.1247457393</gco:Decimal></gmd:southBoundLatitude><gmd:northBoundLatitude><gco:Decimal>48.9812801846</gco:Decimal></gmd:northBoundLatitude></gmd:EX_GeographicBoundingBox>
# <bounding><westbc>-125.1032803826</westbc><eastbc>-66.7383322529</eastbc><northbc>48.9812801846</northbc><southbc>25.1247457393</southbc></bounding>
