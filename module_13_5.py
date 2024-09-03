from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command, CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

import asyncio

api = '7285833454:AAEvGzKEMaKVv-WOedGezrAPPFt0NO3-X2M'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
form_router = Router()
dp.include_router(form_router)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(Command('start'))
async def command_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Рассчитать"),
            types.KeyboardButton(text='Информация')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@form_router.message(F.text == 'Рассчитать')
async def set_age(message: Message, state: FSMContext):
    await message.answer('Сколько вам полных лет?')
    await state.set_state(UserState.age)

@form_router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)

@form_router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

@form_router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    date = await state.get_data()
    Calories = 10 * int(date['weight']) + 6.25 * int(date['growth']) - 5 * int(date['age']) + 5
    await message.answer(f'Ваша норма калорий {str(Calories)}')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
