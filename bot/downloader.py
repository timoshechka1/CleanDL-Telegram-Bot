import yt_dlp
from io import BytesIO

async def download_video(url: str) -> BytesIO:
    buffer = BytesIO()

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '-',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'merge_output_format': 'mp4',
        'outtmpl': '-',
        'force_generic_extractor': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)

    buffer.seek(0)
    buffer.name = "video.mp4"
    return buffer
