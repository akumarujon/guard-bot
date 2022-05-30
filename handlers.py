from config import bot
from telebot.types import Message

@bot.message_handler(commands=['start'])
def start(msg: Message):
    bot.send_message(msg.chat.id,'Welcome to bot!')
