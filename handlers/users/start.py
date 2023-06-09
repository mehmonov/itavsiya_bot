from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu
from loader import dp
@dp.message_handler(text='Bosh menu')
async def bosh_menu(message: types.Message):
    await message.answer('Bosh menyu', reply_markup=menu)
    
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu)
