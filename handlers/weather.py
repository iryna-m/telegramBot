import datetime
import logging
from pprint import pprint

from aiogram.dispatcher import FSMContext
import requests
from aiogram import types
from aiogram.dispatcher.filters import Text
from data.config import OW_TOKEN
from data.messages import get_message
from keyboard.keyboard import keyboard_options, keyboard_get_weather, keyboard_start, keyboard_message
from loader import dp, bot
from states.states import ForecastQuery


@dp.message_handler(Text(equals='Узнать погоду'), state=None)
async def get_weather(message: types.Message):
    await ForecastQuery.waiting_for_location.set()
    await message.answer(get_message('get_weather'), reply_markup=keyboard_get_weather)


@dp.message_handler(content_types='text', state=None)
async def text_handler(message: types.Message):
    if message.text != 'Узнать погоду':
        await message.reply('Сначала нажми на кнопу "Узнать погоду", а затем вводи имя города в поле ввода')


@dp.message_handler(content_types=['location'], state=ForecastQuery.waiting_for_location)
async def process_location_by_geo(message: types.Message, state: FSMContext):
    lat = float(message.location.latitude)
    lon = float(message.location.longitude)
    location = [lat, lon]
    await state.update_data({'answer1': location})
    await ForecastQuery.next()
    await message.answer(get_message('forecast_duration'), parse_mode='html',
                         reply_markup=keyboard_options)


@dp.message_handler(content_types=['text'], state=ForecastQuery.waiting_for_location)
async def process_location(message: types.Message, state: FSMContext):
    location = message.text
    try:
        r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OW_TOKEN}')
        data = r.json()
        lat = data[0]['lat']
        lon = data[0]['lon']
        location = [lat, lon]
        await state.update_data({'answer1': location})
        await ForecastQuery.next()
        await message.answer(get_message('forecast_duration'), parse_mode='html',
                             reply_markup=keyboard_options)
    except:
        await message.answer(get_message('geocoding_failure'), reply_markup=keyboard_get_weather)


@dp.message_handler(state=ForecastQuery.waiting_for_duration)
async def request_weather(message: types.Message, state: FSMContext):
    data = await state.get_data()
    duration = message.text
    await state.update_data({'answer2': duration})
    location = data.get('answer1')
    lat = location[0]
    lon = location[1]
    await message.answer('Пошел узнавать погоду....', reply_markup=types.ReplyKeyboardRemove())
    if duration == 'Погода на сегодня':
        try:
            r = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OW_TOKEN}&units=metric')
            data = r.json()
            pprint(data)
            city = data['name']
            cur_weather = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
            answer_message = get_message('current_weather_message').format(city, cur_weather, humidity, wind,
                                                                           sunset_time)
            await message.answer(f'***** {datetime.datetime.now().strftime("%d-%m-%Y")}*****\n {answer_message}',
                                 reply_markup=keyboard_start, protect_content=False)

        except:
            await message.answer(get_message('weather_for_location_retrieval_failed'), reply_markup=keyboard_start)
        finally:
            await state.finish()
    elif duration == 'Предпочитаю погоду на 5 дней':
        try:
            r = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,'
                             f'minutely,hourly,alerts&units=metric&exclude=&appid={OW_TOKEN}')
            data = r.json()
            date1 = datetime.datetime.fromtimestamp(data['daily'][0]['dt'])
            date2 = datetime.datetime.fromtimestamp(data['daily'][1]['dt'])
            date3 = datetime.datetime.fromtimestamp(data['daily'][2]['dt'])
            date4 = datetime.datetime.fromtimestamp(data['daily'][3]['dt'])
            date5 = datetime.datetime.fromtimestamp(data['daily'][4]['dt'])

            temp1 = data['daily'][0]['temp']['day']
            temp2 = data['daily'][1]['temp']['day']
            temp3 = data['daily'][2]['temp']['day']
            temp4 = data['daily'][3]['temp']['day']
            temp5 = data['daily'][4]['temp']['day']

            description1 = data['daily'][0]['weather'][0]['description']
            description2 = data['daily'][1]['weather'][0]['description']
            description3 = data['daily'][2]['weather'][0]['description']
            description4 = data['daily'][3]['weather'][0]['description']
            description5 = data['daily'][4]['weather'][0]['description']

            await message.answer(get_message('5_days_weather_message').format(date1, temp1, description1, date2,
                                                                              temp2, description2, date3, temp3,
                                                                              description3, date4, temp4,
                                                                              description4, date5, temp5,
                                                                              description5), protect_content=False,
                                 reply_markup=keyboard_message, parse_mode='html')

        except:
            await message.answer(get_message('weather_for_location_retrieval_failed'), reply_markup=keyboard_start)

        finally:
            await state.finish()
