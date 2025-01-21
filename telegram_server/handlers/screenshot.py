from aiogram import Router
from aiogram.types import Message
from .utils import RemoteServer
from .utils import config
from .keyboards import reply_keyboard

router = Router()

@router.message(lambda message: message.text.lower() == "screenshot")
async def start(message:Message):
    await message.answer("Спроба зробити скріншот...", reply_markup=reply_keyboard)
    remoteServer = RemoteServer(config.SERVER)
    to_id = 0
    if message.chat.id == config.IDS[0]:
        to_id = config.IDS[1]
    elif message.chat.id == config.IDS[1]:
        to_id = config.IDS[0]

    res = remoteServer.send_instruction(to_id, message.chat.id,"screenshot")
    if res:
        await message.answer("Запит надіслано на сервер...")
    else:
        await message.answer("Помилка")