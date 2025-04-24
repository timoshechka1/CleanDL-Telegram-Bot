import re

from aiogram import types
from telegram import Update
from telegram.ext import ContextTypes
from bot.cobalt import get_direct_video_url

URL_REGEX = r'https?://[^\s]+'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Приветсвую. Я Телеграм Бот CleanDL, отправьте мне ссылку и я загружу вам видео 🎬")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text

    if re.match(URL_REGEX, message_text):
        await update.message.reply_text("Ссылка принята. Идёт обработка… ⏳")
    else:
        await update.message.reply_text("Пожалуйста, отправь ссылку на видео 📎")

async def download_video(message: types.Message):
    video_link = message.text.strip()

    direct_url = get_direct_video_url(video_link)
    if direct_url:
        await message.reply_video(direct_url)
    else:
        await message.reply("❌ Не удалось получить видео.")