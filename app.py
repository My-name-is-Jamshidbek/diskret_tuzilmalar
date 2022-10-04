from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import CommandStart
from states import *
from aiogram.dispatcher import FSMContext
from btn import *
@dp.message_handler(CommandStart())
async def resend(m:types.Message):
    await m.answer('Assalomu aleykum '+str(m.from_user.full_name)+' bu Diskret ko`paytmalar telgram boti bu bot yordamida siz Diskret ko`paytmani osonlik bilan hisoblashingiz mumkin!\kerakli menyuni tanlang:',reply_markup=btn_menu)
    await Yagona.tur.set()
@dp.message_handler(state=Yagona.tur, content_types=types.ContentType.TEXT)
async def tur(msg:types.Message,state:FSMContext):
    if msg.text == 'Boshlash':
        await msg.answer('Iltimos ko`payuvchi to`plamni quyidagi tartibda kiriting:\n2,6,8,3,2,4',reply_markup=btn_bekor)
        await Yagona.soz.set()
    else:
        await msg.answer('Bunday menyu mavjud emas!',reply_markup=btn_menu)
        await Yagona.tur.set()
@dp.message_handler(state=Yagona.soz,content_types=types.ContentType.TEXT)
async def soz(msg:types.Message,state:FSMContext):
    if msg.text == 'Bekor qilish':
        await msg.answer('Bekor qilindi!', reply_markup=btn_menu)
        await Yagona.tur.set()
    else:
        await state.update_data(soz=str(msg.text))
        await msg.answer('Iltimos ko`paytiruvchi to`plamni quyidagi tartibda kiriting:\n6,9,2,64,-34,26',reply_markup=btn_bekor)
        await Yagona.surish.set()
@dp.message_handler(state=Yagona.surish,content_types=types.ContentType.TEXT)
async def surish(msg:types.Message,state:FSMContext):
    try:
        if msg.text == 'Bekor qilish':
            await msg.answer('Bekor qilindi!',reply_markup=btn_menu)
            await Yagona.tur.set()
        baza = await state.get_data()
        toplam0 = baza.get('soz')
        toplam0 = toplam0.split(',')
        toplam1 = msg.text.split(',')
        javob = 'JAVOB:\n{ '
        for i1 in toplam0:
            for i2 in toplam1:
                javob+=f"( {i1} , {i2} ) , "
        javob=javob[:-2]+'}'
        await msg.answer(javob,reply_markup=btn_menu)
        await Yagona.tur.set()
    except:
        await msg.answer('To`plamlardan birida xatolik!', reply_markup=btn_menu)
        await Yagona.tur.set()
