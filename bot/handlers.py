import requests
import yt_dlp
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

async def get_video_url(link: str) -> str:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'best[ext=mp4]/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        return info.get("url")

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.reply("Пришли ссылку на видео (TikTok, Instagram, YouTube...)")

@router.message()
async def handle_tiktok_link(message: Message):
    url = message.text.strip()
    await message.reply("Скачиваю видео...")

    try:
        video_url = await get_video_url(url)
        if not video_url:
            await message.reply("Не удалось получить ссылку для скачивания. Проверь ссылку и попробуй ещё раз.")
            return

        video_data = requests.get(video_url).content

        await message.reply_video(video_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}", parse_mode=None)



