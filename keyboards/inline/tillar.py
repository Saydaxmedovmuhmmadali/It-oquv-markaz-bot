from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

tillar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text="🇺🇿 Ozbek",callback_data="Ozbek"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="Русский_язык"),
        ],
    ], row_width=True
)