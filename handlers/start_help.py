from aiogram import types
from data.messages import get_message
from keyboard.keyboard import keyboard_start
from loader import dp
from states.states import ForecastQuery


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(get_message('start').format(user_name), parse_mode='html', reply_markup=keyboard_start)


@dp.message_handler(commands=['help'], state='*')
async def process_help_command(message: types.Message):
    await message.answer(get_message('help'))
