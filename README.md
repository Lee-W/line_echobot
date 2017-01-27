# django linebot example

A django implementation of new [Line Message API](https://devdocs.line.me/en/#messaging-api) using [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

## Setup

### Secret Data
You MUST setup the following variables.

- SECRET\_KEY
	- django secret key. You can generate using [Django secret key generator](https://gist.github.com/mattseymour/9205591)	
- LINE\_CHANNEL\_SECRET
- LINE\_CHANNEL\_ACCESS\_TOKEN

There are two way to set these variables  
1. Set these variables in `line_echobot/line_echobot/settings_secret.py`(Exactly the same name)  
2. Add these variables to environment variables. (`settings_secret.py` is loaded first)

### HTTPS Server
You'll need a https server.  
[Heroku](https://www.heroku.com) can serve this for you.  
All the needed settings for heroku are set in this repo.

Otherwise, you can also build your own https server.

### Set Webhook URL
Set webhook url on your `LINE Developers` page to `https://"your domain name"/echobot/callback/`

## Tutorial
The following articles describe how to construct this bot in detail.

- [[Bot] Introduction to Chatbot](http://lee-w-blog.logdown.com/posts/1126591-introduction-to-chatbot)
- [[Bot] Apply Line Messaging API](http://lee-w-blog.logdown.com/posts/1129876-apply-line-messaging-api)
- [[Bot] Line Echo Bot on Django](http://lee-w-blog.logdown.com/posts/1134898-line-echo-bot-on-django)
- [[Bot] Deploy LineBot on Heroku](http://lee-w-blog.logdown.com/posts/1148021-deploy-linebot-on-heroku)
- [[Bot] More About Line Messaging API - Template Messages](http://lee-w-blog.logdown.com/posts/1148026-more-about-line-messaging-api-template-messages)
- [[Bot] More than Just Echo Bot](http://lee-w-blog.logdown.com/posts/1151669-more-than-just-echo-bot)


There is also a [slide version](https://hackmd.io/p/HkW8LjRfl).

## Authors
[Lee-W](https://github.com/Lee-W)

## License
MIT
