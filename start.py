from telegram import Update
from telegram.ext import ContextTypes
from confluence import get_username_by_tg
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    keyboard = [
        [
            InlineKeyboardButton(text="Отпуск", callback_data="/vacation")
        ]
    ]

    markup = InlineKeyboardMarkup(keyboard)

    user_name = get_username_by_tg(update.effective_chat.username)
    context.chat_data["user_name"] = user_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Здравствуйте, " + user_name,
        reply_markup=markup
    )
