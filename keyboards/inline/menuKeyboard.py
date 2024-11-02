from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

 

Menu = InlineKeyboardMarkup(
    
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📝Menyu', callback_data="Menyu"),
        ],
    ],row_width=True
)   
Menyubot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 About", callback_data="About"),
            InlineKeyboardButton(text="🎓 Kurslar", callback_data="Kurslar"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Xodimlar", callback_data="Hodimlar"),
            InlineKeyboardButton(text="🧾 Vakansiya", callback_data="Vaknsiya"),
        ],
        [
            InlineKeyboardButton(text="🛠 Sozlamalar", callback_data="sozlamalar"),
            
        ],
    ],row_width=True
)

Aboutmenu =InlineKeyboardMarkup(
    inline_keyboard=[
       [
            InlineKeyboardButton(text= "▶️ Vidyo", url="https://youtube.com/shorts/qsHai1S7wKg?si=GnAz1KR9ukhCDiNB"),
            InlineKeyboardButton(text="↩️ Ortka", callback_data="About_ortga"),
       ],
    ],row_width=True
)

KurslarMenu= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖥 Front-end", callback_data="fronend"),
            InlineKeyboardButton(text="⚙️ Beckend", callback_data="beckend"),
        ],
        [
            InlineKeyboardButton(text="🛡 Cyber Security", callback_data="cyber"),
            InlineKeyboardButton(text="🎨Graphic", callback_data="garfika"),
        ],
        [
            InlineKeyboardButton(text="↩️ ortga", callback_data="Menyubot_ortga"),
        ],
    ],row_width=True
)

informatsiya =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="🔙 ortga",callback_data="1ortga"),
        ],
    ],
)

anket1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙ortga", callback_data="2ortga"),
        ],
    ],
)

kurslar1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍🏻 Kurslarga yozilish",callback_data="anketa"),
            InlineKeyboardButton(text="⬅️ortga",callback_data="ortga2"),
        ],
    ],
)

xodimlarMenyu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🦅Otajon Bozorboyev", callback_data="otajon"),
            InlineKeyboardButton(text="🧑‍💻Isroilov Rustamjon", callback_data="Rustamjon"),
        ],
        [
            InlineKeyboardButton(text="🦉Xalilov Xusan", callback_data="Xusan"),
        ],
        [
            InlineKeyboardButton(text="👨🏻‍💻Otabek", callback_data="Otabek"),
            InlineKeyboardButton(text="🧑‍💼Xurshiyd", callback_data="Xurshiyd"),
        ],    
        [
            InlineKeyboardButton(text="Miraziz",callback_data="Miraziz")
          
        ],
        [
            InlineKeyboardButton(text="↩️ortga", callback_data="xodimlarortga"),
        ]
    ],
)
Otajon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" ↩️ortga", callback_data="Otajon"),
            InlineKeyboardButton(text="🔗Link", url="https://t.me/obozorboyev_bot"),
        ],
    ], row_width= True
)

Rustamjon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ ortga", callback_data="Rustamjo"),
            InlineKeyboardButton(text="🔗Link", url="https://t.me/abruisbot"),
        ]
    ],row_width=True
)

Xurshiyd =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ ortga", callback_data="Xurshiydi"),
            InlineKeyboardButton(text="🔗Link", url=""),
        ],
    ],row_width=True
)

Xusan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ ortga", callback_data="Xusan"),
            InlineKeyboardButton(text="🔗Link", url="https://t.me/nrx_xusan"),
        ],
    ],row_width=True
)

Otabek = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ ortga", callback_data="Otabek"),
            InlineKeyboardButton(text="🔗Link", url="https://t.me/obozorboyev_bot"),
        ],
    ],row_width=True
)

Miraziz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ ortga", callback_data="Miraziz"),
            InlineKeyboardButton(text="🔗Link", url="https://t.me/obozorboyev_bot"),
        ],
    ],row_width=True
)

sozlamalar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗣️ Tillar", callback_data="Tillar" ),
            InlineKeyboardButton(text="Shikoyat yoki Takliflar", callback_data="shikoyat_takliflar")
            # InlineKeyboardButton(text="📣 Shikoyat_va_takliflar", callback_data="shikoyat_takliflar"),
        ],
    ],row_width=True
)

shikoyat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Ortga",callback_data="1shikoyatortga")
        ],
    ],
)
