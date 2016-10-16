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

## Authors
[Lee-W](https://github.com/Lee-W)

## License
MIT