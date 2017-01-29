# sanic linebot example

A [sanic](https://github.com/channelcat/sanic) implementation of new [Line Message API](https://devdocs.line.me/en/#messaging-api) using [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

## Prerequisite
Python 3.5 or higher

- Dependent Libraries
```sh
pip install -r requirements.txt
```

## Setup

### Secret Data
You MUST setup the following variables to environment variables.
- LINE\_CHANNEL\_SECRET
- LINE\_CHANNEL\_ACCESS\_TOKEN

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
