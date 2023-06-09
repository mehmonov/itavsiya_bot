from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

web = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📹 Online videodarslar"),
            KeyboardButton(text="🏢 Offline darslar"),   
        ],
        [
            KeyboardButton(text="📚 Kitoblar"),
            KeyboardButton(text="📝 Testlar"),
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)