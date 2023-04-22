import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton

from data.config import del_messages
from keyboards.inline import main_callback_data, return_keyboard, back_callback_data, main_keyboard
from loader import dp


@dp.callback_query_handler(main_callback_data.filter(function='function1'))
async def function1(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if call.message.chat.id in del_messages.keys():
        for message in del_messages.get(call.message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    if call.message.chat.id not in del_messages.keys():
        del_messages[call.message.chat.id] = list()
    del_messages[call.message.chat.id].append(
        await dp.bot.send_photo(
            chat_id=call.message.chat.id,
            photo='https://drive.google.com/uc?id=1vzLIlj-nmXeXQonoJL7zXU7RQKbDhrNR',
            caption=''.join(
                (
                    '<b>Основная информация</b>',
                    '',
                    '<b>В нашем лагере планируются две смены</b> с 29 мая по 16 июня и с 19 июня по 7 июля. Каждый день мы будем встречать детей в 9 часов утра и отпускать домой в 6 часов вечера.',
                    '<b>Лагерь будет организован на территории  второго учебного корпуса нашей школы</b>, Москва, Карельский бульвар, 20.'
                )
            ),
            reply_markup=return_keyboard
        )
    )


@dp.callback_query_handler(main_callback_data.filter(function='function2'))
async def function2(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if call.message.chat.id in del_messages.keys():
        for message in del_messages.get(call.message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    if call.message.chat.id not in del_messages.keys():
        del_messages[call.message.chat.id] = list()
    del_messages[call.message.chat.id].append(
        await dp.bot.send_photo(
            chat_id=call.message.chat.id,
            photo='https://drive.google.com/uc?id=1WqzRupzheYgoQx7Q8pNAy9P21_zrxmdw',
            reply_markup=return_keyboard
        )
    )


@dp.callback_query_handler(main_callback_data.filter(function='function3'))
async def function3(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if call.message.chat.id in del_messages.keys():
        for message in del_messages.get(call.message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    if call.message.chat.id not in del_messages.keys():
        del_messages[call.message.chat.id] = list()
    del_messages[call.message.chat.id].append(
        await dp.bot.send_photo(
            chat_id=call.message.chat.id,
            photo='https://drive.google.com/uc?id=1jhYpysg0YBGfkzvzFex9F8JufvuU-gWh',
            reply_markup=return_keyboard
        )
    )


@dp.callback_query_handler(main_callback_data.filter(function='function4'))
async def function4(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if call.message.chat.id in del_messages.keys():
        for message in del_messages.get(call.message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    if call.message.chat.id not in del_messages.keys():
        del_messages[call.message.chat.id] = list()
    del_messages[call.message.chat.id].append(
        await dp.bot.send_photo(
            chat_id=call.message.chat.id,
            caption='Стоимость одной смены 20 000,00 (двадцать тысяч) рублей . Весь расходный материал и сопутствующие услуги (экскурсии, питания) уже включены.',
            photo='https://drive.google.com/uc?id=1js5lypL_R1Rjm2BuZbXQ7NuOdIp1fzc1',
            reply_markup=return_keyboard
        )
    )


@dp.callback_query_handler(main_callback_data.filter(function='function5'))
async def function5(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if call.message.chat.id in del_messages.keys():
        for message in del_messages.get(call.message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    if call.message.chat.id not in del_messages.keys():
        del_messages[call.message.chat.id] = list()
    del_messages[call.message.chat.id].append(
        await dp.bot.send_photo(
            chat_id=call.message.chat.id,
            photo='https://drive.google.com/uc?id=1eUqIKwlWO8xT0gvgIPniv_ejubclVswu'
        )
    )
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Надо будет давать с собой еду ребенку?</b>',
                    'Нет, будет организовано горячее питание не менее двух раз за день.',
                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Из чего состоит Программа лагеря?</b> ',
                    'Игры на свежем воздухе, погружение в гуманитарные, технические и спортивные профессии, киберспорт, квизы, квесты.',
                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Возможно оплатить частями?</b>',
                    'Да, вноситься 50% предоплата до начала смены, затем, по завершению первой недели смены вносится остаток.',
                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Кто работает с детьми?</b>',
                    'Команда, состоящая их профессиональных вожатых, педагогов и методистов с многолетним стажем, учителей высшей категории.',
                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Сколько человек в отряде?</b>',
                    'Планируются группы по 15 детей.'
                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>До какого числа производиться запись?</b>',
                    'Запись производится до 10:00 15 мая 2023',

                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Какие документы нужны помимо договора?</b>',
                    'Необходимо будет предоставить справку от терапевта для физкультурных занятий.',

                )
            )
        )
    )
    await asyncio.sleep(1)
    del_messages[call.message.chat.id].append(
        await dp.bot.send_message(
            chat_id=call.message.chat.id,
            text='\n'.join(
                (
                    '<b>Можно ли получить туристический кэшбек по программе?</b>',
                    'Нет, но на образовательную смену можно будет оформить налоговый вычет.'
                )
            ),
            reply_markup=return_keyboard
        )
    )


@dp.callback_query_handler(back_callback_data.filter(function='back'))
async def function_back(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if call.message.chat.id in del_messages.keys():
        for message in del_messages.get(call.message.chat.id):
            try:
                await dp.bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=message.message_id
                )
            except:
                pass
    del_messages[call.message.chat.id] = list()
    del_messages[call.message.chat.id].append(
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
