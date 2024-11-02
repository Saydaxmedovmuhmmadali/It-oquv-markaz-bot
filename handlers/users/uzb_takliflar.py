from aiogram import types
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from loader import dp
from states.uzbt_akliflar import uzb_PersonalData3
from keyboards.inline.menuKeyboard import Menyubot, shikoyat_menu
import re

@dp.callback_query_handler(text="shikoyat_takliflar")
async def enter_text(call: CallbackQuery):
    await call.answer(text='Comment')
    await call.message.answer("Taklif yoki shikoyatingizni kiriting:")
    await call.message.delete()
    await uzb_PersonalData3.uzb_fullname.set()

@dp.message_handler(state=uzb_PersonalData3.uzb_fullname)
async def answer_soha(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({'name': text})
    await message.answer("Telefon raqamingizni kiriting:")
    await uzb_PersonalData3.next()

@dp.message_handler(state=uzb_PersonalData3.uzb_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text
    if not re.match(r'^\+?[\d\s()-]{10,15}$', phone):  # Проверка формата номера
        await message.answer("Iltimos, to'g'ri telefon raqamini kiriting (masalan, +998123456789).")
        return

    await state.update_data({'telefon_nomer': phone})
    data = await state.get_data()
    fullname = data.get('name')
    phone = data.get('telefon_nomer')

    msg = f"""
    Quyidagi ma'lumotlar qabul qilindi.\n
    Tez orada operatorlarimiz bog'lanadi.\n\n\n
    <b>Taklif va shikoyat</b>: {fullname}\n
    <b>Telefon raqamingiz</b>: {phone}
    """

    await state.finish()
    await message.answer(msg, reply_markup=shikoyat_menu)

@dp.callback_query_handler(text="1shikoyatortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id: call.from_user.username}
    photo = "AgACAgIAAxkBAAII_GcjRVCL2_iowBsMDfNiHFs8yDtXAAK16TEb-wcZSf0l-2Z6ip_vAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=Menyubot)