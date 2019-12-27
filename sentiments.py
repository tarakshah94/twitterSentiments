import pandas as pd
import nltk
from nltk import tokenize, word_tokenize, util
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import vaderSentiment

file = pd.read_csv('flipkart_tweets.csv', index_col = "tweets")
# print(file['tweets'])



# pre-processing
import re

snowballStemmer = SnowballStemmer("english")
stopwords = stopwords.words('english')


clean_tweets = []
def processing_text(tweets):

    for tweet in tweets:
        tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)
        tweet = re.sub(r"http\S+", "", tweet)
        tweet = re.sub(r"[0-9]*", "", tweet)
        tweet = re.sub(r"&amp", "", tweet)
        tweet = tweet.lower()

        clean_tweets.append(tweet)
        return clean_tweets

processing_text(file)

print(clean_tweets)