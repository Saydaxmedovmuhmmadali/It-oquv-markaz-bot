from aiogram import types
from keyboards.inline.tillar import tillar
from keyboards.inline.menu_kebors_rus import rus_Menu, rus_Menyubot, rus_Aboutmenu, rus_KurslarMenu, rus_informatsiya, rus_anket1, rus_kurslar1, rus_xodimlarMenyu, rus_Otajon, rus_Rustamjon, rus_Xurshiyd,rus_Xusan, rus_Otabek, rus_Miraziz, rus_sozlma, rus_shikoyat_menu
from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

@dp.callback_query_handler(text="Русский_язык")
async def menu_handler(call: types.CallbackQuery):
    photo= "AgACAgIAAxkBAAID_Gcf33k3xYms1ERAUhR2nCmj6rwqAAJv5jEb5ZH4SKJVglbmBp8tAQADAgADeAADNgQ"
    habar = "<b>Краткая информация Трамплинг IT Академии краткая информация:</b>\n\n"
    habar += "В Трамплинг IT Academy вы можете изучать программирование у профессионалов..\n"
    habar += "В ходе курса вы получите качественное образование по специальной методике от высококвалифицированных программистов."
    habar+= "и вы сможете создать собственное портфолио на основе более чем 50 проектов на практике."
    await call.message.delete()
    await call.message.answer_photo(photo=photo,caption=habar,reply_markup=rus_Menu)



@dp.callback_query_handler(text="Меню")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIIq2cihfoZfZFPhc4ZHfCXN5WHDSEyAAKY5DEb1AMYSXzja0lSIr2NAQADAgADbQADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=rus_Menyubot)
    
    # msg = f"""
    # Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    # """
    
@dp.callback_query_handler(text="настройки")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIIq2cihfoZfZFPhc4ZHfCXN5WHDSEyAAKY5DEb1AMYSXzja0lSIr2NAQADAgADbQADNgQ"    # msg = f""" bu mani idm san ozinikini
    # Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    # """
    await call.message.answer_photo(photo=photo,reply_markup=rus_sozlma)

  
@dp.callback_query_handler(text="Языки")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIIqWcihJU_lo9QAn2xFWortx4L13uWAAKJ5DEb1AMYSfvK4rYdVlORAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=tillar)

@dp.callback_query_handler(text="Меню")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=rus_Menyubot)
    

@dp.callback_query_handler(text="информация")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAICnWcedKguCdYuAX5zGpk3zYYje66wAAKS4TEbwzrwSNVd7BfcDAY8AQADAgADeAADNgQ"
    msg="<b>Краткая информация об IT Академии Трамплинг:"
    msg= "ВТрамплинг IT Academy вы можете изучать программирование у профессионалов."
    msg+="В ходе курса качественное обучение от высококвалифицированных программистов по специальной методике"
    msg+="примените полученные знания на практике на основе более 50 проектов"
    msg+="вы можете создать свое портфолио."
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Aboutmenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="информация_назад")
async def start(call:types.CallbackQuery):
    await call.message.delete()
    user ={call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=rus_Menyubot)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="курсы")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=rus_KurslarMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Меню_назад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=rus_Menyubot)


@dp.callback_query_handler(text="фронтен")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vidyo = "BAACAgIAAxkBAAIC3mcefY7lUulcvgUN7042m9DJ_FTbAALeXAACwzrwSDhHFG3ATy_HNgQ"
    msg = "У человека, только что вошедшего в мир программирования, начинают возникать различные вопросы"
    msg+="Новый мир, новые взгляды, новые мысли. Естественно, что это вызывает у человека возникновение вопросов."
    msg+= "Все еще немало, но теперь я знаю, как найти ответы на большинство из них самостоятельно."
    await call.message.answer_video(video=vidyo, caption=msg, reply_markup=rus_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="назад2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=rus_KurslarMenu)


@dp.callback_query_handler(text="Бэкэнд")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vidyo = "BAACAgIAAxkBAAIDAAFnHoCHQtimgkIqmY_5CCbuInvkOQACclQAAsM6-Eg4ufmfHqp1ejYE"
    msg = "Бэкенд (англ. back-end) — программная и аппаратная часть сервиса"
    msg +="Это набор инструментов, реализующий логику веб-сайта"
    msg +="Это то, что скрыто от наших глаз, то есть происходит вне компьютера и браузера"

    await call.message.answer_video(video=vidyo,caption=msg, reply_markup=rus_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Кибербезопасность") 
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vidyo = "BAACAgIAAxkBAAIDAmcegKSLwRKvuasjiREm9y1dz8XlAAJ0VAACwzr4SEUqX-EJFlM0NgQ" 
    msg ="Что такое кибербезопасность?\n"
    msg +="Некоторые из нас слышали этот термин раньше,"
    msg +="но некоторые из нас могут не знать, что это значит и почему это так называется"
    msg +="Итак, чтобы полностью понять значение кибербезопасности, давайте разделим это слово на две части: «кибер» и «безопасность."
    await call.message.answer_video(video=vidyo, caption=msg , reply_markup=rus_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Графика")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vido= "BAACAgIAAxkBAAIDBGcegKtiRldUEPviFZnGIoM99DElAAJ1VAACwzr4SIq4tjXfdVJ1NgQ"
    msg ="Графический дизайн – одно из направлений дизайнерской сферы, известное как"
    msg+="создание визуального контента для доставки информации в социальные группы,"
    msg+="служит для их организации и оформления. Основная цель графического дизайна — выявление проблем"
    msg+="и фраза о их творческом преобразовании и интерпретации с использованием инновационных цифровых инструментов"
    await call.message.answer_video(video=vido, caption=msg , reply_markup=rus_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="назад2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=rus_Menyubot)


@dp.callback_query_handler(text="сотрудники")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Сотрудники👇</b>", reply_markup=rus_xodimlarMenyu)

@dp.callback_query_handler(text="сотрудники_назад")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=rus_Menyubot)
 
@dp.callback_query_handler(text ="oтаджон")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAIDKmceii0Tx9umkwrHOKvwdkC7oe_kAAI94zEbwzr4SOoG2lq2khMiAQADAgADeAADNgQ"
    msg = "<b>Имя очствс:</b>\n"
    msg += "Отаджон Бозорбое.\n\n"   
    msg += "<b>год и место рождения</b>:" 
    msg+= "8 января 1999 "
    msg +="Джизакская область, г. Джизак"
    msg +="Образование Ташкентский профессиональный колледж железнодорожного транспорта Учет и аудит (2015-2018)"
    msg+="Опыт работы"
    msg+="Стажер отдела кадров Джизакской железной дороги (2018-2019)"
    msg+=" Начальник отдела кадров Джизакской железной дороги (2019-2023 гг.)"
    msg+="Наставник курсов программирования в Учебном центре Astro Education"
    msg+="(с 2023 г. по настоящее время) Технические навыки Python, Django, "
    msg+="Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot,"
    msg+="Adobe Photoshop, парсинг веб-страниц, синтаксический анализ, Microsoft Office (Word) , Excel, Power Point, Paint и т. д.)"
    msg+="Языки"
    msg+="Узбекский язык (родной язык)"
    msg += "Английский (B2)"
    msg+="Арабский (Чтение)"
    msg+="Японский (С2)"
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Otajon)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Отаджон1")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=rus_xodimlarMenyu)

@dp.callback_query_handler(text="Рустамжон")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAIDLGceijXzkgqR0Nj2SXIzJ-jvPNs2AAI-4zEbwzr4SJkuEAx4eqynAQADAgADeAADNgQ"
    msg = "<b>Имя очствс: </b>\n"
    msg += "Отаджон Бозорбое .\n\n"   
    msg += "<b>год и место рождения</b>:" 
    msg+= "8 января 1999 "
    msg +="Джизакская область, г. Джизак"
    msg +="Образование Ташкентский профессиональный колледж железнодорожного транспорта Учет и аудит (2015-2018)"
    msg+="Опыт работы"
    msg+="Стажер отдела кадров Джизакской железной дороги (2018-2019)"
    msg+=" Начальник отдела кадров Джизакской железной дороги (2019-2023 гг.)"
    msg+="Наставник курсов программирования в Учебном центре Astro Education"
    msg+="(с 2023 г. по настоящее время) Технические навыки Python, Django, "
    msg+="Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot,"
    msg+="Adobe Photoshop, парсинг веб-страниц, синтаксический анализ, Microsoft Office (Word) , Excel, Power Point, Paint и т. д.)"
    msg+="Языки"
    msg+="Узбекский язык (родной язык)"
    msg += "Английский (B2)"
    msg+="Арабский (Чтение)"
    msg+="Японский (С2)"
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Rustamjon)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Рустам")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=rus_xodimlarMenyu)

@dp.callback_query_handler(text="Хусанжон")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAIEAmcf4RA2h-Ub-9WQa_BnEheyyt9kAAKE5jEb5ZH4SEo3J__FPViXAQADAgADeAADNgQ"
    msg = "<b>Имя очствс: </b>\n"
    msg += "Отаджон Бозорбое   .\n\n"   
    msg += "<b>год и место рождения</b>:" 
    msg+= "8 января 1999 "
    msg +="Джизакская область, г. Джизак"
    msg +="Образование Ташкентский профессиональный колледж железнодорожного транспорта Учет и аудит (2015-2018)"
    msg+="Опыт работы"
    msg+="Стажер отдела кадров Джизакской железной дороги (2018-2019)"
    msg+=" Начальник отдела кадров Джизакской железной дороги (2019-2023 гг.)"
    msg+="Наставник курсов программирования в Учебном центре Astro Education"
    msg+="(с 2023 г. по настоящее время) Технические навыки Python, Django, "
    msg+="Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot,"
    msg+="Adobe Photoshop, парсинг веб-страниц, синтаксический анализ, Microsoft Office (Word) , Excel, Power Point, Paint и т. д.)"
    msg+="Языки"
    msg+="Узбекский язык (родной язык)"
    msg += "Английский (B2)"
    msg+="Арабский (Чтение)"
    msg+="Японский (С2)"
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Xusan)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Хусан")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=rus_xodimlarMenyu)

@dp.callback_query_handler(text="Отабекжон")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAIEAAFnH-DFamnVK-7Jc3yr0nzLgb3zLQACgeYxG-WR-EgK-h7HOu2q9wEAAwIAA3kAAzYE"
    msg = "<b>Имя очствс: </b>\n"
    msg += "Отаджон Бозорбое.\n\n"   
    msg += "<b>год и место рождения:</b>" 
    msg+= "8 января 1999 "
    msg +="Джизакская область, г. Джизак"
    msg +="Образование Ташкентский профессиональный колледж железнодорожного транспорта Учет и аудит (2015-2018)"
    msg+="Опыт работы"
    msg+="Стажер отдела кадров Джизакской железной дороги (2018-2019)"
    msg+=" Начальник отдела кадров Джизакской железной дороги (2019-2023 гг.)"
    msg+="Наставник курсов программирования в Учебном центре Astro Education"
    msg+="(с 2023 г. по настоящее время) Технические навыки Python, Django, "
    msg+="Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot,"
    msg+="Adobe Photoshop, парсинг веб-страниц, синтаксический анализ, Microsoft Office (Word) , Excel, Power Point, Paint и т. д.)"
    msg+="Языки"
    msg+="Узбекский язык (родной язык)"
    msg += "Английский (B2)"
    msg+="Арабский (Чтение)"
    msg+="Японский (С2)"
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Xurshiyd)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Отабек")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=rus_xodimlarMenyu)

@dp.callback_query_handler(text="Хуршиджон")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAIEAAFnH-DFamnVK-7Jc3yr0nzLgb3zLQACgeYxG-WR-EgK-h7HOu2q9wEAAwIAA3kAAzYE"
    msg = "<b>Имя очствс: </b>\n"
    msg += "Отаджон Бозорбое.\n\n"   
    msg += "<b>год и место рождения:</b>" 
    msg+= "8 января 1999 "
    msg +="Джизакская область, г. Джизак"
    msg +="Образование Ташкентский профессиональный колледж железнодорожного транспорта Учет и аудит (2015-2018)"
    msg+="Опыт работы"
    msg+="Стажер отдела кадров Джизакской железной дороги (2018-2019)"
    msg+=" Начальник отдела кадров Джизакской железной дороги (2019-2023 гг.)"
    msg+="Наставник курсов программирования в Учебном центре Astro Education"
    msg+="(с 2023 г. по настоящее время) Технические навыки Python, Django, "
    msg+="Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot,"
    msg+="Adobe Photoshop, парсинг веб-страниц, синтаксический анализ, Microsoft Office (Word) , Excel, Power Point, Paint и т. д.)"
    msg+="Языки"
    msg+="Узбекский язык (родной язык)"
    msg += "Английский (B2)"
    msg+="Арабский (Чтение)"
    msg+="Японский (С2)"
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Xurshiyd)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Хуршид")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=rus_xodimlarMenyu)


@dp.callback_query_handler(text="Миразизжон")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAID_mcf4Hq2XFi0KirMlWL8iUI0CA9kAAJ-5jEb5ZH4SCDQXQr1uMK-AQADAgADeAADNgQ"
    msg = "<b>Имя очствс: </b>\n"
    msg += "Отаджон Бозорбое   .\n\n"   
    msg += "<b>год и место рождения</b>:" 
    msg+= "8 января 1999 "
    msg +="Джизакская область, г. Джизак"
    msg +="Образование Ташкентский профессиональный колледж железнодорожного транспорта Учет и аудит (2015-2018)"
    msg+="Опыт работы"
    msg+="Стажер отдела кадров Джизакской железной дороги (2018-2019)"
    msg+=" Начальник отдела кадров Джизакской железной дороги (2019-2023 гг.)"
    msg+="Наставник курсов программирования в Учебном центре Astro Education"
    msg+="(с 2023 г. по настоящее время) Технические навыки Python, Django, "
    msg+="Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot,"
    msg+="Adobe Photoshop, парсинг веб-страниц, синтаксический анализ, Microsoft Office (Word) , Excel, Power Point, Paint и т. д.)"
    msg+="Языки"
    msg+="Узбекский язык (родной язык)"
    msg += "Английский (B2)"
    msg+="Арабский (Чтение)"
    msg+="Японский (С2)"
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=rus_Miraziz)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Миразиз")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=rus_xodimlarMenyu)