from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from data.config import del_messages
from keyboards.inline import main_keyboard
from loader import dp
from utils.set_bot_commands import set_default_commands


@dp.message_handler()
async def main_menu_text(message: Message):
    await bot_start(message)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    if message.chat.id in del_messages.keys():
    #
    # if del_messages[message.chat.id]:
        for message in del_messages.get(message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    del_messages[message.chat.id] = list()
    del_messages[message.chat.id].append(
        await message.answer_photo(
            photo='https://drive.google.com/uc?id=1vzLIlj-nmXeXQonoJL7zXU7RQKbDhrNR',
        )
    )
    del_messages[message.chat.id].append(
        await message.answer(
            text='\n'.join(
                (
                    "Основное меню",
                    ''
                )
            ),
            reply_markup=main_keyboard
        )
    )
