from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

pcbuy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Do'konlarni ko'rish", callback_data="buypc")
        ],
    ]
)