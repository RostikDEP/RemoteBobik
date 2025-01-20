from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="screenshot")]
    ],
    resize_keyboard=True
)