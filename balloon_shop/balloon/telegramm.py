import telepot

token = '5664945248:AAFqfyYpB35FAre7SsTv2IymwiLxX6kHbgI'
my_id = 1518784837
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode='Markdown')
