from telegram.ext import ContextTypes
from telegram import Update
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

from welcome import vacation_button_handler, next_vacation_button_handler
from mailto import normal_vacation_with_bsc, normal_vacation_with_project
from formatter import show_document
from vacation_end import show_jira_task
from dateselector import select_start_date, get_calendar_result, calendar_edit, select_end_date, \
    process_calendar_result, current_calendar_selection


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """хэндлер нажатий на кнопки"""
    command = update.callback_query.data
    calendar1_result, calendar1_key, calendar1_step = get_calendar_result(update, 1)
    calendar2_result, calendar2_key, calendar2_step = get_calendar_result(update, 2)

    if command == "/next_vacation":
        await next_vacation_button_handler(update, context)
    elif command == "select_start_date":
        await select_start_date(update, context)
    elif command == "start_vacation_process":
        await normal_vacation_with_project(update, context)
    elif command == "project_vacation_agreed":
        await normal_vacation_with_bsc(update, context)
    elif command == "bsc_vacation_agreed":
        await show_document(update, context)
    elif command == "signed":
        await show_jira_task(update, context)
    elif command == "/mock":
        await mock_handler(update, context)
    elif not calendar1_result and calendar1_key:
        await calendar_edit(update, context, calendar1_key, 1)
    elif not calendar2_result and calendar2_key:
        await calendar_edit(update, context, calendar2_key, 2)
    elif calendar1_result and current_calendar_selection(context) == 1:
        await select_end_date(update, context, calendar1_result)
    elif calendar2_result and current_calendar_selection(context) == 2:
        await process_calendar_result(update, context, calendar2_result)


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "отпуск".lower() in text.lower():
        await vacation_button_handler(update, context)


async def mock_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Данный функционал находится в разработке",
    )
