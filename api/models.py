# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserTweet(models.Model):
    msg_id = models.CharField(max_length=200)
    tweet_msg = models.CharField(max_length=200)
    create_date = models.DateField(blank=True, null=True)

class TweeterFollower(models.Model):
    follwer_id = models.CharField(max_length=200)
    follower = models.CharField(max_length=200)
    
class TweeterFollowing(models.Model):
    following_id = models.CharField(max_length=200)
    following = models.CharField(max_length=200)
