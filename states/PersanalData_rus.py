from aiogram.dispatcher.filters.state import StatesGroup, State

class rus_PersonalData(StatesGroup):
    rus_qaysi_saxa = State()
    rus_fullnam = State()
    rus_email = State()
    rus_resume = State()
    rus_phoneNumber = State()
