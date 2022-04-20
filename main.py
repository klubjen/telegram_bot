import telebot
bot = telebot.TeleBot('5311385773:AAG18f6YMOdR3pQQ3OcWDNqpvFlxZCklUvQ')

# Для обработки  команд

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет - это <b>Кубанский бот</b>, а ты, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, - лох. Напиши /list'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['list'])
def list(message):
    mess1 = f"Вот список доступных команд и слов:<b>\n /list\n /start\n photo\n Привет\n id</b>"
    bot.send_message(message.chat.id, mess1, parse_mode='html')

# Для обработки сообщений

@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == "привет":
         bot.send_message(message.chat.id, "Иди Нахуй!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID - гавно, смотри: {message.from_user.id} ", parse_mode='html')
    elif message.text == "photo":
        photo = open('IMG_4208.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "По человечески говори, урод!", parse_mode='html')



bot.polling(none_stop=True)