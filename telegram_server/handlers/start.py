from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from .keyboards import reply_keyboard

router = Router()

@router.message(Command("start"))
async def start(message:Message):
    await message.answer("Бот запущений...", reply_markup=reply_keyboard)