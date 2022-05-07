from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')  # Take str value
ADMINS = env.list('ADMINS')  # admin ids list
#IP = env.str('IP')
open_weather_token = env.str('OW_TOKEN')
