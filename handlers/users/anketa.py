
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.Persanal_data2 import Persanl_data2
from keyboards.inline.menuKeyboard import  kurslar1, anket1

@dp.callback_query_handler(text="anketa")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("To'liq ismingizni kiriting")
    await Persanl_data2.fullname.set()

@dp.message_handler(state=Persanl_data2.fullname)
async def answer_soha(message: Message, state: FSMContext):

    fullname = message.text
    await state.update_data(
        {
            'name': fullname
        }
    )
    await message.answer("Telefon raqamingizni kiriting:")
    await Persanl_data2.next()

@dp.message_handler(state=Persanl_data2.phone)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon_nomer': phone
        }
    )
    
    data = await state.get_data()
    fullname = data.get('name')
    phone = data.get('telefon_nomer')

    msg = f"""
        Quyidagi ma'lumotlar qabul qilindi.\n
        Tez orada operatorlarimiz bog'lanadi.\n\n\n
        <b>ism familiya sharifi</b>: {fullname}\n
        <b>Telefon raqamingiz</b>: {phone}
    """

    

    await state.finish()
    await message.answer(msg, reply_markup=anket1)

@dp.callback_query_handler(text="2ortga")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo = photo, reply_markup=kurslar1)

