from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Приветсвую. Я Телеграм Бот CleanDL, отправьте мне ссылку и я загружу вам видео 🎬")