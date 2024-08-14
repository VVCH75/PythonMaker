from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
import asyncio

api = '7285833454:AAEvGzKEMaKVv-WOedGezrAPPFt0NO3-X2M'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command('start'))
async def start_message(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def message(message):
    print('Введите команду /start, чтобы начать общение.')

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
