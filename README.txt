SUMMARY:

This project required the use of Twitter data. At the time, "Star Wars: The Last Jedi" was about to release in theaters. I decided to do a marketing exercise looking at the tweets relating to Mark Hamill (Luke) and Daisy Ridley (Rey) relating to the upcoming release of the film.

I used python to extract, format and parse the relevant tweet data. I also performed some introductory textual analysis by writing a function to count the exclamation points in each tweet.

After loading the parsed data into R, I ran two statistical analyses on the data showing that there appeared to be more buzz regarding Daisy Ridley as compared with Mark Hamill.



For a more detailed walkthrough my code and process, please read below.

In PYTHON:

I pulled tweets using the tweepy package in Python. In the Python code, the "finding_tweets()" function extracts tweets. It has several conditional statements depending on what timeframe the user wants to extract tweets. 

The "tweets_to_df()" function converts the list of tweets into a dataframe. The conditional statement in this function is there because different methods have to be called on a tweet to extract its text depending on if it is retweeted or not. 

Then I extract only the subject character/actor hashtags and make indicator columns for each actor so that each tweet (row) is labeled. 

The exclama() function counts the exclamation points in each text. A new attribute column is created as well. 

Then the new finds are appended to the existing dataframe, a check for nulls and empty strings, and then a .csv file is created with only the indicator columns (no full text).



In R:

I calculated one-sided 1-sample proportion tests for Mark Hamill and Daisy Ridley. The sample was all tweets mentioning either actor (or both). The test was to see if one of the actors was mentioned more often. Results showed that the majority of tweets mentioned Daisy Ridley.

Next is a simple textual analysis. The number of exclamation points in the text of each tweet is counted. A two-sample, one-sided T-Test is run to see if the mean number of exlamation points in the tweets about each actor are significantly different from each other. Results showed that the average level of excitement about Mark Hamill tweets was lower than the average level of excitement about Daisy Ridley tweets.
