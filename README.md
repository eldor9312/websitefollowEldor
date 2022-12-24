
# Websitecheck by Eldor
This telegram bot checks for updates on site


## Before running this code make sure you have these libraries

pytelegrambotapi

urllib.request

requests

textblob

re

time

hashlib

BeautifulSoup4


## To  start

1. In main.py put your token (token = '') where you need to insert a telegram bot token which you get from BotFather.

2. In buttons.py there is a line that says password="время", you can change this password to any other password to register/login admins(put password in lower case as the code reads the text in lower case ) 

3. In buttons.py there is a line that says time_tosleep, you can change it in order to say for how many seconds it will sleep before checking the website again

4. In buttons.py there is a line that says probability, you can change it so spellcheck will put another word if it is sure for that coefficient

## You can change also
Name of buttons,texts,stickers in buttons.py

## Be careful

When admin adds website to check, when there is an update it will send to every user of bot, but if you restart the bot, it will reset the users as well
