import vars
import markup
import telebot as tb
############################################################
import mech                                             ####
import eles                                             ####
import bugs                                             ####
import ther                                             ####
############################################################
from logger import Logger
from main_func import logout, opn, back, admin, ban

tBot = tb.TeleBot(vars.token)

def welcome(cid,msg):
    tBot.send_message(cid, "Hello, I am " + vars.name + ", and i know many physics formulas (There's a lot more coming)",reply_markup=markup.main)
    if cid not in vars.chat_ids:
        vars.chat_ids.append(cid)
        vars.cid_theme[cid]="none"
        nm = str(msg.chat.username)
        if nm == "None":
            nm = str(msg.chat.first_name)
        with Logger(nm+'_'+str(msg.chat.id)):
            print("New user:",msg.chat.first_name, msg.chat.last_name, msg.chat.username, '(' + str(msg.chat.id) + ')')

def reply_func(msg):
    cid = str(msg.chat.id)
    txt = str(msg.text)
    theme = str(vars.cid_theme.get(cid))

    nm = str(msg.chat.username)
    if nm == "None":
        nm = str(msg.chat.first_name)
    with Logger(nm+'_'+str(msg.chat.id)):
        logout(msg)
    if(cid in vars.banlist):
    	ban()

    elif(txt == "Назад"):
        back(theme,cid)
    elif(txt == "К выбору основных тем"):
        back("None", cid)
        vars.main_theme[cid] = "None"
    else:
        if(vars.main_theme[cid]=="mech" or txt == "Механика"):
            mech.reply(cid,txt,theme)
        if(vars.main_theme[cid]=="ther" or txt == "Термодинамика"):
            ther.reply(cid,txt,theme)
        if(vars.main_theme[cid]=="eles" or txt == "Электростатика"):
        	eles.reply(cid,txt,theme)
        if(vars.main_theme[cid]=="bugs" or txt == "Ошибки и предложения"):
        	bugs.reply(cid,txt,theme)


