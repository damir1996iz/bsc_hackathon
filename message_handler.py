from telegram.ext import ContextTypes
from telegram import Update

from welcome import vacation_button_handler
from mailto import normal_vacation_with_bsc


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """хэндер нажатий на кнопки"""
    command = update.callback_query.data

    if command == "/vacation":
        await vacation_button_handler(update, context)
    elif command == "project_vacation_agreed":
        await normal_vacation_with_bsc(update, context)
