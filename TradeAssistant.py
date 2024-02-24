from TTOKEN import BOT_TOKEN
import telebot
# import json
import requests

TOKEN = BOT_TOKEN
bot = telebot.TeleBot(TOKEN)
URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)


# send welcome message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """welcome to crypto price bot
                                    \n it's demo version bot
                                    \n /support for knowing what crypto is supported
                                    \n /help 
                                    \n if you have crypto name enter:""")


# send help message
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, """/start for start bot 
                                    \n /support for knowing what crypto is supported
                                    \n if you have any adea for developer you can send to :
                                    \n "https://telegram.me/BChatBot?start=sc-1184589-2xwIyno" 
                                    \n """)


# send message for supported crypto
@bot.message_handler(commands=['support'])
def support(message):
    bot.reply_to(message, """for now we are supporting 
                                    \n /BTCUSDT 
                                    \n /ETHUSDT 
                                    \n /TRXUSDT 
                                    \n /SOLUSDT 
                                    \n is soon add more cryptocurrencies """)


@bot.message_handler(func=lambda m: True, commands=['BTCUSDT'])
def show_btc(message):
    symbol = message.text[1:]
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}', timeout=30)
    data = response.json()
    bot.reply_to(message, f"{data['symbol']} price is {data['price']}")

    print(response.status_code)


@bot.message_handler(func=lambda m: True, commands=['ETHUSDT'])
def show_eth(message):
    symbol = message.text[1:]
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}', timeout=30)
    data = response.json()
    bot.reply_to(message, f"{data['symbol']} price is {data['price']}")


@bot.message_handler(func=lambda m: True, commands=['TRXUSDT'])
def show_trx(message):
    symbol = message.text[1:]
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}', timeout=30)
    data = response.json()
    bot.reply_to(message, f"{data['symbol']} price is {data['price']}")


@bot.message_handler(func=lambda m: True, commands=['SOLUSDT'])
def show_sol(message):
    symbol = message.text[1:]
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}', timeout=30)
    data = response.json()
    bot.reply_to(message, f"{data['symbol']} price is {data['price']}")


@bot.message_handler(func=lambda m: True)
def search(message):
    symbol = message.text.upper()
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}', timeout=30)
    if response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f"{data['symbol']} price is {data['price']}")
    else:
        bot.reply_to(message, """your search not found
                                        \n enter full crypto name""")


bot.infinity_polling()
