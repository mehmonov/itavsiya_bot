from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


dsk = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Web dasturlash"),
            KeyboardButton(text="📱 Mobil dasturlash"),
        ],
        [
            KeyboardButton(text="🖥 Desktop dasturlash"),
            KeyboardButton(text="🤖 Telegram bot dasturlash"),
            
        ],
        [
            KeyboardButton(text="⚙️ Sun’iy intellekt va ma’lumotlar fanlari"),
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
        
    ],
    resize_keyboard=True
)