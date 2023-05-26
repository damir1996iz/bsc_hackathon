import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from auth import TOKEN
from start import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token(TOKEN).build()

start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

application.run_polling()
