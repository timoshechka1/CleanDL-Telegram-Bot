from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import BufferedInputFile
import yt_dlp
import os
import tempfile
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
        'outtmpl': '-',
        'merge_output_format': 'mp4',
        'max_filesize': 2000 * 1024 * 1024,
    }

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts['outtmpl'] = os.path.join(tmpdir, '%(title)s.%(ext)s')

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                if 'entries' in info:
                    info = info['entries'][0]

                filename = ydl.prepare_filename(info)
                ydl.download([url])

                with open(filename, 'rb') as f:
                    buffer.write(f.read())

    except Exception as e:
        raise Exception(f"Ошибка загрузки: {str(e)}")

    buffer.seek(0)
    return buffer


@router.message()
async def video_handler(message: types.Message):
    if not message.text.startswith(('http://', 'https://')):
        await message.answer("Пожалуйста, отправьте корректную ссылку на видео.")
        return

    try:
        await message.answer("Начинаю загрузку видео...")
        video_buffer = await download_video(message.text)

        # Создаем BufferedInputFile напрямую из буфера
        video_file = BufferedInputFile(
            file=video_buffer.getvalue(),
            filename="video.mp4"
        )
        await message.answer_video(video=video_file)

    except Exception as e:
        error_message = str(e).replace('<', '&lt;').replace('>', '&gt;')
        await message.answer(f"❌ Ошибка при загрузке видео: {error_message}")

