# -*- coding: utf-8 -*-
import vars
import markup
import telebot as tb

# Bot main
tBot = tb.TeleBot(vars.token)

# Bot commands

@tBot.message_handler(commands=['start', 'Start', 'help', 'Help'])
def send_welcome(message):
    cid = str(message.chat.id)
    tBot.send_message(cid, "Hello, I am " + vars.name + ". I can copy you. Have a nice day!😄", reply_markup=markup.reg)
    if cid not in vars.chat_ids:
        sti = open('hi.webp', 'rb')
        tBot.send_sticker(cid, sti)
        vars.chat_ids.append(cid)
        print("New user:",message.chat.first_name, message.chat.last_name, '(' + str(message.chat.id) + ')')

@tBot.message_handler(commands=['easter_egg'])
def easter_egg(message):
    sti = open('easter.webp', 'rb')
    tBot.send_message(message.chat.id, "You have found an easter egg")
    tBot.send_sticker(message.chat.id, sti)

# TODO add more commands
for i in range(1,30):
    tBot.send_message("595370804", "Suka_blyat")


# Echo part
@tBot.message_handler(content_types=['sticker'])
def echo_stick(message):
	print(message.chat.first_name, message.chat.last_name, '(' + str(message.chat.id) + ')', 'sent a sticker')
	tBot.send_sticker(message.chat.id, message.sticker.file_id)

@tBot.message_handler(content_types=['photo'])
def echo_photo(message):
	print(message.chat.first_name, message.chat.last_name, '(' + str(message.chat.id) + ')', 'sent a photo')
	tBot.send_photo(message.chat.id,message.photo[0].file_id)

@tBot.message_handler(content_types=['audio'])
def echo_audio(message):
	print(message.chat.first_name, message.chat.last_name, '(' + str(message.chat.id) + ')', 'sent an audio')
	tBot.send_audio(message.chat.id, message.audio.file_id)

@tBot.message_handler()
def echo_text(message):
	print(message.chat.first_name, message.chat.last_name, '(' + str(message.chat.id) + ')', '->', message.text)
	tBot.send_message(message.chat.id, message.text)

# Bot end
tBot.polling()
