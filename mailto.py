from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from urllib.parse import quote
from confluence import get_user_vacations, get_username_by_tg

REDIRECT_SERVER = "http://185.46.11.250/mailto/"


def mailto(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
            message: str, button: str, agreed_command: str,
        emails: str, subject: str, body: str):
    url = REDIRECT_SERVER + "?emails={emails}&subject={subject}&body={body}".format(
                emails=emails,
                subject=quote(subject, "utf-8"),
                body=quote(body, "utf-8"),
            )
    keyboard = [[
        InlineKeyboardButton(button, url=url),
        InlineKeyboardButton("Уже согласовано", callback_data=agreed_command)
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    return context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        reply_markup=reply_markup
    )


def normal_vacation_mailto(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
        message: str, button: str, agreed_command: str,
        emails: str, from_date: str, to_date: str):
    return mailto(
        update, context, message, button, agreed_command, emails,
        subject="Очередной отпуск с {fromDate} по {toDate}".format(fromDate=from_date, toDate=to_date),
        body="Прошу согласовать очередной отпуск с {fromDate} по {toDate}".format(fromDate=from_date, toDate=to_date),
    )


async def normal_vacation_with_project(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vacations = get_user_vacations(get_username_by_tg(update.effective_chat.username))
    if len(vacations) > 0:
        vacation = vacations[0]
        message = "Давайте согласуем ближайший очередной отпуск"
        button = "Согласовать с проектом"
        await normal_vacation_mailto(
            update, context, message, button,
            "project_vacation_agreed",
            vacation.project_approvers,
            vacation.start_date,
            vacation.end_date)


async def normal_vacation_with_bsc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vacations = get_user_vacations(get_username_by_tg(update.effective_chat.username))
    if len(vacations) > 0:
        vacation = vacations[0]
        message = "При согласовании отпуска внутри компании не забудьте вложить письмо с согласование на проекте."
        button = "Согласовать в БСЦ"
        await normal_vacation_mailto(
            update, context, message, button,
            "bsc_vacation_agreed",
            vacation.bsc_approvers,
            vacation.start_date,
            vacation.end_date)
