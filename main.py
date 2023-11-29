import telebot
from telebot import types

bot = telebot.TeleBot("6951892342:AAHNgZLKJ9iV_B2z1SAK-No48wT4vNnd3oI")

@bot.message_handler(commands=["start"])
def start_message(message):  # исправляем название функции
    bot.send_message(message.chat.id, "Привет! Это Nkali.")

@bot.message_handler(commands=['button'])
def button_message(message):  # также исправляем название функции
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Привет! Поможешь составить маршрут?")
    markup.add(item1)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)  # исправляем на использование обработчика для любого сообщения
def handle_message(message):
    if message.text == "Привет! Поможешь составить маршрут?":  # исправляем условие
        bot.send_message(message.chat.id, "Конечно) Сейчас.")
    else:
        bot.send_message(message.chat.id, "Я не понимаю, о чем вы.")

bot.polling(none_stop=True)  # исправляем на использование метода polling