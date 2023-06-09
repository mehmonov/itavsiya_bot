from aiogram import types
from keyboards.default.infoItKeyboard import infoItKeyboard
from loader import dp

@dp.message_handler(text="🚀 IT sohalari bo'yicha ma'lumotlar")
async def get_it_info(message: types.Message):
    await message.answer("🚀 IT sohalari bo'yicha ma'lumotlar", reply_markup=infoItKeyboard)