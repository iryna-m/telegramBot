import os
from aiogram import executor
# from data.config import MODE
from data import config
from loader import dp, bot
from misc.logging import logger
from misc.notify_admin import on_startup_notify
from misc.set_bot_commands import set_default_commands
import sys


async def on_startup(dispatcher):
    await bot.set_webhook(config.APP_URL)
    await set_default_commands(dispatcher)

    # Send message to admin that bot is running
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

    # if MODE == 'dev':
    #     def run():
    #         logger.info('Starting in DEV mode')
    #         executor.start_polling(dp, on_startup=on_startup)
    # elif MODE == 'prod':
    #     def run():
    #         logger.info('Starting in PROD mode')
    #         executor.start_webhook(listen='0.0.0.0', port=int(os.environ.get('PORT', '8443')),
    #                                url_path=os.getenv('BOT_TOKEN'),
    #                                webhook_url='https://{}.herokuapp.com/{}'.format(os.environ.get('APP_NAME'),
    #                                                                                 os.getenv('BOT_TOKEN')))
    # else:
    #     logger.error('Mode is not specified')
    #     sys.exit(1)
