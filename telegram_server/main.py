from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from handlers import *
import asyncio
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp:Dispatcher = Dispatcher()

async def main():
    #Реєстрація обробників
    dp.include_router(start.router)
    dp.include_router(screenshot.router)
    #--------------------------
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())