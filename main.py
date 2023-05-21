import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import messages
from bot_strings import BotStrings

# Токен бота
BOT_TOKEN = "5400568258:AAHDIL-T7K8rq5ZubTeWb6JdNjUS43w_Sz0"
# Уровень логирования
LOG_LEVEL = logging.INFO
# Объект работы с текстовками
botStrings = BotStrings("bot_strings.json")
# Объект работы с хранилищем данных
storage = MemoryStorage()


def start_pooling(dp: Dispatcher):
    executor.start_polling(dp, skip_updates=True)


def main():
    """Главная функция бота"""
    logging.basicConfig(level=LOG_LEVEL)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=storage)
    messages.bot_messages(dp)
    start_pooling(dp)


if __name__ == "__main__":
    main()
