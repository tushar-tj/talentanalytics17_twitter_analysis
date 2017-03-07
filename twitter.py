# Import methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# Import credentials from constants file
from constants import consumer_key, consumer_secret, access_token, access_token_secret


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = tweepy.API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['TalentAnalytics17'])

    #This line captures data with the keyword not more than 7 days old
    for tweet in tweepy.Cursor(api.search, q="#TalentAnalytics17", lang="en").items():
        print tweet
        # print tweet.created_at, tweet.text