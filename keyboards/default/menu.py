from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="🚀 IT sohalari bo'yicha ma'lumotlar"),
        ],
        [
            KeyboardButton(text="💻 Kompyuter tanlash"),
        ],
        [
            KeyboardButton(text="🔗 Foydali linklar"),
        ]
        
    ]
)