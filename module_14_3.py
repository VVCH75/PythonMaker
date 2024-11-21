from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command, CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
api = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
form_router = Router()
dp.include_router(form_router)
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
    ]
)

@dp.message(Command('start'))
async def command_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Рассчитать"),
            types.KeyboardButton(text='Информация')
        ],
        [
            types.KeyboardButton(text='Купить')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)

@dp.message(F.text == 'Купить')
async def get_buying_list(message: types.Message):
    for i in range(4):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100} ')
        await message.answer_photo(photo='https://disk.yandex.ru/i/QvFyXHQ7X2QG0A')
    await message.answer(text='Выберите продукт для покупки:', reply_markup=inline_kb)

@form_router.callback_query(F.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
