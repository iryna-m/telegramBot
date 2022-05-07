import logging
import handlers
from aiogram import executor
from loader import dp
from misc.notify_admin import on_startup_notify
from misc.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Set default command for bot
    await set_default_commands(dispatcher)

    # Send message to admin that bot is running
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)





