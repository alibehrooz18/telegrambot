import telebot
# import json
import requests

TOKEN = '6652334606:AAHUOXC3eXLyOIen4Ml9w1lnqXvBN7CzvUI'
bot = telebot.TeleBot(TOKEN)
URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)


# send welcome message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """welcome to trade assistant bot
                                    \n it's demo version bot
                                    \n /help 
                                    \n /support
                                    \n Looking for what crypto ?
                                    \n /BTCUSDT
                                    \n /ETHUSDT 
                                    \n /TRXUSDT 
                                    \n /SOLUSDT """)


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


bot.infinity_polling()
