from telegram.ext import ContextTypes
from telegram import Update

from welcome import vacation_button_handler, next_vacation_button_handler
from mailto import normal_vacation_with_bsc
from formatter import show_document
from vacation_end import show_jira_task


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """хэндер нажатий на кнопки"""
    command = update.callback_query.data

    if command == "/vacation":
        await vacation_button_handler(update, context)
    if command == "/next_vacation":
        await next_vacation_button_handler(update, context)
    if command == "project_vacation_agreed":
        await normal_vacation_with_bsc(update, context)
    elif command == "bsc_vacation_agreed":
        await show_document(update, context)
    elif command == "signed":
        await show_jira_task(update, context)
    elif command == "/mock":
        await mock_handler(update, context)


async def mock_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Данный функционал находится в разработке",
    )
