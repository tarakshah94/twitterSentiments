import tweepy
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy_credentials
from tweepy import Stream
import pandas as pd
import json
import time

# auth = tweepy.OAuthHandler(tweepy_credentials.consumer_token,tweepy_credentials.consumer_secret)
#
# auth.set_access_token(tweepy_credentials.access_token, tweepy_credentials.access_secret)
#
# api = tweepy.API(auth)
#
# query = 'microsoft'
#
# max_id = None

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


class TwitterClient(object):
    def __init__(self):

        try:
            # Authenticate
            authorization = OAuthHandler(tweepy_credentials.consumer_token, tweepy_credentials.consumer_secret)
            # setting access token and secret
            authorization.set_access_token(tweepy_credentials.access_token, tweepy_credentials.access_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(authorization, wait_on_rate_limit=True)

        except tweepy.TweepError as e:
            print(f"Error: Twitter Authentication Failed - \n{str(e)}")


    def fetch_tweets(self, search, max_Tweets=2100):
        # empty list to store parsed tweets
        tweets = []
        last_tweetId = None
        tweet_id = -1
        tweetCount = 0
        tweetsPerQry = 100

        while tweetCount < max_Tweets:
            try:
                if (tweet_id <= 0):
                    if (not last_tweetId):
                        new_tweet = self.api.search(q=search, count=tweetsPerQry)
                    else:
                        new_tweet = self.api.search(q=search, count=tweetsPerQry,
                                                     since_id=last_tweetId)
                else:
                    if (not last_tweetId):
                        new_tweet = self.api.search(q=search, count=tweetsPerQry,
                                                     max_id =str(tweet_id - 1))
                    else:
                        new_tweet = self.api.search(q=search, count=tweetsPerQry,
                                                     max_id =str(tweet_id - 1),
                                                     since_id =last_tweetId)
                if not new_tweet:
                    print("New tweets Not found")
                    break

                for tweet in new_tweet:
                    parsed_tweet = {}
                    parsed_tweet['tweet'] = tweet.text

                    # append new tweets to a list
                    if tweet.retweet_count > 0:
                        # check if it's a retweet and append only once if so...
                        if parsed_tweet not in tweets:
                            tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)

                tweetCount += len(new_tweet)
                print("Downloaded "+ str(tweetCount) +  " tweets")
                tweet_id = new_tweet[-1].id

            except tweepy.TweepError as e:
                print("Tweepy error : " + str(e))
                break

        return pd.DataFrame(tweets).to_csv('tweets_flipkart.csv', encoding='utf-8', index=False)

tweetsHandler = TwitterClient()
tweetsHandler.fetch_tweets('Flipkart')

##############################################################################################################



########################### Selenium #####################################################################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# class SeleniumClient(object):
#     def __init__(self):
#         #Initialization method.
#         self.chrome_options = webdriver.ChromeOptions()
#         self.chrome_options.add_argument('--headless')
#         self.chrome_options.add_argument('--no-sandbox')
#         self.chrome_options.add_argument('--disable-setuid-sandbox')
#         options = self.chrome_options
#         # you need to provide the path of chromdriver in your system
#         self.browser = webdriver.Chrome('C:/Chromedriver/chromedriver')
#
#         self.base_url = 'https://twitter.com/search?q='
#
#     def get_tweets(self, query):
#         '''
#         Function to fetch tweets.
#         '''
#         try:
#             self.browser.get(self.base_url+query)
#             time.sleep(2)
#
#             body = self.browser.find_element_by_tag_name('body')
#
#             for _ in range(30):
#                 body.send_keys(Keys.PAGE_DOWN)
#                 time.sleep(0.3)
#
#             timeline = self.browser.find_element_by_id('timeline')
#             tweet_nodes = timeline.find_elements_by_css_selector('.tweet-text')
#
#             self.browser.quit()
#             return pd.DataFrame({'tweets': [tweet_node.text for tweet_node in tweet_nodes]})
#
#         except:
#             print("Selenium - An error occured while fetching tweets.")
#
# selenium_client = SeleniumClient()
#
# tweets_df = selenium_client.get_tweets('AI and Deep learning')