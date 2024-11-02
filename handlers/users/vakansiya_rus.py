import logging

from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
# from utils.notify_admins import 


from loader import dp
from states.PersanalData_rus import rus_PersonalData
from keyboards.inline.menu_kebors_rus import rus_Menyubot, rus_informatsiya  

@dp.callback_query_handler(text="Вакансия")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("В каком направлении вы хотите работать:")
    await rus_PersonalData.rus_qaysi_saxa.set()

@dp.message_handler(state=rus_PersonalData.rus_qaysi_saxa)
async def answer_fullname(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'поле выбрано': soha
        }
    )
    await message.answer("Введите свое полное имя:")
    await rus_PersonalData.rus_fullnam.set()

@dp.message_handler(state=rus_PersonalData.rus_fullnam)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'F.I.O': fullname
        }
    )
    await state.set_state(rus_PersonalData.rus_resume)
    await message.answer("Отправьте свое резюме:")
    # await rus_PersonalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=rus_PersonalData.rus_resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            'resume': resume.file_id
        }
    )
    await message.answer('Введите свой номер телефона')
    await rus_PersonalData.next()

@dp.message_handler(state=rus_PersonalData.rus_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

   
    await state.update_data(
        {
            'номер телефона': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('поле выбрано')
    fullname = data.get('F.I.O')
    resume = data.get('резюме')
    phone = data.get('номер телефона')

    msg = (
    "Следующая информация принята.\n"
    "Наши операторы свяжутся с вами в ближайшее время.\n\n\n"
    f"<b>Ваш отправленный адрес</b>: {soha}\n"
    f"<b>имя фамилия</b>: {fullname}\n"
    f"<b>Ваше резюме</b>: {resume}\n"
    f"<b>Ваш номер телефона</b>: {phone}"
    )

    
    await state.finish()
    await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=rus_informatsiya)

@dp.callback_query_handler(text="1назад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=rus_Menyubot)

