from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.tillar import tillar
from keyboards.inline.menuKeyboard import Menu, Menyubot, Aboutmenu, KurslarMenu, kurslar1, xodimlarMenyu, Otajon,Rustamjon, Xusan, Xurshiyd, Otabek, Miraziz,sozlamalar_menu 
from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

@dp.callback_query_handler(text="Ozbek")
async def menu_handler(call: types.CallbackQuery):
    photo= "AgACAgIAAxkBAAID_Gcf33k3xYms1ERAUhR2nCmj6rwqAAJv5jEb5ZH4SKJVglbmBp8tAQADAgADeAADNgQ"
    habar = "<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot:</b>\n\n"
    habar += "Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin.\n"
    habar += "Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z portfolioingizni yaratishingiz mumkin."
    await call.message.delete()
    await call.message.answer_photo(photo=photo,caption=habar,reply_markup=Menu)

@dp.callback_query_handler(text="Menyu")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=Menyubot)
    
@dp.callback_query_handler(text="sozlamalar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIIq2cihfoZfZFPhc4ZHfCXN5WHDSEyAAKY5DEb1AMYSXzja0lSIr2NAQADAgADbQADNgQ"    # msg = f""" bu mani idm san ozinikini
    # Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    # """
    await call.message.answer_photo(photo=photo,reply_markup=sozlamalar_menu)

@dp.callback_query_handler(text="Tillar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIIqWcihJU_lo9QAn2xFWortx4L13uWAAKJ5DEb1AMYSfvK4rYdVlORAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=tillar)


@dp.callback_query_handler(text="About")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAICnWcedKguCdYuAX5zGpk3zYYje66wAAKS4TEbwzrwSNVd7BfcDAY8AQADAgADeAADNgQ"
    msg="<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot</b>:"
    msg+="Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin."
    msg+="Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim"
    msg+="olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z"
    msg+="portfolioingizni yaratishingiz mumkin."
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=Aboutmenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="About_ortga")
async def start(call:types.CallbackQuery):
    await call.message.delete()
    user ={call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAIIqWcihJU_lo9QAn2xFWortx4L13uWAAKJ5DEb1AMYSfvK4rYdVlORAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=Menyubot)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Kurslar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=KurslarMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Menyubot_ortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=Menyubot)


@dp.callback_query_handler(text="fronend")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vidyo = "BAACAgIAAxkBAAIC3mcefY7lUulcvgUN7042m9DJ_FTbAALeXAACwzrwSDhHFG3ATy_HNgQ"
    mes = "Dasturlash olamiga endi kirib kelgan insonda turli hil savollar paydo bo’lishni boshlaydi"
    msg = "Yangi olam, yangi qarashlar, yangi fikrlar. Bu albatta insonda savollar tug’ilishiga sababchi bo’lishi tabiiy. "
    msg = "Hali ham oz deb bo’lmaydi, lekin endi ularning aksariga o’zim javob topishni bilaman."
    await call.message.answer_video(video=vidyo, caption=msg, reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ortga2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICxGceeHqJdpw31-VugvSQC-CKMchvAALM4TEbwzrwSIbxf5ePqUmUAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=KurslarMenu)


@dp.callback_query_handler(text= "beckend")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vidyo = "BAACAgIAAxkBAAIDAAFnHoCHQtimgkIqmY_5CCbuInvkOQACclQAAsM6-Eg4ufmfHqp1ejYE"
    msg = "Backend (inglizcha back-end) - bu xizmatning dasturiy ta'minot va apparat qismidir"
    msg +="Bu veb-sayt mantig'i amalga oshiriladigan vositalar to'plami"
    msg +="Bu bizning ko'zimizdan yashiringan narsa, ya'ni kompyuter va brauzerdan tashqarida sodir bo'ladi"
    await call.message.answer_video(video=vidyo,caption=msg, reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text ="cyber") 
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vidyo = "BAACAgIAAxkBAAIDAmcegKSLwRKvuasjiREm9y1dz8XlAAJ0VAACwzr4SEUqX-EJFlM0NgQ" 
    msg ="Kiberxavfsizlik nima?\n"
    msg +=" Ba’zilarimiz bu atamani ilgari eshitganmiz,"
    msg +="lekin ba’zilarimiz bu nimani anglatishini yoki nima uchun bunday deb atalishini bilmasligimiz mumkin"
    msg +="Shunday qilib, kiberxavfsizlikning ma’nosini to’liq tushunish uchun keling, so’zni ikki qismga ajratamiz: “kiber” va “xavfsizlik”."
    await call.message.answer_video(video=vidyo, caption=msg , reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text= "garfika")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    vido= "BAACAgIAAxkBAAIDBGcegKtiRldUEPviFZnGIoM99DElAAJ1VAACwzr4SIq4tjXfdVJ1NgQ"
    msg ="Grafik dizayn — dizayn sohasining yoʻnalishlaridan biri boʻlib, maʼlum" 
    msg+="axborotni ijtimoiy guruhlarga yetkazish uchun vizual kontent yaratish,"
    msg+="ularni tartiblash, loyihalashga xizmat qiladi. Grafik dizaynning asosiy maqsadi muammolarni aniqlash"
    msg+="va ularni ijodkorlik bilan innovatsion va raqamli vositalar yordamida oʻzgartirish va toʻgʻri talqin qilishdan ibora"
    await call.message.answer_video(video=vido, caption=msg , reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ortga2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=kurslar1)

@dp.callback_query_handler(text="Hodimlar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)

@dp.callback_query_handler(text="xodimlarortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = "AgACAgIAAxkBAAICp2cedkA___htx6axUO2GMRfSFfrxAAKw4TEbwzrwSKWQjtCnDxOSAQADAgADeAADNgQ"
    await call.message.answer_photo(photo=photo, reply_markup=Menyubot)


@dp.callback_query_handler(text ="otajon")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAIDKmceii0Tx9umkwrHOKvwdkC7oe_kAAI94zEbwzr4SOoG2lq2khMiAQADAgADeAADNgQ"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Otajon Bozorboyev.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=Otajon)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Otajon")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)

@dp.callback_query_handler(text="Rustamjon")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo= "AgACAgIAAxkBAAIDLGceijXzkgqR0Nj2SXIzJ-jvPNs2AAI-4zEbwzr4SJkuEAx4eqynAQADAgADeAADNgQ"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Isroilov Rustamjo.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=Rustamjon)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Rustamjo")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)

@dp.callback_query_handler(text="Xusanjon")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAIEBGcf4TXqkHsduV55GqLq6SWh_wYLAAKF5jEb5ZH4SDhdEnxzmvbXAQADAgADeAADNgQ"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Xalilov Xusan.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=Xusan)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Xusan")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)


@dp.callback_query_handler(text="Otabekjon")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAIEAmcf4RA2h-Ub-9WQa_BnEheyyt9kAAKE5jEb5ZH4SEo3J__FPViXAQADAgADeAADNgQ"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Otabek.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=Otabek)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Otabek")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)

@dp.callback_query_handler(text="Xurshiydbek")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAIEAAFnH-DFamnVK-7Jc3yr0nzLgb3zLQACgeYxG-WR-EgK-h7HOu2q9wEAAwIAA3kAAzYE"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Xurshiyd.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=Xurshiyd)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Xurshiydi")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)


@dp.callback_query_handler(text="Mirazizjon")
async def men_handler(call:types.CallbackQuery):
    await call.message.delete()
    photo="AgACAgIAAxkBAAID_mcf4Hq2XFi0KirMlWL8iUI0CA9kAAJ-5jEb5ZH4SCDQXQr1uMK-AQADAgADeAADNgQ"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Miraziz.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    msg+= "Yapon tli (C2)"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=Miraziz)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Miraziz")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarMenyu)

