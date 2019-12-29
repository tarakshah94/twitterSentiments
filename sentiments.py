import pandas as pd
import nltk
import csv
from nltk import tokenize, word_tokenize, util
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
snowballStemmer = SnowballStemmer("english")
stopwords = stopwords.words('english')
import vaderSentiment
from textblob import TextBlob

file = pd.read_csv('tweets_flipkart.csv')
print(file.count())
# print(file['tweets'])



# pre-processing

def processing_text(tweet):
    tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"[0-9]*", "", tweet)
    tweet = re.sub(r"&amp", "", tweet)
    tweet = tweet.lower()

    clean_tweet = tweet.lower()
    return clean_tweet


def tokens_stemmer(tweets):

    total_tweets_tokens = []
    total_stemmer_tokens = []


    tokens = nltk.word_tokenize(tweets)

    tweets_tokens = []
    snowballStemmer_tokens = []

    for token in tokens:
        if token not in stopwords:
            tweets_tokens.append(token)
            snowballStemmer_tokens.append(snowballStemmer.stem(token))
    total_tweets_tokens.append(tweets_tokens)
    total_stemmer_tokens.append(snowballStemmer_tokens)

    tweet_token_total = []
    tweet_stem_total = []

    # Convert stemming and tokenied output back to sentences for sentimental analysis
    for tweets_tokens in total_tweets_tokens:
        tweet = ' '.join(words for words in tweets_tokens)
        tweet_token_total.append(tweet)

    for tweets_stems in total_stemmer_tokens:
        tweets = ' '.join(words for words in tweets_stems)
        tweet_stem_total.append(tweets)
    return tweet_token_total, tweet_stem_total


def score_value(score):
    if score >= -0.2 and score < 0.2:
        # print('Neutral')
        output = 'Neutral'

    elif score >= 0.20 and score < 0.60:
        # print('Slightly Positive')
        output = 'Slightly Positive'

    elif score >= 0.60 and score <= 1.0:
        # print('Positive')
        output = 'Positive'

    elif score >= -0.60 and score < -0.20:
        # print('Slighly Negative')
        output = 'Slighly Negative'

    elif score >= -1.0 and score < -0.60:
        # print('Negative')
        output = 'Negative'

    return output



output_textblob = []
output_vader = []


for i, j in file.iterrows():

    ################################ TEXTBLOB USING Tokenizing and stemming #####################
    processed_tweets = tokens_stemmer(processing_text(j["tweet"]))
    # print(processed_tweets[0])
    tweet_stemmed = processed_tweets[1]
    # print(tweet_stemmed)

    for tweet in tweet_stemmed:
        analyze = TextBlob(tweet)
        text_blob_polarity = analyze.sentiment.polarity
        # print(polarity)
        # print(tweet)
        # writer.writerows(polarity)
        output_textblob.append(score_value(text_blob_polarity))


    ######################################## VADER SENTIMENT ANALYSIS ################################

    analyzer = SentimentIntensityAnalyzer()
    vader_sentimets = analyzer.polarity_scores(j["tweet"])
    vader_compound_score = vader_sentimets['compound']

    output_vader.append(score_value(vader_compound_score))





file['output_textblob'] = output_textblob
file['output_Vader']    = output_vader
file1_save = file.to_excel("outputs.xlsx", "w")
print("Output file saved successfully!!")

