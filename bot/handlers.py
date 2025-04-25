import requests

from aiogram import types
from bot.snaptik import get_tiktok_download_link

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Пришли ссылку на видео TikTok")

@dp.message_handler()
async def handle_tiktok_link(message: types.Message):
    url = message.text.strip()
    await message.reply("Скачиваю видео...")

    try:
        download_url = get_tiktok_download_link(url)
        video_data = requests.get(download_url).content

        await message.reply_video(video_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")
