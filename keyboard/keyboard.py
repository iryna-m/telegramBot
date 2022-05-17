from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, message

# Create Default Keyboard
keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
get_weather = types.KeyboardButton('Узнать погоду')
keyboard_start.add(get_weather)

keyboard_get_weather = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location = types.KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
keyboard_get_weather.add(location)

options = ['Погода на сегодня', 'Предпочитаю погоду на 5 дней']
keyboard_options = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
keyboard_options.add(*options)

# Create Inline button for sharing
keyboard_message = types.InlineKeyboardMarkup(row_width=1)
buttons = [
    types.InlineKeyboardButton(text='Детали здесь', url='https://openweathermap.org/'),
]
keyboard_message.add(*buttons)
