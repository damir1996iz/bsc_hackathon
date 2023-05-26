from telegram.ext import ContextTypes
from telegram import Update


async def vacation_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы нажали кнопку отпуск",
    )
