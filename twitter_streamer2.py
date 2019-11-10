from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import twitter_credentials

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename,1)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener,retry_count=25)

        # This line filter Twitter Streams to capture data by the keywords:
        print(stream.filter(track=hash_tag_list))


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename,num):
        self.num=1
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        if self.num>25:
            return True
        else: self.num+=1
        try:
            print(data)
            #breakpoint()
            with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
    def finish(self):
        return 0;

if __name__ == '__main__':
    i=0
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["donald trump","trump"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

    auth = tweepy.OAuthHandler("uTnCs6PyHFIrMG0pLxj4Gt1XX", "MtseQjd9sG1G94yV8ytL5Ww69Eb6G7V60DSGYjvnV9fAu")
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweet=api.search(q='donald trump',count=25)
    for t in tweet:
        print('\n'+t.text)