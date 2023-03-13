import asyncio

import telebot.types as tgTypes
from telebot.async_telebot import AsyncTeleBot

import config, dbHandler
from models import group, player


bot = AsyncTeleBot(config.BOT_TOKEN)

def main():
    dbHandler.init()
    asyncio.run(bot.infinity_polling())


if __name__ == '__main__':
    main()