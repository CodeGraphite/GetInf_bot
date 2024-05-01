from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, db
from data.config import ADMINS


    

@dp.message_handler(commands='followers', state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()
    text = f"""📊 Loyiha statistikasi:
===========================
👻 Jami foydalanuvchilar: {len(db.give_all_users())} ta 
==========================="""
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
