# reading in and viewing the data
tweet_df <- read.table("C:/Users/Deane/Documents/Education Programs/U of Wisconsin/DS710/Lesson 13 & 14/ds710fall2017finalproject/BigTweet.csv",
                       header = TRUE, sep = ",")
View(tweet_df)

# creating a column to record tweets about both actors
tweet_df['Tweets.about.Both'] <- NA
tweet_df$'Tweets.about.Both'[which(tweet_df$'Tweets.about.Luke'=="True" & tweet_df$'Tweets.about.Rey'=="True")] <- "True"
length(tweet_df$'Tweets.about.Both'[which(tweet_df$'Tweets.about.Both'=="True")])

typeof(tweet_df$'Tweets.about.Luke'[1])

# counting the number of tweets about each actor and the total number of relevant tweets.
aboutLuke <- length(tweet_df$'Tweets.about.Luke'[which(tweet_df$'Tweets.about.Luke'=="True")])
aboutRey <- length(tweet_df$'Tweets.about.Rey'[which(tweet_df$'Tweets.about.Rey'=="True")])
aboutBoth <- length(tweet_df$'Tweets.about.Both'[which(tweet_df$'Tweets.about.Both'=="True")])
relevant_tweets <- aboutLuke + aboutRey - aboutBoth
aboutLuke
# 623 tweets about Luke
aboutRey
# 1026 tweets about Rey
aboutBoth
# 374 tweets about Both
relevant_tweets
# 1275 relevant tweets in all

# proportion of relevant tweets among all "Last Jedi" tweets collected
relevant_tweets/nrow(tweet_df)
# 0.02076547

# My Hypothesis Testing.
# Null Hyp: Proportion of Luke tweets >= 50%
# Alt Hyp: Proportion of Luke tweets < 50%
 prop.test(aboutLuke, n = relevant_tweets, p=0.5, alternative = 'less')
#     1-sample proportions test with continuity correction

# data:  aboutLuke out of relevant_tweets, null probability 0.5
# X-squared = 98.0012, df = 1, p-value < 2.2e-16
# alternative hypothesis: true p is less than 0.5
# 95 percent confidence interval:
#  0.0000000 0.3979344
# sample estimates:
#  p 
# 0.3778047
 
# we reject the null.

# Null Hyp: Proportion of Rey tweets <= 50%
# Alt Hyp: Proportion of Rey tweets > 50%
prop.test(aboutRey, n = relevant_tweets, p=0.5, alternative = 'greater')
#     1-sample proportions test with continuity correction

# data:  aboutRey out of relevant_tweets, null probability 0.5
# X-squared = 98.0012, df = 1, p-value < 2.2e-16
# alternative hypothesis: true p is greater than 0.5
# 95 percent confidence interval:
#   0.6020656 1.0000000
# sample estimates:
#   p 
# 0.6221953 

# we reject the null.

# Null Hyp: The difference between the mean # of exclamation points in tweets about Luke 
# vs. the # of exclamation points in tweets about Rey is zero or less than zero.  
#      mean(LukeExcite) - mean(ReyExcite) <= 0
# Alt Hyp:  The difference between the mean # of exclamation points in tweets about Luke
# vs. the # of exclamation points in tweets about Rey is greater than zero.
#      mean(LukeExcite) - mean(ReyExcite) > 0
LukeExcite <- tweet_df[which(tweet_df$'Tweets.about.Luke'=="True"),4]
ReyExcite <- tweet_df[which(tweet_df$'Tweets.about.Rey'=="True"),4]
t.test(ReyExcite, LukeExcite, alternative = "greater")
#     	Welch Two Sample t-test
# data:  ReyExcite and LukeExcite
# t = -8.1159, df = 1479.331, p-value = 1
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#  -0.3642065        Inf
# sample estimates:
#   mean of x mean of y 
# 0.4805068 0.7833066

#  We do not reject the null. 

# confirming
mean(tweet_df[which(tweet_df$'Tweets.about.Luke'=="True"),4])
# 0.7833066
mean(tweet_df[which(tweet_df$'Tweets.about.Rey'=="True"),4])
# 0.4805068

# graphing
# making a barplot on the # of tweets about each actor
tableTest = matrix(c(aboutLuke, aboutRey), nrow=1, ncol=2)
barplot(tableTest, names.arg=c("About Luke", "About Rey"), col="blue", xlab= "Character", ylab= 'Number of Tweets', main="Tweets About Each Character")



