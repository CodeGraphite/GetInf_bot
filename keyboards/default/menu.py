from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

send_contact_btn = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton("Telefon raqamni jo'natish☎️", request_contact=True)
    ]
  ],
  resize_keyboard = True
)