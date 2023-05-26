from telegram.ext import ContextTypes
from confluence import get_username_by_tg, get_user_vacations
from telegram import Update


async def get_context(context: ContextTypes.DEFAULT_TYPE, update: Update, key: str):
    if key not in context.chat_data.keys():
        if key == "user_name":
            user_name = get_username_by_tg(update.effective_chat.username)
            context.chat_data["user_name"] = user_name
            return user_name
        if key == "next_vacation":
            try:
                vacation_list = get_user_vacations(await get_context(context, update, "user_name"))
            except:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Ошибка в форматировании таблицы"
                )
                return

            if len(vacation_list) == 0:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Я тебя не нашел в графике отпусков. Обратись в отдел кадров."
                )

            near_vacation = sorted(vacation_list, key=lambda item: item.start_date)[0]
            context.chat_data["next_vacation"] = near_vacation
            return near_vacation
    else:
        return context.chat_data[key]
