import vars
import markup
import telebot as tb
from logger import Logger as log
from main_func import logout, opn, back

tBot = tb.TeleBot(vars.token)

def reply(cid,txt,theme):
    if (txt == "Ошибки и предложения"):
        tBot.send_message(cid,"Нашли ошибку или хотите что-то предложить?",reply_markup=markup.bugs)
        vars.main_theme[cid]="bugs"

    if(txt == "Ошибка"):
        tBot.send_message(cid,"Опишите ошибку, найденную вами")
        vars.filename = "bugs"
    if(txt == "Предложение"):
        tBot.send_message(cid,"Что вы хотели предложить?")
        vars.filename = "offers"


    if(vars.filename == "bugs" or vars.filename == "offers"):
        if(message.text != "Ошибка" and message.text != "Предложение"):
            with Logger(vars.filename,"bo"):
               logout()
            mes = "0"
            if(vars.filename == "bugs"):
                mes = "Благодарим за находку данной ошибки, постараемся исправить в ближайшее время"
            if(vars.filename == "offers"):
                mes = "Благодарим за предложение. Обязательно рассмотрим и решим что с ним делать..."
            tBot.send_message(message.chat.id, mes)
            vars.filename = str(message.chat.username)+'_'+str(message.chat.id)