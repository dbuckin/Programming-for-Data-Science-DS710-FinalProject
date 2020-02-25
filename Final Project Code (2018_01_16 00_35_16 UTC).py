# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:34:45 2017

@author: Deane
"""
import tweepy

con_key = # fill in
con_secret = #  fill in
acc_token = # fill in
acc_secret = # fill in
# creating authentication  (this allows me to retrieve 45,000 tweets per 15 min)
auth = tweepy.AppAuthHandler(consumer_key=con_key, consumer_secret=con_secret)
#Connect to the Twitter API using the authentication
api = tweepy.API(auth)

import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', -1) #allows me to see the full text of tweets when testing

# if adding on more tweets to the tweet_df dataframe created earlier...
# finding the id of the last tweet I collected (most recent tweet) so we can start the 
# new search from that point.
tweet_df.tail()
# 940700121255223297

last_id = int(tweet_df['id'][0])
# 940754923431526400


# The larger search
# To search for newer tweets, simply set the since_id in the query with   last_id.
# To search for older tweets, simply set the max_id in the query with the 
# highest tweet ID at which you're willing to start your search.
def finding_tweets(query, num_needed, max_id = -1, since_id = None):
    """ searches for tweets containing our desired hashtags
        and returns a list of tweets order by age reversed.
        (the first tweet is newest, the last tweet is oldest)"""
    tweets = []
    while len(tweets) < num_needed:
        try:
            if (max_id <= 0):
                if (not since_id):
                    new_tweets = api.search(q = '%23TheLastJedi%20OR%20%23LastJedi%20OR%20%23WaitforVIII%20OR%20%23starwarsviii%20', 
                                    count = 100, tweet_mode = 'extended')
                else:
                    new_tweets = api.search(q = '%23TheLastJedi%20OR%20%23LastJedi%20OR%20%23WaitforVIII%20OR%20%23starwarsviii%20', 
                                    count = 100, tweet_mode = 'extended', since_id = since_id)
            else:
                if (not since_id):
                    new_tweets = api.search(q = '%23TheLastJedi%20OR%20%23LastJedi%20OR%20%23WaitforVIII%20OR%20%23starwarsviii%20', 
                                    count = 100, tweet_mode = 'extended', max_id = str(max_id - 1))
                else:
                    new_tweets = api.search(q = '%23TheLastJedi%20OR%20%23LastJedi%20OR%20%23WaitforVIII%20OR%20%23starwarsviii%20', 
                                    count = 100, tweet_mode = 'extended', max_id = str(max_id - 1),
                                    since_id = since_id)
    
        except tweepy.TweepError as e:
            print("Error", e)
            break
        else:
            if not new_tweets:
                print("Could not find any more tweets!")
                break
            tweets.extend(new_tweets)
            max_id = new_tweets[-1].id
    
    return tweets

tweets = finding_tweets(query='%23TheLastJedi%20OR%20%23LastJedi%20OR%20%23WaitforVIII%20OR%20%23starwarsviii%20',
                        num_needed = 50000, since_id = last_id)
# testing and notes to self

tweets[-1].id_str # '942769579943694341'  Most recent tweet found 12/18/17
tweets[0].id_str  # '942955148078333953'

# 16400 tweets found from 12/12/17
# 45000 tweets found from 12/18/17
# 61400 tweets total

#Converting the tweets list to a dataframe
def tweets_to_df(tweets):
    """accepts a list of tweets and converts it into a dataframe"""
    column_names = ('id','text')
    dict_list = []
    for tweet in tweets:
        tweetID = tweet.id_str
        if hasattr(tweet, 'retweeted_status'):
            text = tweet.retweeted_status.full_text
        else:
            text = tweet.full_text
        dict_list.append(dict(zip(column_names, [tweetID, text])))
    
    return pd.DataFrame(dict_list)

new_tweet_df = tweets_to_df(tweets)
# when I created my first tweet data frame, this call was:  tweet_df = tweets_to_df(tweets)

# the next sets of code are applied to my new_tweet_df.  But they were applied to my first
# tweet_df when I made my first search.

# searching my tweets for the hashtags of actors in the full text and making new columns
new_tweet_df['Tweets about Luke'] = new_tweet_df['text'].str.contains('#LukeSkywalker|#MarkHamill')
new_tweet_df['Tweets about Rey'] = new_tweet_df['text'].str.contains('#DaisyRidley|#Rey')
       
# 54 tweets about Luke 12/12
# 569 tweets about Luke 12/18
# 623 tweets about Luke total

# 272 tweets about Rey  12/12
# 754 tweets about Rey 12/18
# 1026 tweets about Rey total

# getting a count of "!" for each text.
def exclama(row):
    """This function is applied over the rows of a tweet dataframe
        a new column with the number of exclamation points is added"""
    counter = 0
    trigger = row['text'].find('!')
    if trigger != -1:
        for i in row['text']:
            if i == '!':
                counter += 1
    return counter
new_tweet_df['Number of !'] = new_tweet_df.apply(exclama, axis = 1)

# appending the new_tweet_df to the existing tweet_df
tweet_df = tweet_df.append(new_tweet_df, ignore_index = True)

# don't forget to check for and get rid of NaNs and NAs
for index, row in tweet_df.iterrows():
    if(any(pd.isnull(row))):
        print(index, "here!")
        
# converting NAs to empty strings (if any)
test_df.fillna("", inplace=True)

# saving to .csv
# removing the text column before saving to .csv.   
without_text_df = tweet_df.copy() # without_text_df is now an independent copy of tweet_df
del without_text_df['text']
without_text_df.to_csv("BigTweet.csv", index = False, encoding = 'utf-8')





    

