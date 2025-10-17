import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Получаем токен из переменной окружения
TOKEN = "8256149638:AAFi1uBAXS3PDzKdx05UmqMeS9zKrYQ-mcg"

if not TOKEN:
    raise ValueError("❌ Ошибка: TELEGRAM_TOKEN не задан в переменных окружения!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Привет! Я бот-помощник Джарвиса.\n"
        "Напиши /download, чтобы скачать программу."
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Джарвис — ваш ИИ-ассистент для Windows!\n\n"
        "⬇️ Скачайте программу по ссылке:\n"
        "https://disk.yandex.ru/d/rC-adHUVcQTbFw\n\n"
        "✅ Просто запустите файл — установка не требуется!\n"
        "📁 Размер: ~507 МБ\n"
        "💻 Требуется: Windows 10/11, микрофон, интернет\n"
        "🔒 Антивирус может ругаться — это ложная тревога."
    )

def main():
    print("🚀 Запускаю Telegram-бота...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", download))
    print("✅ Бот работает! Ожидаю сообщений...")
    app.run_polling()

if __name__ == "__main__":
    main()