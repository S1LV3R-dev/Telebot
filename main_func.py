import vars
import markup
import telebot as tb

tBot = tb.TeleBot(vars.token)

def opn(x):
    k = "./form/"+str(x)+".png"
    a = open(k,"rb").read()
    return a;

def back(x, cid):
    if x == "None" or x == "mech" or x == "eles" or x == "ther":
        tBot.send_message(cid, "Hello, I am " + vars.name + ", and i know many physics formulas", reply_markup=markup.main)
        vars.cid_theme[cid]="None"
        vars.main_theme[cid]="None"

    if x == "kine" or x == "dinm" or x == "stat" or x=="lawm" or x=="impl":
        tBot.send_message(cid, "Выберите раздел механики", reply_markup=markup.mech)
        vars.cid_theme[cid]="mech"

    if x == "fall" or x == "move" or x == "circ" or x == "dvzh":
        tBot.send_message(cid, "Выберите раздел кинематики", reply_markup=markup.kine)
        vars.cid_theme[cid]="kine"
    if x == "pote" or x == "capa":
        tBot.send_message(cid, "Выберите раздел Электростатики", reply_markup=markup.eles)
        vars.cid_theme[cid]="eles"
    if x == "trde" or x == "phaz":
        tBot.send_message(cid, "Выберите раздел термодинамики", reply_markup=markup.ther)
        vars.cid_theme[cid]="ther"

    if x == "engp":
        tBot.send_message(cid, "Законы сохранения в механике", reply_markup=markup.lawm)
        vars.cid_theme[cid]="lawm"

    if x == "laws" or x == "forc" or x == "coef" or x == "kosm" or x == "grav" or x =="pres":
        tBot.send_message(cid, "Динамика", reply_markup=markup.dynm)
        vars.cid_theme[cid]="dinm"

def logout(message):
        print(message.chat.first_name,end=' ')
        if(str(message.chat.last_name)!="None"):
            print(message.chat.last_name,end=' ')
        print('('+str(message.chat.id)+')','->',message.text)

def ban():
    tBot.send_message(cid,"Вы в бане")
def admin():
    tBot.send_message(cid, "administrator")