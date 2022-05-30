from config import bot
from telebot.types import Message
from utils import is_msg_from_admin

@bot.message_handler(commands=['start'])
def start(msg: Message):
    bot.send_message(msg.chat.id,'Welcome to bot!')


@bot.message_handler(commands=['help'])
def help(msg: Message):
    bot.send_message(msg.chat.id, "Your guide link.")

# Ban chat member
@bot.message_handler(commands=['kick'])
def ban_member(msg: Message):
    if is_msg_from_admin(msg.chat.id, msg.from_user.id,bot):
        bot.ban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)