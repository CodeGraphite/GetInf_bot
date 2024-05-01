from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


viloyatlar = {
    "Andijon":'Andijon',
    "Buxoro":'buxoro',
    "Farg'ona":'fargona',
    "Jizzax":'jizzax',
    "Xorazm":'xorazm',
    'Namangan':'namangan',
    "Navoiy":'navoiy',
    "Qashqadaryo":'qashqadaryo',
    "Qoraqalpog'iston":'qoraqalpogiston',
    "Samarqand":'samarqand',
    "Sirdaryo":'sirdaryo',
    "Surxondaryo":'surxondaryo',
    "Toshkent viloyati":'toshkent_vil',
    "Toshkent shahri":'toshkent'
}

async def main_menu_btns():
    main_menu_btns = InlineKeyboardMarkup(row_width=2)
    for key_ in viloyatlar:
        main_menu_btns.insert(
            InlineKeyboardButton(text=key_, callback_data=f'vil_{key_}')
        )
    return main_menu_btns


yes_or_no = {
    "Ha":'yes',
    "Yo'q":'no'
}
async def main_yes_no():
    main_menu_btns = InlineKeyboardMarkup(row_width=2)
    for key_, value_ in yes_or_no.items():
        main_menu_btns.insert(
            InlineKeyboardButton(text=key_, callback_data=value_)
        )
    return main_menu_btns
















