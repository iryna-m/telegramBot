import logging
from aiogram import Bot, Dispatcher, types, executor
from os import getenv
from sys import exit

tg_bot_token = getenv('BOT_TOKEN')
open_weather_token = getenv('OW_TOKEN')
