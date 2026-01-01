import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from config import TELEGRAM_TOKEN
from prompts import SYSTEM_PROMPT
from gigachat_client import GigaChatClient
from state_manager import StateManager

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

state_manager = StateManager()
llm = GigaChatClient(system_prompt=SYSTEM_PROMPT)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    state_manager.update_state(user.id, started=True)
    text = (
        "Привет! 👋 Я твой гид по Стамбулу!\n\n"
        "Чем помочь?\n\n"
        "1️⃣ Маршрут на 6 дней\n"
        "2️⃣ Рекомендации прямо сейчас\n"
        "3️⃣ Ответить на вопрос\n"
        "4️⃣ Спланировать один день\n"
        "5️⃣ Рекомендации по еде\n"
        "6️⃣ Фото-локации\n"
        "7️⃣ Необычные опыты\n\n"
        "Напиши цифру или опиши, что тебе нужно 🎯"
    )
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я могу помочь спланировать путешествие в Стамбул!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.strip()
    state = state_manager.get_state(user.id)
    reply = llm.generate(text)
    await update.message.reply_text(reply)

def main():
    if not TELEGRAM_TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN not found")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
