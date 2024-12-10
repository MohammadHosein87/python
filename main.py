import telebot

bot = telebot.TeleBot("6576658767:AAEkQ9gxcSAUV46eIPGT9xnlgkYmbVtZAGU")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "خوش آمدید")
    bot.send_photo(message.chat.id, open("C:/Users/User/Desktop/Ehteram/کارآفرینی/02-human-resource.jpg", 'rb'))


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "what can i do?", reply_markup=key_board)


key_board = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_board.add("Test", "Test2")


@bot.message_handler()
def keyboard(message):
    if message.text == "چه خبر؟":
        bot.send_message(message.chat.id, "سلامتی، داشمی")
    elif message.text == "Test2":
        bot.send_message(message.chat.id, "you")
    elif message.text == "سلام":
        bot.send_message(message.chat.id, "سلام خوبی؟")


bot.infinity_polling()
