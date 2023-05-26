from telegram.ext import ContextTypes
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from confluence import get_username_by_tg, get_user_vacations


async def vacation_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка /vacation"""

    message = "Вы выбрали функционал согласования отпусков"

    keyboard = [[
        InlineKeyboardButton(text="Оплачиваемый", callback_data="/next_vacation")
    ]]

    markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        reply_markup=markup
    )


async def next_vacation_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка /next_vacation"""

    vacation_list = get_user_vacations(get_username_by_tg(update.effective_chat.username))

    if len(vacation_list) == 0:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Я тебя не нашел в графике отпусков. Обратись в отдел кадров."
        )

    near_vacation = sorted(vacation_list, key=lambda item: item.start_date)[0]

    message = "Ближайший отпуск запланирован с {} по {}".format(
        near_vacation.start_date.strftime("%d-%m-%Y"),
        near_vacation.end_date.strftime("%d-%m-%Y")
    )

    keyboard = [[
        InlineKeyboardButton(text="Продолжить оформление", callback_data="project_vacation_agreed"),
        InlineKeyboardButton(text="Другие даты", callback_data="/mock")
    ]]

    markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        reply_markup=markup
    )
