from aiogram import types
from keyboards.default.dasturlashSohalariKeyboard import dsk
from loader import dp

@dp.message_handler(text="🧩 Dasturlash")
async def get_it_code(message: types.Message):
    await message.answer("🧩 Dasturlash \n \n "
                         "Dasturlash - bu kompyuterlar va boshqa mikroprotsessorli elektron mashinalar uchun dasturlar tuzish, sinash va oʻzgartirish jarayonidan iborat. Odatda dasturlash yuqori saviyali dasturlash tillari (PHP, Java, C++, Python) vositasida amalga oshiriladi. Bu dasturlash tillarining semantikasi odam tiliga yaqinligi tufayli dastur tuzish jarayoni ancha oson kechadi.\n\n Dasturlashning ko’plab sohalari mavjud, jumladan web dasturlash, mobil ilovalar yaratish, ma’lumotlar bazasi bilan ishlash va boshqalar. Dasturlashni o’rganish juda qiziqarli va foydali mashg’ulot hisoblanadi."
                         
                         , reply_markup=dsk)
    
  