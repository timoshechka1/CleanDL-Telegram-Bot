from aiogram import Router, types
from aiogram.filters import Command
import yt_dlp
from io import BytesIO

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Отправь мне ссылку на видео для скачивания.")


async def download_video(url: str) -> BytesIO:
    buffer = BytesIO()

    ydl_opts = {
        'format': 'best',
        'outtmpl': '-',
        'quiet': True,
        'no_warnings': True,
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            video_data = ydl.prepare_filename(ydl.extract_info(url, download=False))

            with open(video_data, 'rb') as f:
                buffer.write(f.read())

    except Exception as e:
        raise Exception(f"Ошибка загрузки: {e}")

    buffer.seek(0)
    buffer.name = "video.mp4"
    return buffer


@router.message()
async def video_handler(message: types.Message):
    try:
        video = await download_video(message.text)
        await message.answer_video(video)
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

