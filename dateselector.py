from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP, DAY
from telegram.ext import ContextTypes
from telegram import Update
from context import get_context
from mailto import normal_vacation_with_project


async def select_date(update: Update, context: ContextTypes.DEFAULT_TYPE, calendar_id: int):
    context.chat_data["current_calendar"] = calendar_id
    d = DetailedTelegramCalendar(calendar_id=calendar_id)
    d.step = DAY
    d._build(step=DAY)
    calendar, step = d.build()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_prompt(calendar_id),
        reply_markup=calendar
    )


async def select_start_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await select_date(update, context, 1)


def get_calendar_result(update: Update, calendar_id: int):
    try:
        return DetailedTelegramCalendar(calendar_id=calendar_id).process(update.callback_query.data)
    except:
        return None, None, None


async def calendar_edit(update: Update, context: ContextTypes.DEFAULT_TYPE, calendar_key, calendar_id):
    await context.bot.edit_message_text(
        text=get_prompt(calendar_id),
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        reply_markup=calendar_key
    )


def get_prompt(calendar_id: int):
    if calendar_id == 1:
        return "Выберите дату начала отпуска"
    elif calendar_id == 2:
        return "Выберите дату окончания отпуска"
    else:
        return None


async def select_end_date(update: Update, context: ContextTypes.DEFAULT_TYPE, calendar_result):
    context.chat_data["calendar1_result"] = calendar_result
    await select_date(update, context, 2)


async def process_calendar_result(
        update: Update, context: ContextTypes.DEFAULT_TYPE, calendar2_result
):
    context.chat_data["current_calendar"] = None
    vacation = await get_context(context, update, "next_vacation")
    vacation.start_date = context.chat_data["calendar1_result"]
    vacation.end_date = calendar2_result
    context.chat_data["next_vacation"] = vacation
    await normal_vacation_with_project(update, context)


def current_calendar_selection(context: ContextTypes.DEFAULT_TYPE):
    return context.chat_data["current_calendar"]
