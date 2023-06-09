from aiogram import types
from keyboards.default.dasturlash.web import web
from loader import dp
from keyboards.inline.frontAndBackend import fbk
@dp.callback_query_handler(text="frontend")
async def get_frontend_info(call: types.CallbackQuery):
    await call.message.answer(f"Frontend \n \n "
          " Frontend - bu veb texnologiyalarning biridir. Bu texnologiya yordamida veb sahifalarning insonga ko‘rinib turuvchi, ma’lumot beruvchi vizual qismi yaratiladi.  Frontend texnologiyalarini o‘rgangan inson o‘z ijodkorligi, kretiv yondoshuvi orqali turli g‘oyalarini veb sahifalar, dasturlar shaklida ro‘yobga chiqarishi mumkin bo‘ladi"
          "Frontend darslari uchun quyidagi linkka o'ting: \n -> https://www.youtube.com/@UlugbekSamigjonov",
          reply_markup=web)
@dp.callback_query_handler(text="backend")
async def get_backend_info(call: types.CallbackQuery):
    await call.message.answer(f"Backend dasturlash \n \n "
"Backend dasturlashda siz server tomonida ishlovchi kodlarni yozasiz va ma’lumotlar bazasi bilan ishlaysiz. Backend dasturchilar uchun kerakli bo’lgan dasturlash tillari orasida PHP, Python, Ruby va boshqalar bor." "    Backend darslari uchun quyidagi linkka o'ting: \n -> https://www.youtube.com/@UlugbekSamigjonov",
    )


@dp.message_handler(text="🌐 Web dasturlash")
async def get_web_info(message: types.Message):
    await message.answer(f"Web dasturlash",
          reply_markup=web)
    await message.answer(
        " Web dasturlash ham juda qiziqarli va katta daromad keltiradigan soha hisoblanadi \n \n Frontend - bu veb texnologiyalarning biridir. Bu texnologiya yordamida veb sahifalarning insonga ko‘rinib turuvchi, ma’lumot beruvchi vizual qismi yaratiladi.  Frontend texnologiyalarini o‘rgangan inson o‘z ijodkorligi, kretiv yondoshuvi orqali turli g‘oyalarini veb sahifalar, dasturlar shaklida ro‘yobga chiqarishi mumkin bo‘ladi\n\n Backend dasturlash - bu veb-sayt yoki dasturiy ta’minot dasturining foydalanuvchilar ko’rmaydigan har qanday qismiga ishora qiladi1. Backend jarayonlariga misollar: kiruvchi veb-sahifa so’rovini qayta ishlash, HTML yaratish uchun skriptni ishga tushirish (PHP, ASP, JSP va boshqalar) \n\nBackend dasturlashda siz server tomonida ishlovchi kodlarni yozasiz va ma’lumotlar bazasi bilan ishlaysiz. Backend dasturchilar uchun kerakli bo’lgan dasturlash tillari orasida PHP, Python, Ruby va boshqalar bor.", 
        reply_markup=fbk)   
@dp.message_handler(text="📹 Online videodarslar")
async def get_web_video(message: types.Message):
    await message.answer(text="📹 Online videodarslar")
    await message.answer(
        f"Youtube orqali o'rganish uchun quyidagi linkka o'ting:\n -> https://www.youtube.com/@UlugbekSamigjonov/playlists"
    )
    await message.answer(
        "Darslar qo'shib boriladi tez orada"
    )
@dp.message_handler(text="🏢 Offline darslar")
async def get_web_offline(message: types.Message):
    await message.answer(text="🏢 Offline darslar")
    await message.answer(
        "Offline darslar bo'yicha ma'lumotlar tez orada qo'shiladi"
    )
    
@dp.message_handler(text="📚 Kitoblar")
async def get_web_books(message: types.Message):
    await message.answer(text="📚 Kitoblar")
    await message.answer(
        "Anvar Narzullayev "
        "Ushbu kitob bugungi kunda dasturlash asoslariga oid o‘zbek tilidagi mukammal tuzilgan qo‘llanmalardan biridir. Qo‘lingizdagi kitobning o‘ziga xos jihati shundaki, uning har bir bo‘limi uchun tayyorlangan qo‘shimcha onlayn materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg‘ulotlar va vazifalarning kodlari eʼtiboringizga havola etilgan. O‘quvchilar bu materiallarni maxsus QR kod yordamida o‘z kompyuterlariga yuklab olib, ulardan unumli foydalanishi mumkin."
        "https://asaxiy.uz/uz/product/anvar-narzullaev-pythonda-dasturlash-asoslari"
    )
    