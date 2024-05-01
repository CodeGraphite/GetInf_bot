from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.inline.admin_menu import *
from keyboards.inline.menu import *




@dp.message_handler(commands=['admin'], state='*', user_id = ADMINS)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer("Admin menu:\n\t\t/give_list - ro'yxatni excel formatda olish\n\t\t/give_base - ro'yxatni .db formatda olish", reply_markup= types.ReplyKeyboardRemove())
    await state.finish()
    await state.reset_data()









