import re

from telegram import Update
from telegram.ext import ContextTypes


URL_REGEX = r'https?://[^\s]+'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Приветсвую. Я Телеграм Бот CleanDL, отправьте мне ссылку и я загружу вам видео 🎬")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text

    if re.match(URL_REGEX, message_text):
        await update.message.reply_text("Ссылка принята. Идёт обработка… ⏳")
    else:
        await update.message.reply_text("Пожалуйста, отправь ссылку на видео 📎")