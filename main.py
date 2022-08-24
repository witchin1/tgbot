import telebot
import config

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help']) #декоратор, функция, которая внутри библиотеки
def say_hi(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def my_destiny(message):
	bot.reply_to(message, message.text)



bot.infinity_polling()