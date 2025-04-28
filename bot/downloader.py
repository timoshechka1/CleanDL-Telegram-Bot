import yt_dlp
import requests
from io import BytesIO

async def download_video(url: str) -> BytesIO:
    buffer = BytesIO()

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '-',
        'merge_output_format': 'mp4',
        'max_filesize': 50 * 1024 * 1024,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if isinstance(info, dict) and 'url' in info:
                response = requests.get(info['url'], stream=True)
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        buffer.write(chunk)
            else:
                result = ydl.download([url])
                if isinstance(result, bytes):
                    buffer.write(result)

    except Exception as e:
        raise Exception(f"Ошибка загрузки: {str(e)}")

    buffer.seek(0)
    return buffer
