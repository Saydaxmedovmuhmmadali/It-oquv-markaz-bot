import logging

from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
# from utils.notify_admins import 


from loader import dp
from states.Persanl_data1 import uzb_PersonalData
from keyboards.inline.menuKeyboard import  Menyubot, informatsiya

@dp.callback_query_handler(text="Vaknsiya")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi yo'nalish bo'yicha ishlamoqchisiz:")
    await uzb_PersonalData.uzb_qaysi_soxaga.set()

@dp.message_handler(state=uzb_PersonalData.uzb_qaysi_soxaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'soha tanlandi': soha
        }
    )
    await message.answer("To'liq ism sharifingizni kiriting:")
    await uzb_PersonalData.uzb_fullname.set()

@dp.message_handler(state=uzb_PersonalData.uzb_fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'F.I.O': fullname
        }
    )
    await state.set_state(uzb_PersonalData.uzb_resume)
    await message.answer("Rezyumeni yuboring:")
    # await uzb_PersonalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=uzb_PersonalData.uzb_resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data({"resume":resume.file_id})
    await message.answer("Telefon raqamingizni yuboring:")
    await uzb_PersonalData.next()

@dp.message_handler(state=uzb_PersonalData.uzb_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon nomer': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('soha tanlandi')
    fullname = data.get('F.I.O')
    resume = data.get('resume')
    phone = data.get('telefon nomer')




    msg = (
        "Quyidagi ma'lumotlar qabul qilindi.\n"
        "Tez orada operatorlarimiz bog'lanadi.\n\n\n"
        f"<b>Topshirgan yo'nalshingiz</b>: {soha}\n"
        f"<b>ism familiya sharifi</b>: {fullname}\n"
        f"<b>Rezyumengiz</b>: {resume}\n"
        f"<b>Telefon raqamingiz</b>: {phone}"
    )

    
    # await comment(msg)

    
    await state.finish()
    # await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=informatsiya)

@dp.callback_query_handler(text="1ortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo ="AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=Menyubot)
