import requests
from io import BytesIO
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile, BufferedInputFile  # новый импорт

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
        download_url = await get_tiktok_download_link(url)
        video_data = requests.get(download_url).content

        video_stream = BytesIO(video_data)
        video_stream.name = "video.mp4"  # обязательно указать имя файла

        await message.reply_video(video=BufferedInputFile(file=video_stream.getvalue(), filename="video.mp4"))

    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}", parse_mode=None)


