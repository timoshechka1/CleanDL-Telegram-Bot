from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Привет!")

@router.message()
async def handle_tiktok_link(message: Message):
    await message.answer("Ты отправил ссылку!")