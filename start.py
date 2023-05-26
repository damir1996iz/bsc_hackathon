from telegram.ext import ContextTypes
from confluence import get_username_by_tg
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from context import get_context


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    keyboard = [
        [
            KeyboardButton(text="Отпуск")
        ]
    ]

    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    user_name = await get_context(context, update, "user_name")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Здравствуй! Я тебя узнал. Ты – " + user_name,
        reply_markup=markup
    )
