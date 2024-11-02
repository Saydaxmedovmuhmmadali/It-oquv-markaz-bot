from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 



rus_Menu = InlineKeyboardMarkup(
    
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📝 Меню', callback_data="Меню"),
        ],
    ],row_width=True
)
rus_Menyubot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 информация", callback_data="информация"),
            InlineKeyboardButton(text="🎓 курсы", callback_data="курсы"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 сотрудники", callback_data="сотрудники"),
            InlineKeyboardButton(text="🧾 Вакансия", callback_data="Вакансия"),
        ],
       [
            InlineKeyboardButton(text="🛠 настройки", callback_data="настройки"),
            
        ],
    ],row_width=True
)

rus_Aboutmenu =InlineKeyboardMarkup(
    inline_keyboard=[
       [
            InlineKeyboardButton(text="▶️ видео", url="https://youtube.com/shorts/qsHai1S7wKg?si=GnAz1KR9ukhCDiNB"),
            InlineKeyboardButton(text="↩️ назад", callback_data="информация_назад"),
       ],
    ],row_width=True
)

rus_KurslarMenu= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖥 фронтен", callback_data="фронтен"),
            InlineKeyboardButton(text="⚙️ Бэкэнд", callback_data="Бэкэнд"),
        ],
        [
            InlineKeyboardButton(text="🛡 Кибербезопасностьy", callback_data="Кибербезопасность"),
            InlineKeyboardButton(text="🎨 Графика", callback_data="Графика"),
        ],
        [
            InlineKeyboardButton(text="↩️ назад", callback_data="Меню_назад"),
        ],
    ],row_width=True
)

rus_informatsiya =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="🔙 назад",callback_data="1назад"),
        ],
    ],
)

rus_anket1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 назад", callback_data="2назад"),
        ],
    ],
)

rus_kurslar1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍🏻 Запишитесь на курсы",callback_data="анкета"),
            InlineKeyboardButton(text="⬅️ назад",callback_data="назад2"),
        ],
    ],
)

rus_xodimlarMenyu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🦅 Отаджон Бозорбоев", callback_data="oтаджон"),
            InlineKeyboardButton(text="🧑‍💻 Исраилов Рустамжон", callback_data="Рустамжон"),
        ],
        [
            InlineKeyboardButton(text="🦉 Хусанжон", callback_data="Хусанжон"),
        ],
        [
            InlineKeyboardButton(text="👨🏻‍💻 Отабекжон", callback_data="Отабекжон"),
            InlineKeyboardButton(text="🧑‍💼 Хуршиджон", callback_data="Хуршиджон"),
        ],    
        [
            InlineKeyboardButton(text="Миразизжон",callback_data="Миразизжон"),
            InlineKeyboardButton(text="↩️ назад", callback_data="сотрудники_назад"),
        ],
    ],
)
rus_Otajon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ назадa", callback_data="Отаджон1"),
            InlineKeyboardButton(text="🔗 Связь", url="https://t.me/obozorboyev_bot"),
        ],
    ], row_width= True
)

rus_Rustamjon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ назадa", callback_data="Рустам"),
            InlineKeyboardButton(text="🔗 Связь", url="https://t.me/abruisbot"),
        ]
    ],row_width=True
)

rus_Xurshiyd =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ назадa", callback_data="Хуршид"),
            InlineKeyboardButton(text="🔗 Связь", url="https://t.me/nrx_xusan"),
        ],
    ],row_width=True
)

rus_Xusan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ назадa", callback_data="Хусан"),
            InlineKeyboardButton(text="🔗 Связь", url="https://t.me/nrx_xusan"),
        ],
    ],row_width=True
)

rus_Otabek = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ назадa", callback_data="Отабек"),
            InlineKeyboardButton(text="🔗 Связь", url="https://t.me/obozorboyev_bot"),
        ],
    ],row_width=True
)

rus_Miraziz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ назадa", callback_data="Миразиз"),
            InlineKeyboardButton(text="🔗 Link", url="https://t.me/obozorboyev_bot"),
        ],
    ],row_width=True
)

rus_sozlma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗣️ Языки", callback_data="Языки" ),
            InlineKeyboardButton(text="📣 вопросы_предложения", callback_data="вопросы_предложения"),
        ],
    ],row_width=True
)

rus_shikoyat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Ortga",callback_data="rus_shkoyat")
        ],
    ],
)
