from aiogram.dispatcher.filters.state import StatesGroup, State

class uzb_PersonalData3(StatesGroup):
    uzb_fullname = State()
    uzb_phoneNumber = State()