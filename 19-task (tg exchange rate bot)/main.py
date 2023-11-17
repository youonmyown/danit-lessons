import requests
import telebot
from telebot import types

TOKEN = '5988101645:AAE7l2HF2lQTsVAHao-9B3C6tGrWZdCVQXY'
API_KEY = '6d029d98a51c67292040be262273e74a'
API_ENDPOINT = f'http://data.fixer.io/api/latest?access_key=6d029d98a51c67292040be262273e74a'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Hi! .Type /exchange to get the current exchange rate.')

@bot.message_handler(commands=['exchange'])
def handle_exchange(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_usd = types.KeyboardButton('USD')
    item_eur = types.KeyboardButton('EUR')
    item_gbp = types.KeyboardButton('GBP')
    markup.add(item_usd, item_eur, item_gbp)

    msg = bot.send_message(message.chat.id, 'Select currency:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_currency_choice)


def process_currency_choice(message):
    try:
        response = requests.get(API_ENDPOINT)
        data = response.json()

        chosen_currency = message.text.upper()
        if chosen_currency in data['rates']:
            rate_to_usd = data['rates'][chosen_currency]

            uah_to_usd = 1 / data['rates']['UAH']

            rate_to_uah = rate_to_usd / uah_to_usd

            bot.send_message(message.chat.id, f'{chosen_currency} to UAH rate: {rate_to_uah:.2f}')

            bot.register_next_step_handler(message, process_currency_choice)
        else:
            bot.send_message(message.chat.id, 'The selected currency is not supported.')

    except Exception as e:
        bot.send_message(message.chat.id, f'An error has occurred: {e}')


if __name__ == '__main__':
    bot.polling(none_stop=True)