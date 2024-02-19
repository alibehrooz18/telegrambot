import telebot
TOKEN = '6652334606:AAHUOXC3eXLyOIen4Ml9w1lnqXvBN7CzvUI'
bot = telebot.TeleBot(TOKEN)
# URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """welcome to trade assistant bot
                                    \n it's demo version bot
                                    \n /help 
                                    \n /support
                                    \n Looking for what crypto ?
                                    \n /BTC 
                                    \n /ETH 
                                    \n /TRX 
                                    \n /SOL """)

# send start message


# send help message
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """/start for start bot 
                                    \n /support for knowing what crypto is supported   
                                    \n for... """)


# send message for supported crypto
@bot.message_handler(commands=['support'])
def send_support(message):
    bot.reply_to(message, """for now we are supporting 
                                    \n /BTC 
                                    \n /ETH 
                                    \n /TRX 
                                    \n /SOL 
                                    \n is soon adding more cryptocurrencies """)


@bot.message_handler(commands=['BTC'])
def send_help(message):
    bot.reply_to(message,f"BTC price is : {BTC} for now")

@bot.message_handler(commands=['ETH'])
def send_help(message):
    bot.reply_to(message, f"ETH price is : {ETH} for now")


@bot.message_handler(commands=['TRX'])
def send_help(message):
    bot.reply_to(message, f"TRX price is : {TRX} for now")


@bot.message_handler(commands=['SOL'])
def send_help(message):
    bot.reply_to(message, f"SOL price is : {SOL} for now")


bot.infinity_polling()