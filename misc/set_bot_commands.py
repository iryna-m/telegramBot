from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "To get started"),
            types.BotCommand("help", "If you want to find out what this bot for"),
        ]
    )