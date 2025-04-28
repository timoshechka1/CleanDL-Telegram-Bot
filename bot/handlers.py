import yt_dlp
import requests
from io import BytesIO

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

        # Иногда result — это плейлист
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

