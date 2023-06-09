from aiogram import types
from keyboards.default.dasturlashSohalariKeyboard import dsk
from loader import dp
from keyboards.default.ks_tanlash import ks_tanlash

@dp.message_handler(text="💻 Kompyuter tanlash")
async def get_pc_for_code(message: types.Message):
    await message.answer("Nima uchun kompyuter tanlaymiz? ", reply_markup=ks_tanlash)
    
@dp.message_handler(text="🧩 Dasturlash uchun")
async def get_pc_for_code(message: types.Message):
    await message.answer(
        "Dasturlash uchun kompyuter tanlashda quyidagi omillarni hisobga olish kerak: \n \n ⚙️ Processor: Dasturlash uchun kuchli va tez ishlovchi processor kerak. Intel Core i5 yoki i7, yoki AMD Ryzen 5 yoki 7 kabi processorlar mos keladi. \n \n 💾 Xotira: Dasturlashda ko’p hajmli dasturlar va IDE’larni ishlatish uchun kamida 8GB operativ xotira kerak, ammo 16GB yoki undan ko’p xotira mavjud bo’lsa yanada yaxshi. \n\n 📀 Disk xotirasi: SSD disk xotirasi dasturlar va fayllarni tez ochishga yordam beradi. Kamida 256GB disk xotirasi bo’lsa yaxshi, ammo ko’proq bo’lsa yanada afzal. \n\n 🖥 Ekran: Dasturlashda ko’p oynalar va kodlarni bir vaqtning o’zida ko’rish uchun katta ekran kerak. 15 dyuymdan ko’p ekranli noutbuklar yoki stasionar kompyuterlar uchun 21 dyuymdan ko’p ekranli monitorlar mos keladi. \n \n \n <i>Bizning bot -> https://t.me/itavsiya_bot</i>", )
    
@dp.message_handler(text="Grafik dizayn uchun")
async def get_pc_for_design(message: types.Message):
    await message.answer(
        "Grafik dizayn uchun kompyuter tanlashda quyidagi omillarni hisobga olish kerak:Processor: Grafik dizayn uchun kuchli va tez ishlovchi processor kerak. Intel Core i5 yoki i7, yoki AMD Ryzen 5 yoki 7 kabi processorlar mos keladi.Xotira: Grafik dizayn uchun ko’p hajmli dasturlar va fayllarni ishlatish uchun kamida 8GB operativ xotira kerak, ammo 16GB yoki undan ko’p xotira mavjud bo’lsa yanada yaxshi.Disk xotirasi: SSD disk xotirasi dasturlar va fayllarni tez ochishga yordam beradi. Kamida 256GB disk xotirasi bo’lsa yaxshi, ammo ko’proq bo’lsa yanada afzal.Ekran: Grafik dizayn uchun aniq ranglarni ko’rish uchun sifatli ekran kerak. IPS paneli mavjud bo’lgan ekranlar ranglarni aniqroq ko’rsatadi. Ekran hajmi ham muhim ahamiyatga ega, 15 dyuymdan ko’p ekranli noutbuklar yoki stasionar kompyuterlar uchun 21 dyuymdan ko’p ekranli monitorlar mos keladi.Grafik karta: Grafik dizayn uchun sifatli grafik karta kerak. NVIDIA yoki AMD kompaniyalarining o’rtacha yoki yuqori darajadagi grafik kartalari mos keladi.")
    
@dp.callback_query_handler(text="buypc")
async def get_pc(call: types.CallbackQuery):
    await call.message.answer(
        
    )