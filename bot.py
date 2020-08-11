# -*- coding: utf-8 -*-
import vars
import telebot as tb
from reply_def import reply_func, welcome

# Bot main
tBot = tb.TeleBot(vars.token)

# Bot commands
@tBot.message_handler(commands=['start', 'Start'])
def send_welcome(message):
    cid = str(message.chat.id)
    welcome(cid,message)

@tBot.message_handler(commands=['mytheme'])
def show_theme(message):
    cid = message.chat.id;
    tBot.send_message(cid, str(vars.cid_theme.get(cid)))

@tBot.message_handler(commands=['cnth'])
def change_theme(message):
    them = str(message.text).split()[-1]
    vars.cid_theme[message.chat.id]=them

@tBot.message_handler(commands=['break'])
def break_bot(message):
	if(str(message.chat.username) != vars.admin):
		vars.banlist.append(str(message.chat.id))
	else:
		raise MemoryError

# Form part
@tBot.message_handler(content_types="text")
def echo_text(message):
	reply_func(message)

# Bot end
tBot.polling()
