from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ks_tanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧩 Dasturlash uchun"),
            KeyboardButton(text="Grafik dizayn uchun"),
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)
