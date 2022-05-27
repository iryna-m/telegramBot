import os
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')  # Take str value
ADMINS = env.list('ADMINS')  # admin ids list
OW_TOKEN = env.str('OW_TOKEN')
