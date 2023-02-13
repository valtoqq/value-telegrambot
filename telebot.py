import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6211181694:AAGXX1N6wqtpK7hwrcI0VLBsyS6IgJExD9E')

dictvalue={'BTC': 'bitcoin', 'BNB': 'binancecoin', 'USDC': 'usd-coin', 'ETH': 'ethereum', 'USDT': 'tether', 'XRP': 'ripple', 'BUSD': 'binance-usd'}

def valueexchange():
    cryptocourse = ['bitcoin', 'ethereum', 'tether', 'binancecoin', 'usd-coin', 'binance-usd', 'ripple']
    r = {}
    for c in cryptocourse:
        r[c] = '$' + str(requests.get(f'https://api.coingecko.com/api/v3/coins/{c}/tickers').json()['tickers'][0]['last'])

    return r

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}, этот бот показывает актуальный курс валют'
    bot.send_message(message.chat.id, mess)
    markup = types.ReplyKeyboardAAMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Валюты")
    b = types.KeyboardButton("Помощь")
    markup.add(a, b)
    bot.send_message(message.chat.id, "Выберите интересующий раздел", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def button2(message):
    if message.text == "Валюты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttonvalue1 = types.KeyboardButton("BTC")
        buttonvalue2 = types.KeyboardButton("ETH")
        buttonvalue3 = types.KeyboardButton("USDT")
        buttonvalue4 = types.KeyboardButton("BNB")
        buttonvalue5 = types.KeyboardButton("USDC")
        buttonvalue6 = types.KeyboardButton("XRP")
        buttonvalue7 = types.KeyboardButton("BUSD")
        backmenu = types.KeyboardButton("Вернуться в меню")
        markup.add(buttonvalue1, buttonvalue2, buttonvalue3, buttonvalue4, buttonvalue5, buttonvalue6, buttonvalue7, backmenu)
        bot.send_message(message.chat.id, "Валюты", reply_markup=markup)

    elif message.text == "Помощь":
        bot.send_message(message.chat.id, "При возникновении вопросов/предложений/жалоб напишите создателю бота @valtoq")

    elif message.text == "Вернуться в меню":
        bot.send_message(message.chat.id, "Вы вернулись в меню")
        start(message)

    elif message.text in ('BTC', 'BNB', 'USDC', 'ETH', 'USDT', 'XRP', 'BUSD'):
        n = message.text
        r = valueexchange() [dictvalue[n]]
        bot.send_message(message.chat.id, r)

bot.polling(none_stop=True)
