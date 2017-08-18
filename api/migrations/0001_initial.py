# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TweeterFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follwer_id', models.CharField(max_length=200)),
                ('follower', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TweeterFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_id', models.CharField(max_length=200)),
                ('following', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follwer_id', models.CharField(max_length=200)),
                ('follower', models.CharField(max_length=200)),
            ],
        ),
    ]
