# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import twitter
import tweepy
from django.views.generic import View, ListView
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

from .models import TweeterFollower, TweeterFollowing, UserTweet


def authenticate_account():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

class FollowerListView(ListView):
    model = TweeterFollower
    template_name = 'follower.html'
    context_object_name = 'followers'

    def get_follwers(self):
        api =authenticate_account()
        for friend in tweepy.Cursor(api.friends).items():
            TweeterFollower.objects.get_or_create(follower=friend.screen_name,
                    follwer_id=friend.id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FollowerListView, self).get_context_data(**kwargs)
        self.get_follwers()
        return context


class FollowingListView(ListView):
    model = TweeterFollowing
    template_name = 'following.html'
    context_object_name = 'followings'

    def get_followings(self):
        api =authenticate_account()
        if api.followers():
            for friend in tweepy.Cursor(api.followers()).items():
                TweeterFollowing.objects.get_or_create(following=friend.screen_name,
                        following_id=friend.id)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FollowingListView, self).get_context_data(**kwargs)
        self.get_followings()
        return context


class TopTweetView(View):

    def get_followings(self):
        api = authenticate_account()
        scrn_name = api.me().screen_name
        tweets = api.search(scrn_name)
        if tweets:
            for tweet in tweets:
                UserTweet.objects.get_or_create(msg_id=tweet.id,
                        tweet_msg=tweet.text,
                        create_date=tweet.created_at.date())
        return api


    def get(self, request, *args, **kwargs):
        api = self.get_followings()
        scrn_name = api.me().screen_name
        rep = api.search(scrn_name)
        api_urls = []
        all_msgs = {}
        for tw in rep:
            is_retwt = api.retweets(tw.id)
            if is_retwt:
                tw_urls = is_retwt[0].entities['urls']

                usr_twts = UserTweet.objects.filter(
                    tweet_msg__contains=tw_urls[0]['url'])
                all_msgs.update({tw.text:usr_twts.count()})
        return render(request, "top_tweets.html", 
            {'all_msgs':all_msgs})

class TweetDaysListView(ListView):
    model = UserTweet
    template_name = 'todays_tweets.html'
    context_object_name = 'tweet_msgs'

    def get_queryset(self):
        from datetime import datetime
        dat = datetime.today().date()
        return UserTweet.objects.filter(create_date=dat) 
