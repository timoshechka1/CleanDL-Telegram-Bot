from aiogram import Router, types
from aiogram.filters import Command
import yt_dlp
import requests
from io import BytesIO

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Отправь мне ссылку на видео для скачивания.")

async def download_video(url: str) -> BytesIO:
    buffer = BytesIO()

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)

        if 'entries' in result:
            result = result['entries'][0]

        video_url = result.get("url")
        if not video_url:
            raise Exception("Не удалось получить прямую ссылку на видео")

        response = requests.get(video_url, stream=True)
        if not response.ok:
            raise Exception(f"Ошибка загрузки видео: {response.status_code}")

        for chunk in response.iter_content(chunk_size=1024*1024):
            buffer.write(chunk)

    buffer.seek(0)
    buffer.name = "video.mp4"
    return buffer

@router.message()
async def video_handler(message: types.Message):
    try:
        video = await download_video(message.text)
        await message.answer_video(video)
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

