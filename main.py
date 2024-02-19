import telebot
TOKEN = '6319801047:AAHahLp6E0lT45vTkHNTyhBPadLE0iAmmn4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """welcome to my bot. 
                                    \n Type /help for a list of commands.""")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """how can I help you? 
                                    \n /start for start 
                                    \n /hello for say hi 
                                    \n now i can't do anything but we update it soon """)


@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, 'Hi!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
