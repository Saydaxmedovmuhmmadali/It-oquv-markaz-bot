from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.rus_taklflar import rus_PersonalData4
from keyboards.inline.menu_kebors_rus import rus_Menyubot, rus_shikoyat_menu
# from utils.notify_admins import 

@dp.callback_query_handler(text="вопросы_предложения")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Пишите предложения и жалобы!")
    await rus_PersonalData4.rus_fullname.set()

@dp.message_handler(state=rus_PersonalData4.rus_fullname)
async def answer_soha(message: Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {
            'name': text
        }
    )
    await message.answer("Отправьте свой номер телефона:")
    await rus_PersonalData4.rus_phoneNumber.set()

@dp.message_handler(state=rus_PersonalData4.rus_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon_nomer': phone
        }
    )
    
    data = await state.get_data()
    txt = data.get('name')
    phone = data.get('telefon_nomer')


    msg = f"""
        Была получена следующая информация.\n
        Наши операторы свяжутся с вами в ближайшее время.\n\n\n
        <b>Предложение и жалоба</b>: {txt}\n
        <b>Ваш номер телефона</b>: {phone}
    """
    # await comment(msg)
    
    await state.finish()
    # await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=rus_shikoyat_menu)

@dp.callback_query_handler(text="1_жалобе")
async def start(call: CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=rus_Menyubot)
    await call.answer(cache_time=60)