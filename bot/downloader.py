import yt_dlp
import requests
from io import BytesIO

async def download_video(url: str) -> BytesIO:
    buffer = BytesIO()

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '-',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'force_overwrites': True,
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        video_url = result.get("url")
        response = requests.get(video_url, stream=True)

        for chunk in response.iter_content(chunk_size=1024*1024):
            buffer.write(chunk)

    buffer.seek(0)
    buffer.name = "video.mp4"
    return buffer



