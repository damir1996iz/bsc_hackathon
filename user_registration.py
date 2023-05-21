from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRegistration(StatesGroup):
    """FSM для регистрации пользователя"""

    surname = State()
    """Фамилия"""
    name = State()
    """Имя пользователя"""
    middle_name = State()
    """Отчество"""
