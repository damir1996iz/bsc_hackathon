from telegram import Update
from telegram.ext import ContextTypes
from confluence import get_username_by_tg

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userName = get_username_by_tg(update.effective_chat.username)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Здравствуйте, " + userName,
    )
