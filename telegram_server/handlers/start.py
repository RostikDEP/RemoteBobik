from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from .keyboards import reply_keyboard

router = Router()

@router.message(CommandStart)
async def start(message:Message):
    await message.answer("Бот запущений...", reply_markup=reply_keyboard)