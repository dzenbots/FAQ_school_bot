from aiogram import types
from aiogram.types import BotCommandScopeChat, Message


async def set_default_commands(dp, message: Message):
    await dp.bot.set_my_commands(
        commands=
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ],
        scope=BotCommandScopeChat(chat_id=message.chat.id)
    )
