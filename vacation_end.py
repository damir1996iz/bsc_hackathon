from telegram.ext import ContextTypes
from telegram import Update


VACATION_TASK = "https://cz-support.finshape.com/jira/browse/P20009352-969"


async def show_jira_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Не забудьте списать время в задачу {task} по 8 часов в каждый рабочий день".format(
            task=VACATION_TASK
        )
    )
