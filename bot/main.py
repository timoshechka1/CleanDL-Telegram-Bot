from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from bot.handlers import start

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот Запущен...")

    app.run_polling()

if __name__ == "__main__":
    main()