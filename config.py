from telebot import TeleBot

BOT_TOKEN = ''
ADMIN_ID = ''
BOT_ID = BOT_TOKEN.split(':')[0]
PARSE_MODE = ''

bot = TeleBot(BOT_TOKEN,parse_mode=PARSE_MODE)