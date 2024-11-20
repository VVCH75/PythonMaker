from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость"),
            KeyboardButton(text='О нас')
        ]
             ],
    resize_keyboard=True,
)
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Штамп 1',callback_data='cart1')],
        [InlineKeyboardButton(text='Штамп 2',callback_data='cart2')],
        [InlineKeyboardButton(text='Штамп 3',callback_data='cart3')],
        [InlineKeyboardButton(text='Штамп 4',callback_data='cart4')],
        [InlineKeyboardButton(text='Другое',callback_data='other')]
    ]
)
buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='http://ya.ru')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]
    ]
)