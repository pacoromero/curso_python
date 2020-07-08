Hosting telegram bot on Heroku for free.
Easy way to host your python telegram bot on Heroku

Deploying via Heroku Toolbelt (CLI)
Install Heroku Toolbelt, then:

Clone repository
git clone https://github.com/Kylmakalle/heroku-telegram-bot.git

Edit files
Edit bot.py file with your code

ATTENTION! Do not collapse/delete/comment some_token = os.environ[SOME_TOKEN] style stings (you can delete redis setup line if you do not need it), do not change them with your REAL tokens, all tokens will be setted up below in this guide!

More About Config Vars

Also, don't do like this, it's insecure, realy.

Edit requirments.txt with your code's dependencies

Specify your python runtime, avaliable versions listed here

Go to command line
cd heroku-telegram-bot
heroku login
heroku create --region eu appname # create app in eu region, common regions: eu, us
heroku addons:create heroku-redis:hobby-dev -a appname # (Optionaly) installing redis
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
heroku config:set TELEGRAM_TOKEN=123456789:AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLL # set config vars, insert your own
heroku config:set SOME_API_TOKEN=qwertyuiop1234567890
                ...
heroku ps:scale bot=1 # start bot dyno
heroku logs --tail # If for some reason it’s not working, check the logs
heroku ps:stop bot #stop bot dyno
