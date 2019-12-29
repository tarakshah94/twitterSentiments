# twitterSentiments
Unsupervised Tweet sentimental analysis using Textblob and Tweepy

Steps to run:

1. Register at developer.twitter.com if you haven't already.
2. Create an app on Twitter dev portal and get consumer_token, consumer_secretkey, access_token and access_securitykey
3. Edit the credentials ferched above in the tweepy_credentials.py file
4. Edit the search you want to make in the line below:
    ''''tweetsHandler.fetch_tweets('Flipkart')''''
5. You can increase the tweet counts to be fetched by increasing the max_Tweets parameter in the function line of the code shown below:
    ''''def fetch_tweets(self, search, max_Tweets=2100)''''
6. Run the dataset.py 
    this will fetch the tweets for you! 
7. Finally run the sentiments.py to run the Vader and Textblob models simultaneously
8. Your output will be saved in outputs.xlsx file inside the working directory.

Cheers!
