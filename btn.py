from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_menu = ReplyKeyboardMarkup(resize_keyboard=True)
btn_menu.add(KeyboardButton('Boshlash'))
btn_bekor = ReplyKeyboardMarkup(resize_keyboard=True)
btn_bekor.add(KeyboardButton("Bekor qilish"))