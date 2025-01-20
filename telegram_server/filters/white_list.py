from aiogram.types import Message
from aiogram.filters import BaseFilter

class WhiteList(BaseFilter):
    def __init__(self, allowed_ids:list[int]):
        self.allowed_ids = allowed_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.allowed_ids