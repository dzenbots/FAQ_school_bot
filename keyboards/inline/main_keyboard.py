from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

main_callback_data = CallbackData('main_callback', 'function')
back_callback_data = CallbackData('back', 'function')

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Основная информация',
                callback_data=main_callback_data.new(
                    function='function1'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Расписание смены',
                callback_data=main_callback_data.new(
                    function='function2'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Распорядок дня',
                callback_data=main_callback_data.new(
                    function='function3'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Стоимость',
                callback_data=main_callback_data.new(
                    function='function4'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Часто задаваемые вопросы',
                callback_data=main_callback_data.new(
                    function='function5'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Подать заявку!',
                url='https://doc-10-88-docs.googleusercontent.com/docs/securesc/bf2fht89abetjaebdgcasq78hok2alqv/b5qfgahd4m81o4nh8gt38j5o2n9aoccp/1682092575000/16108819346713437606/03428597177388494783/1_afz8kwAV_yH92qPFJ8nq6-KhGt8vOIF?ax=ALy03A6eH0dcRTE7uWmekFVWKmi5PPAx1cmiIxh-ByY52eAzRXxbBjpXMaGR9LtDM9hfSXUlsgAHJHlYBpr-x5NITVnYI7t6T859irE9PE_6ef7t-TMdU30FK7RCztHpZZ3QXezTLz51LCTT5lX8MbVQOSehd3e6Xtj-ZiPDDFGFOPSnUo8hmydVEUpwN6Q3pERtO7HxDl_iHnJPv0PGXlrd8oLAuN56p5aK7vv3dq0BybZlv5eFM7Euv73y-6MgIOKsH5acQRobO58F7batiBjVG80W4j2Ye2mwwtRE280kd-nqB8Eg1pJkkkTo9YgrhUht_ZB_QvogYPeD7L8TgOuQDDfxIN_S_4hMc9At4MRpiC5Gp4XwUNHBcZWwkh49yA2q7U7GVVY2HMf0qUV0eebAql2HBoZd784whccSYRoNba712uwikqSPJPO8Gs6gpQd9EaadRvgu5wk6VowWWd-Y0Y3mP3PdwbK_e3XMcGZPP4D3gTF7UFnF8StLIlaBTcPAH4AyQ28uYP5F0QWZEw8b93aYoTeZYm5nbmNIaEEkEGZyhnQRP299UexLwBz9EKReOfdl8NSUuoNjgNVwMsSyNUt5EOsIrYhiJn0fAPU4US6pqZMH7sFDitAFpEwnbyyJ02E3z16w-qQ0970lNdPnBqatJh__q0pp2XJ5KB5DPKnb7q_x8fpQS2jmlX45eIyXM3mdm45huxilcCTqCHWszSYWcAvurvIGehwgdDsgGBPcSGT28CmGZWr72BGFQYjKGlianTjoZGUH1s0MogULT9WCuYFiRYjfqTjGFrwXUc_6G0dqrqSI9WxXvJ6of6ovXs5ClegKMSC8XZxFrYlniws9Sn-Ur3L1Nda6LMB3uGRqiDXLKTS-455Xh8cwsm5uhNvrFskXakESNigh9SHP_SyF5ukP0u65mMOLxbtUR_-H3PB5b_AKG-59MJMhNtbWKqg1WTEg&uuid=0151f7aa-6c32-4d5c-b5b5-19728af36c60&authuser=0&nonce=c0qghp7fpvv8c&user=03428597177388494783&hash=jkgoer54cltotitlveiam1c49qkaabn9'
            )
        ]
    ]
)

return_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Назад',
                callback_data=back_callback_data.new(
                    function='back'
                )
            )
        ]
    ]
)