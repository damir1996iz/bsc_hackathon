from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from main import botStrings
from user_registration import UserRegistration


def bot_messages(dp: Dispatcher):
    """Функция обработки сообщений"""
    @dp.message_handler(commands=["start"])
    async def start(message: types.Message, state: FSMContext):
        """Функция обработки /start"""
        async with state.proxy() as user_data:
            if "name" not in user_data.keys():
                await UserRegistration.surname.set()
                await message.reply(botStrings["welcomeTextUnregistered"])
            else:
                await message.reply(botStrings["welcomeTextRegistered"].format(user_data["name"]))

    @dp.message_handler(state=UserRegistration.surname)
    async def registration_surname(message: types.Message, state: FSMContext):
        """Функция обработки ввода фамилии"""
        async with state.proxy() as user_data:
            user_data["surname"] = message.text
        await UserRegistration.next()
        await message.reply(botStrings["registrationName"])

    @dp.message_handler(state=UserRegistration.name)
    async def registration_name(message: types.Message, state: FSMContext):
        """Функция обработки ввода имени"""
        async with state.proxy() as user_data:
            user_data["name"] = message.text
        await UserRegistration.next()
        await message.reply(botStrings["registrationMiddleName"])

    @dp.message_handler(state=UserRegistration.middle_name)
    async def registration_middle_name(message: types.Message, state: FSMContext):
        """Функция обработки ввода отчества"""
        async with state.proxy() as user_data:
            user_data["middle_name"] = message.text
            await message.reply(botStrings["registrationCompleted"].format(
                user_data["surname"],
                user_data["name"],
                user_data["middle_name"]
            ))
        await UserRegistration.next()
