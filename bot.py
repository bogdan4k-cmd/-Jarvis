import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Безопасное получение токена из переменной окружения
TOKEN = os.environ.get("8256149638:AAFi1uBAXS3PDzKdx05UmqMeS9zKrYQ-mcg")

if not TOKEN:
    raise ValueError("❌ Ошибка: переменная TELEGRAM_TOKEN не задана!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Привет! Я бот-помощник Джарвиса.\n"
        "Напиши /download, чтобы скачать программу."
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Привет! Это Джарвис — ваш ИИ-ассистент для Windows.\n\n"
        "⬇️ Скачайте программу с Яндекс.Диска:\n"
        "https://disk.yandex.ru/d/rC-adHUVcQTbFw\n\n"
        "✅ Просто запустите файл — установка не требуется!\n"
        "📁 Размер: ~507 МБ\n"
        "💻 Требуется: Windows 10/11, микрофон, интернет\n"
        "🔒 Антивирус может предупреждать — это ложная тревога (файл безопасен)."
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