import datetime
from aiogram.dispatcher import FSMContext
import requests
from aiogram import types
from data.messages import get_message
from keyboard.keyboard import keyboard_start, keyboard_options
from loader import dp, bot
from states.states import ForecastQuery


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(get_message('start').format(user_name), parse_mode='html', reply_markup=keyboard_start)
    await ForecastQuery.waiting_for_location.set()


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(get_message('help'))


@dp.message_handler(state=ForecastQuery.waiting_for_location)
async def choose_forecast_duration(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location'] = message.text

    await message.reply(get_message('forecast_duration'), parse_mode='html',
                        reply_markup=keyboard_options)
    await ForecastQuery.waiting_for_duration.set()


@dp.message_handler(states=[ForecastQuery.waiting_for_location, ForecastQuery.waiting_for_duration])
async def get_weather(message: types.Message, state: FSMContext):
      user_name = message.from_user.first_name
      lat = float(message.location.latitude)
      lon = float(message.location.longitude)

# global wd
# code_to_smile = {'Clear' : 'Ясно \U00002600',
#                  'Clouds' : 'Облачно \U00002601',
#                  'Rain' : 'Дождь \U00002614',
#                  'Drizzle' : 'Моросящий дождь \U00002614',
#                  'Thunderstorm' : 'Гроза \U000026A1',
#                  'Snow' : 'Снег \U0001F328'}
#
# try:
#     r1 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
# r2 = requests.get(
#             f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric')
#     data = r.json()
#     city = data['name']
#     weather_description = data['weather'][0]['main']
#     if weather_description in code_to_smile:
#         wd = code_to_smile[weather_description]
#     else:
#         print('Посмотри в окно')
#
#     cur_weather = data['main']['temp']
#     humidity = data['main']['humidity']
#     wind = data['wind']['speed']
#     sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
#     await message.reply(f'***** {datetime.datetime.now().strftime("%d-%m-%Y")}*****\n'
#     get_message('weather_in_city_message').format(city, cur_weather, humidity, wind, sunset_time)
#
# except:
# await message.reply(
#     'Мы не можем определить вашу погоду по локации, попробуйте ввести название города в поле ввода')
