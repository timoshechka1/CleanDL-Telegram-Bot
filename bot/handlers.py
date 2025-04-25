import requests
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.snaptik import get_tiktok_download_link

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.reply("Пришли ссылку на видео TikTok")

@router.message()
async def handle_tiktok_link(message: Message):
    url = message.text.strip()
    await message.reply("Скачиваю видео...")

    try:
        download_url = get_tiktok_download_link(url)
        video_data = requests.get(download_url).content

        await message.reply_video(video_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")
