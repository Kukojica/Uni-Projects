import telebot
bot = telebot.TeleBot('6010925971:AAHRJpJJTIZyB-MtD90gUdQBHYHJuTMTepg')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMMZGqMcVDVV3xYjuawl7xXS3mcIS4AAq8AAwS9HhmFFm9jW5iI9y8E')

@bot.message_handler(commands=['start'])


bot.polling(none_stop=True)
