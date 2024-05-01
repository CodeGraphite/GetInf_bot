from aiogram.dispatcher.filters.state import State, StatesGroup

class UserData(StatesGroup):
    viloyat = State()
    tuman = State()
    ism_familiya = State()
    telefon = State()
    check = State()

    
