
A Simple Twitter REST API Example
=================================
This application is simple Twitter REST API demonstration application.

Configuration details for this application
------------------------------------------

To configure this appliction into your local machine you must have installed python and pip package of python.

Once you have installed above requirements then follow these instruction to configure this application.

clone/download this application repository into your local machine.
then navigate to twitterapi directory and execute the following commands


```
$ pip install -r requirements.txt
```

this will install all require application depandancies.
As we used the Sqlite database and this database copy already exist in this application so you dont need to do any action with database. 

To start this application just run the following command

    python manage.py runserver

this will start the Django server, you can access the applicaiton on your browser using this url.

	http://localhost:8000/


Following data brings from twitter and stores in database

these are the basic endpoint's of twitter that data it will fetch :-
	
1. User Followings: Get all the friends of twitter handle and store in database 
	
	/twitter

2. User Follwers: Get all the followers of twitter handle and store in database 
	
	/following
	
3. User Tweets: Get Tweets of twitter handle and display

	/days_tweet
	
4. Day tweets: Get Tweets of twitter handle diplay by todays date 

	/top_tweet


To use this APP working you need to add the following twitter developer app credentials in settings.py

		## Twitter API keys
		CONSUMER_KEY = ''#'your_consumer_key'
		CONSUMER_SECRET = ''#'your_consumer_secret'
		ACCESS_TOKEN = ''#'your_access_token'
		ACCESS_TOKEN_SECRET = ''#'your_access_token_secret'

these credentials you will get by creating a twitter developer app from here

		https://apps.twitter.com/app/new

		
