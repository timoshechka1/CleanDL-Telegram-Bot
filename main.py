from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет, я бот!")

@router.message()
async def handle_tiktok_link(message: Message):
    await message.answer("Ты отправил ссылку!")