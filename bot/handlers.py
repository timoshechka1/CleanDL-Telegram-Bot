from telegram import Update
from telegram.ext import ContextTypes
from bot.snaptik import get_direct_video_url

URL_REGEX = r'https?://[^\s]+'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Приветсвую. Я Телеграм Бот CleanDL, отправьте мне ссылку и я загружу вам видео 🎬")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_link = update.message.text.strip()

    direct_url = get_direct_video_url(video_link)
    if direct_url:
        await update.message.reply_video(direct_url)
    else:
        await update.message.reply_text("❌ Не удалось получить видео.")