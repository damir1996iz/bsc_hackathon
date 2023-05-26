import logging

import telegram.ext.filters
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler

from auth import TOKEN
from start import start
from message_handler import callback_query_handler, message_handler
from mailto import normal_vacation_with_project

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token(TOKEN).build()

start_handler = CommandHandler('start', start)
normal_vacation_with_project_handler = CommandHandler('vacation_with_project', normal_vacation_with_project)
application.add_handler(start_handler)
application.add_handler(normal_vacation_with_project_handler)
application.add_handler(CallbackQueryHandler(callback_query_handler))
application.add_handler(MessageHandler(telegram.ext.filters.TEXT, message_handler))

application.run_polling()
