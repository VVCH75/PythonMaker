from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command, CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from crud_functions import *


import asyncio
from config import *
from keyboards import *
from texts import *
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())
form_router = Router()
dp.include_router(form_router)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message(F.text == 'Регистрация')
async def sing_up(message: types.Message, state: FSMContext):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)

@dp.message(RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    if is_included(message.text) == True:
        await message.answer('Пользователь существует, введите другое имя')
        await state.set_state(RegistrationState.username)
    await state.update_data(username=message.text)
    await message.answer('Введите свой email:')
    await state.set_state(RegistrationState.email)

@dp.message(RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)

@dp.message(RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    add_user(f'{RegistrationState.username}', RegistrationState.email, RegistrationState.age)
    await message.answer('Регистрация прошла успешно')

@dp.message(Command('start'))
async def command_start(message: types.Message):
    # d = get_all_products()
    # await message.answer(f'{d}')
    # for prod in d:
    #     await message.answer(f'{prod[0]} | {prod[1]} | {prod[2]} | {prod[3]}')
    #     await message.answer_photo(prod[4])
    await message.answer(f'{message.from_user.username}, ' + start, reply_markup=start_kb)

@dp.message(F.text == 'О нас')
async def info(message: types.Message):
    await message.answer(about, reply_markup=start_kb)

@dp.message(F.text == 'Стоимость')
async def price(message: types.Message):
    await message.answer('Чего хотеть изволите?', reply_markup=catalog_kb)

@form_router.callback_query(F.data == 'back_to_catalog')
async def back(call):
    await call.message.answer('Чего хотеть изволите?', reply_markup=catalog_kb)
    await call.answer()

@form_router.callback_query(F.data == 'cart1')
async def buy_1(call):
    await call.message.answer_photo(photo='https://disk.yandex.ru/i/QvFyXHQ7X2QG0A', caption=cart1, reply_markup=buy_kb)
    await call.answer()

@form_router.callback_query(F.data == 'cart2')
async def buy_2(call):
    await call.message.answer_photo(photo='https://disk.yandex.ru/i/qBGKD-P7OjE8sQ', caption=cart2, reply_markup=buy_kb)
    await call.answer()

@form_router.callback_query(F.data == 'cart3')
async def buy_3(call):
    await call.message.answer_photo(photo='https://disk.yandex.ru/i/R7BzLxri0AOz8w', caption=cart3, reply_markup=buy_kb)
    await call.answer()

@form_router.callback_query(F.data == 'cart4')
async def buy_4(call):
    await call.message.answer_photo(photo='https://disk.yandex.ru/i/Bm_xygaqdqPkzQ', caption=cart4, reply_markup=buy_kb)
    await call.answer()

@form_router.callback_query(F.data == 'other')
async def buy_other(call):
    await call.message.answer(other, reply_markup=buy_kb)
    await call.answer()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())