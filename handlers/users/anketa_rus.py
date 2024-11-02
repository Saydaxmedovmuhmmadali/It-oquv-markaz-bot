from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.PersanlData2_rus import PersanlData2_rus
from keyboards.inline.menu_kebors_rus import rus_anket1, rus_kurslar1, rus_KurslarMenu

@dp.callback_query_handler(text="анкета")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Введите свое полное имя")
    await PersanlData2_rus.fullname.set()

@dp.message_handler(state= PersanlData2_rus.fullname)
async def answer_soha(message: Message, state: FSMContext):

    fullname = message.text
    await state.update_data(
        {
            'name': fullname
        }
    )
    await message.answer("Введите свой номер телефона:")
    await PersanlData2_rus.next()

@dp.message_handler(state=PersanlData2_rus.phone)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text
    print("phone")
    await state.update_data(
        {
            'номер телефона': phone
        }
    )
    
    data = await state.get_data()
    fullname = data.get('name')
    phone = data.get('номер телефона')

    msg = f"""
        Была получена следующая информация.\n
        Наши операторы скоро свяжутся с вами.\n\n\n
        <b>имя фамилия</b>: {fullname}\n
        <b>Ваш номер телефона</b>: {phone}
    """

    

    await message.answer(msg, reply_markup=rus_anket1)
    await state.finish()

@dp.callback_query_handler(text="2назад")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo = photo, reply_markup=rus_KurslarMenu)

