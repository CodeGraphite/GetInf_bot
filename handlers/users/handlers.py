from loader import dp, db, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.inline.menu import *
from keyboards.inline.admin_menu import *
from keyboards.default.menu import send_contact_btn

from data.config import ADMINS
from states.state import UserData



@dp.callback_query_handler(Text(startswith='vil_'))
async def send_welcome(call: types.CallbackQuery, state:FSMContext):
    await state.update_data(viloyat=call.data[4:])
    await call.message.answer('Tumanni kiriting:')
    await UserData.tuman.set()
    await call.message.delete()

@dp.message_handler(content_types='text',state=UserData.tuman)
async def bot_start(message: types.Message, state: FSMContext):
    await state.update_data(tuman=message.text)
    await message.answer("To'liq ism va familyangizni yuboring!")
    await UserData.ism_familiya.set()

@dp.message_handler(content_types='text',state=UserData.ism_familiya)
async def bot_start(message: types.Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await message.answer("Telefon raqamingizni yuboring!",reply_markup=send_contact_btn)
    await UserData.telefon.set()


@dp.message_handler(content_types=['contact','text'],state=UserData.telefon)
async def bot_start(message: types.Message, state: FSMContext):
    if message.contact:
        await state.update_data(telefon= message.contact['phone_number'])
    else:
        await state.update_data(telefon= message.text)
    data = await state.get_data()
    viloyat = data.get('viloyat')
    tuman = data.get('tuman')
    ism_familiya = data.get('ism_familiya')
    telefon = data.get('telefon')
    await message.answer("Ma'lumotlarni tekshiring!",reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"\nViloyat: {viloyat}\nTuman: {tuman}\nIsm va Familiya: {ism_familiya}\nTelefon: {telefon}", reply_markup=await main_yes_no())
    await UserData.check.set()


@dp.callback_query_handler(text= ["yes","no"],state=UserData.check)
async def yes_or_not(call: types.CallbackQuery,state: FSMContext):
    if call.data == 'yes':
        data = await state.get_data()
        viloyat = data.get('viloyat')
        tuman = data.get('tuman')
        ism_familiya = data.get('ism_familiya')
        telefon = data.get('telefon')
        await call.message.answer(db.add_info(call.from_user.id,call.from_user.username,viloyat,tuman,ism_familiya,telefon))
        await state.finish()
        await state.reset_data()
        await call.message.delete()
    else:
        await state.finish()
        await state.reset_data()
        await call.message.answer("Ma'lumotlarni qayta to'ldirish uchun /start komandasini yuboring!🔥")
        await call.message.delete()

