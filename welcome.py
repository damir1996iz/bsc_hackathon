from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes
from context import get_context
from dateselector import select_start_date

async def vacation_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка /vacation"""

    message = "Выбери, какой отпуск оформляем (также ты можешь ознакомиться с <a " \
              "href=\"https://cz-support.finshape.com/confl/x/na5eBQ\">регламентами</a> самостоятельно):"

    keyboard = [
        [InlineKeyboardButton(text="Sick day", callback_data="/mock"),
         InlineKeyboardButton(text="Оплачиваемый", callback_data="/next_vacation")],
        [InlineKeyboardButton(text="За свой счет", callback_data="/mock"),
         InlineKeyboardButton(text="Больничный", callback_data="/mock")],
        [InlineKeyboardButton(text="Учебный", callback_data="/mock"),
         InlineKeyboardButton(text="По беременности", callback_data="/mock")],
        [InlineKeyboardButton(text="Уход за ребенком", callback_data="/mock")]
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        reply_markup=markup,
        parse_mode="html"
    )


async def next_vacation_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка /next_vacation"""
    try:
        near_vacation = await get_context(context, update, "next_vacation", True)

        if (near_vacation.start_date == "") or (near_vacation.end_date == ""):
            await select_start_date(update, context)
            return

        message = "У тебя запланирован отпуск с {} по {}. Оформляем?".format(
            near_vacation.start_date.strftime("%d-%m-%Y"),
            near_vacation.end_date.strftime("%d-%m-%Y")
        )

        keyboard = [[
            InlineKeyboardButton(text="Да, оформляем", callback_data="start_vacation_process"),
            InlineKeyboardButton(text="Нет, другие даты", callback_data="select_start_date")
        ]]

        markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
            reply_markup=markup
        )
    except ValueError as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ошибка в форматировании таблицы"
        )
