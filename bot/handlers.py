from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import BufferedInputFile

from bot.downloader import download_video

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.reply("Пришли ссылку на видео (TikTok, Instagram, YouTube...)")

@router.message()
async def handle_video_link(message: Message):
    url = message.text.strip()
    await message.reply("Скачиваю видео...")

    try:
        video_stream = await download_video(url)

        await message.reply_video(video=BufferedInputFile(file=video_stream.getvalue(), filename="video.mp4"))

    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}", parse_mode=None)



