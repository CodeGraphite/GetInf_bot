from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import *
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext


from data.config import ADMINS




@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    text = db.add_user(message)
    if text:
        for admin in ADMINS:
            await bot.send_message(admin, text)
    
    await state.finish()
    await state.reset_data()
    await message.answer("Viloyatingizni tanlang: ", reply_markup= await main_menu_btns())
   


