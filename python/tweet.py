#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import cgi
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

tweet = cgi.FieldStorage()
api.update_status(tweet["text"].value)

print("Content-type:text/html;charset=UTF-8\n\n");
