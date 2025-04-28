from aiogram import Router, types
from aiogram.filters import Command
import yt_dlp
import os
from io import BytesIO

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Отправь мне ссылку на видео для скачивания.")


async def download_video(url: str) -> BytesIO:
    buffer = BytesIO()

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'max_filesize': 50 * 1024 * 1024,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            if 'entries' in info:
                info = info['entries'][0]

            temp_filename = ydl.prepare_filename(info)
            ydl.download([url])

            with open(temp_filename, 'rb') as f:
                buffer.write(f.read())

            os.remove(temp_filename)

    except Exception as e:
        raise Exception(f"Ошибка загрузки: {str(e)}")

    buffer.seek(0)
    buffer.name = "video.mp4"
    return buffer


@router.message()
async def video_handler(message: types.Message):
    if not message.text.startswith(('http://', 'https://')):
        await message.answer("Пожалуйста, отправьте корректную ссылку на видео.")
        return

    try:
        await message.answer("Начинаю загрузку видео...")
        video = await download_video(message.text)
        await message.answer_video(video)
    except Exception as e:
        await message.answer(f"❌ Ошибка при загрузке видео: {str(e)}")

