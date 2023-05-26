from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from urllib.parse import quote

REDIRECT_SERVER = "http://185.46.11.250/mailto/"


def mailto(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
        message: str, button: str,
        emails: str, subject: str, body: str):
    url = REDIRECT_SERVER + "?emails={emails}&subject={subject}&body={body}".format(
                emails=emails,
                subject=quote(subject, "utf-8"),
                body=quote(body, "utf-8"),
            )
    keyboard = [[InlineKeyboardButton(button, url=url)]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    return context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        reply_markup=reply_markup
    )


def normal_vacation_mailto(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
        message: str, button: str,
        emails: str, from_date: str, to_date: str):
    return mailto(
        update, context, message, button, emails,
        subject="Очередной отпуск с {fromDate} по {toDate}".format(fromDate=from_date, toDate=to_date),
        body="Прошу согласовать очередной отпуск с {fromDate} по {toDate}".format(fromDate=from_date, toDate=to_date),
    )


async def normal_vacation_with_project(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from_date = "10.06.2023"
    to_date = "20.06.2023"
    message = "Давайте согласуем ближайший очередной отпуск"
    button = "Согласовать с проектом"
    emails = "user1@server1.ru;user2@server2.ru"
    await normal_vacation_mailto(update, context, message, button, emails, from_date, to_date)
