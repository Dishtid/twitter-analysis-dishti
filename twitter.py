

#  This program accesses data from a twitter user site (hard-coded as Stevens)

#  To run in a terminal window:   python3  twitter_data.py
#from textblob import TextBlob  # needed to analyze text for sentiment
#import argparse                 # for parsing the arguments in the command line
import csv                # for creating output .csv file
import tweepy              # Python twitter API package
import unidecode                # for processing text fields in the search results
#import pandas as pd
import streamlit as st
### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "G5JLnhHkFSqR1Wg43VM2wZhhD"
CONSUMER_KEY_SECRET = "HgNOmKfOBVZjWIoKkeggCJ4j28tWya1sk6akbhm9LPl4NiDFUs"
ACCESS_TOKEN = "1176333597978087424-hJz2R1sjHoozzLmVBGJMkq3UrOUTyE"
ACCESS_TOKEN_SECRET = "naaij8JirpjveTSyOFqpAUubXhYiwOUnM1VPVjjus20Tr"

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
def twitter_search(search_terms):
# Get Information About a Twitter User Account

        twitter_user = api.get_user(search_terms)
        if twitter_user:
        # Get Basic Account Information
            st.write("twitter_user id: ", twitter_user.id)
            st.write(twitter_user.name)
            st.write("twitter_user name: ", twitter_user.name)
            st.write("twitter_user screen name: ", twitter_user.screen_name)
            st.write("twitter_user description: ", twitter_user.name)
            st.write("twitter_user Followers count: ", twitter_user.followers_count)
            tmpTweets = api.user_timeline(id=twitter_user.id)
            #new_tweets = api.user_timeline(screen_name=twitter_user.screen_name, count=1)

            if tmpTweets:
                n = api.user_timeline(id=twitter_user.id, count=1)[0]
                #text = n.text
                texts = n.text
                # text of the tweet
                text = unidecode.unidecode(texts)
                st.write("twitter_user latest tweet: ", text)
            else:
                st.write("No tweets by the user")
            st.write("Top 10 followers screen name as follows:")
            st.write('')
            follow = api.followers_ids(id=twitter_user.id, count=10)[0:10]
            if len(follow) > 0:
                #print(follow)
                st.write("Printing followers ", len(follow))
                for i in follow:
                    screen = api.get_user(id=i)
                    st.write("Screen name ", screen.screen_name)
            else:
                st.write("total followers ", len(follow))
            #u = raw_input("Wish to continue? Enter user name")
           # if u == "STOP":
            #    exit()
            #else:
             #   twitter_search(u)
        # for tweet in tweepy.Cursor(api.search, q=search_term, lang="en",
        #                            result_type="popular").items(10):
        #     created = tweet.created_at  # date created
        #     text = tweet.text  # text of the tweet
        #     text = unidecode.unidecode(text)
        #     retweets = tweet.retweet_count  # number of retweets
        #     favourite_count = tweet.favorite_count  # number of favourites
        #    # username = tweet.user.name  # user name
        #     userid = tweet.user.id  # userid
        #     location = tweet.user.location  # user location
        #     followers = tweet.user.followers_count  # number of user followers
        #     friends = tweet.user.friends_count  # number of user friends



        #
        #
            # friends = []

        # print("\nFirst 5 friends:")
        #
        # # Creating a Cursor
        # cursor = tweepy.Cursor(api.friends, screen_name='FollowStevens')
        #
        # # Get and print 5 friends
        # for account in cursor.items(5):
        #     print(account.screen_name)

#search_terms= raw_input("Enter user name")
#if search_terms == "STOP":
#    exit()
#else:
#    twitter_search(search_terms)


st.header("Twitter Streamer and Sentiment Analysis")
st.write("....")
t =st.text_input("Enter User Name")
start = st.button("Get Analysis")
stop = st.button("Reset")

if start:
	twitter_search(str(t))

