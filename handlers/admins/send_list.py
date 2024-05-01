from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, db

import pandas as pd

@dp.message_handler(commands=['give_list'], state='*', user_id = ADMINS)
async def send_welcome(message: types.Message, state: FSMContext):
    info = db.give_all_info()
    df = pd.DataFrame({'id': [id[0] for id in info],
                    'username': [username[1] for username in info],
                    'viloyat': [viloyat[2] for viloyat in info],
                    'tuman':[tuman[3] for tuman in info],
                    'ism familiya':[ism_familiya[4] for ism_familiya in info],
                    'telefon':[telefon[5] for telefon in info]
                    })
    df.to_excel('data/base_info.xlsx',sheet_name='1',index=False)
    
    await message.answer_document(open('data/base_info.xlsx', 'rb'))
    await state.finish()
    await state.reset_data()

