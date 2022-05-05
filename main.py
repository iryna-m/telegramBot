import requests
import datetime
import kb
import asyncio
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text

loop = asyncio.get_event_loop()
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot, loop=loop)


@dp.message_handler(commands='start')
async def get_location(message: types.Message):
    user_name = message.from_user.first_name
    msg = dp.message_handler(f'Привет, <b>{user_name}</b>! \n Я расскажу тебе о погоде, ты можешь ввести имя города в поле'
                        f' ввода или воспользоваться кнопкой', parse_mode='html', reply_markup=kb.keyboard_start)
    #await message.reply(f'Привет, <b>{user_name}</b>! \n Я расскажу тебе о погоде, ты можешь ввести имя города в поле'
                        #f' ввода или воспользоваться кнопкой', parse_mode='html', reply_markup=kb.keyboard_start)
    bot.next_step_handler(msg, choose_option)


@dp.message_handler(content_types=["location"])
async def choose_option(message: types.Message):
    user_name = message.from_user.first_name
    lat = float(message.location.latitude)
    lon = float(message.location.longitude)
    await message.reply(f'<b>{user_name}</b>, \n О какой погоде тебе рассказать?', parse_mode='html',
                        reply_markup=kb.keyboard_options)
    # try:
    #     r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric')
    #     data = r.json()
    #     city = data['name']
    #     cur_weather = data['main']['temp']
    #     humidity = data['main']['humidity']
    #     wind = data['wind']['speed']
    #     sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    #     await message.reply(f'***** {datetime.datetime.now().strftime("%d-%m-%Y")}*****\n'
    #                         f' Погода в городе: {city}\n Температура: {cur_weather}C° {wd}\n '
    #                         f'Влажность воздуха: {humidity}\n Ветер: {wind}\n '
    #                         f'Солнышко зайдет: {sunset_time}')
    # except:
    #     await message.reply('Мы не можем определить вашу погоду по локации, попробуйте ввести название города в поле ввода')
    #

@dp.message_handler()
async def get_weather_by_city_name(message: types.Message):
    user_name = message.from_user.first_name
    await message.reply(f'<b>{user_name}</b>, \n О какой погоде тебе рассказать?', parse_mode='html',
                        reply_markup=kb.keyboard_options)

    # global wd
    # code_to_smile = {'Clear' : 'Ясно \U00002600',
    #                  'Clouds' : 'Облачно \U00002601',
    #                  'Rain' : 'Дождь \U00002614',
    #                  'Drizzle' : 'Моросящий дождь \U00002614',
    #                  'Thunderstorm' : 'Гроза \U000026A1',
    #                  'Snow' : 'Снег \U0001F328'}
    #
    # try:
    #     r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
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
    #
    #     await message.reply(f'***** {datetime.datetime.now().strftime("%d-%m-%Y")}*****\n'
    #           f' Погода в городе: {city}\n Температура: {cur_weather}C° {wd}\n '
    #           f'Влажность воздуха: {humidity}\n Ветер: {wind}\n '
    #           f'Солнышко зайдет: {sunset_time}')
    #
    # except:
    #     await message.reply('\U0001F449 Проверте правильно ли Вы ввели название города')



if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)