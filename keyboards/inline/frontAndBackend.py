from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

fbk = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Frontend haqiqda", callback_data="frontend"),
        ],
        [
            InlineKeyboardButton(text="Backend haqida", callback_data="backend"),
        ]
    ]
)