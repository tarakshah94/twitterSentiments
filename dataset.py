import tweepy
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy_credentials
from tweepy import Stream
import pandas as pd
import json
import time

auth = tweepy.OAuthHandler(tweepy_credentials.consumer_token,tweepy_credentials.consumer_secret)

auth.set_access_token(tweepy_credentials.access_token, tweepy_credentials.access_secret)

api = tweepy.API(auth)

query = 'Flipkart'

max_id = None

# tweets_raw = []
#
# for i in range(1,21):
#
#
#     if(not max_id):
#         search_tweets = api.search(query, count=100, since_id=max_id, rpp = i, in_reply_to_status_id = '@Flipkart')
#     else:
#         search_tweets = api.search(query, count=100, since_id=max_id, rpp=i, in_reply_to_status_id = '@Flipkart')
#
#     with open('flipkart_tweets.csv', "a", encoding="utf-8") as f:
#         for tweet in search_tweets:
#             tweets_raw.append(tweet.text)
#             f.write(tweet.text)
#             f.write('\n')
#
#
#
# print(len(list(dict.fromkeys(tweets_raw))))
# # print(len(tweets_raw))




# class StdOutListener(StreamListener):
#
#     def on_data(self, data):
#         print(data)
#         return True
#
#     def on_error(self, status):
#         print(status)
#
#
# if __name__ == "__main__":
#     listener = StdOutListener()
#     auth = OAuthHandler(tweepy_credentials.consumer_token,tweepy_credentials.consumer_secret)
#     auth.set_access_token(tweepy_credentials.access_token,tweepy_credentials.access_secret)




# auth = tweepy.OAuthHandler(tweepy_credentials.consumer_secret, tweepy_credentials.consumer_token)
# # auth.set_access_token(tweepy_credentials.access_secret, tweepy_credentials.consumer_token)
# #
# # api = tweepy.API(auth, wait_on_rate_limit=True)








################################################ TEST 1 ##########################################


# class TwitterClient(object):
#     def __init__(self):
#         # Access Credentials
#         consumer_key = tweepy_credentials.consumer_token
#         consumer_secret = tweepy_credentials.consumer_secret
#         access_token = tweepy_credentials.access_token
#         access_token_secret = tweepy_credentials.access_secret
#
#
#         try:
#             # OAuthHandler
#             authorization = OAuthHandler(consumer_key, consumer_secret)
#             # setting access token and secret
#             authorization.set_access_token(access_token, access_token_secret)
#             # create tweepy API object to fetch tweets
#             self.api = tweepy.API(authorization, wait_on_rate_limit=True)
#
#         except tweepy.TweepError as e:
#             print(f"Error: Twitter Authentication Failed - \n{str(e)}")
#
#             # Function to fetch tweets
#
#
#     def get_tweets(self, query, maxTweets=2000):
#         # empty list to store parsed tweets
#         tweets = []
#         sinceId = None
#         tweet_id = -1
#         tweetCount = 0
#         tweetsPerQry = 180
#
#         while tweetCount < maxTweets:
#             try:
#                 if (tweet_id <= 0):
#                     if (not sinceId):
#                         new_tweets = self.api.search(q=query, count=tweetsPerQry)
#                     else:
#                         new_tweets = self.api.search(q=query, count=tweetsPerQry,
#                                                      since_id=sinceId)
#                 else:
#                     if (not sinceId):
#                         new_tweets = self.api.search(q=query, count=tweetsPerQry,
#                                                      max_id=str(tweet_id - 1))
#                     else:
#                         new_tweets = self.api.search(q=query, count=tweetsPerQry,
#                                                      max_id=str(tweet_id - 1),
#                                                      since_id=sinceId)
#                 if not new_tweets:
#                     print("No more tweets found")
#                     break
#
#                 for tweet in new_tweets:
#                     parsed_tweet = {}
#                     parsed_tweet['tweets'] = tweet.text
#
#                     # appending parsed tweet to tweets list
#                     if tweet.retweet_count > 0:
#                         # if tweet has retweets, ensure that it is appended only once
#                         if parsed_tweet not in tweets:
#                             tweets.append(parsed_tweet)
#                     else:
#                         tweets.append(parsed_tweet)
#
#                 tweetCount += len(new_tweets)
#                 print("Downloaded {0} tweets".format(tweetCount))
#                 max_id = new_tweets[-1].id
#
#             except tweepy.TweepError as e:
#                 print("Tweepy error : " + str(e))
#                 break
#
#         # return pd.DataFrame(tweets).to_csv('tweets_flipkart.csv', encoding='utf-8')
#
#         return tweets
#
# tweetsHandler = TwitterClient()
# tweetsHandler.get_tweets('Flipkart')

##############################################################################################################


