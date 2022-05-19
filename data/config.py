import os
from environs import Env

env = Env()
env.read_env()

#MODE = os.getenv('MODE')  # To use via dev mode(polling) or Prod(webhook)
APP_URL = 'https://wf-telegram-bot.herokuapp.com/'
BOT_TOKEN = env.str('BOT_TOKEN')  # Take str value
ADMINS = env.list('ADMINS')  # admin ids list
#IP = env.str('IP')
OW_TOKEN = env.str('OW_TOKEN')
