import telepot
from .token_and_ID import *

token = token_telegram
my_id = my_id_telegram
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode='Markdown')
