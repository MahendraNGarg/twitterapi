
from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.FollowerListView.as_view(), name='follower'),
    url(r'following/$', views.FollowingListView.as_view(), name='following'),
    url(r'days_tweet/$', views.TweetDaysListView.as_view(), name='messagess'),
    url(r'top_tweet/$', views.TopTweetView.as_view(), name='top'),
]