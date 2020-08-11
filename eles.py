import vars
import markup
import telebot as tb
from logger import Logger as log
from main_func import logout, opn, back

tBot = tb.TeleBot(vars.token)

def reply(cid,txt,theme):
	if(txt == "Электростатика"):
		tBot.send_message(cid, "Выберите раздел", reply_markup=markup.eles) 
		vars.cid_theme[cid]="eles"
		vars.main_theme[cid]="eles"
	if(txt == "Электроемкость"):
		tBot.send_message(cid, "Электроемкость", reply_markup=markup.capa)
		vars.cid_theme[cid]="capa"
	if(txt == "Потенциал"):
		tBot.send_message(cid, "Потенциал", reply_markup=markup.pote)
		vars.cid_theme[cid]="pote"

	ph = "0"

	if(txt == "Закон Кулона"):
		ph = opn("kulon")
	if(txt == "Напряженность электрического\nполя"):
		ph = opn("napr")
	if(txt == "Электрическое поле\nмежду пластинами"):
		ph = opn("double")
	if(txt == "Сила на заряд"):
		ph = opn("forsch")
	if(txt == "Емкость конденсатора"):
		ph = opn("konde")
	if(txt == "Плоский конденсатор"):
		ph = opn("plosk")
	if(txt == "Сферический конденсатор"):
		ph = opn("esphe")
	if(txt == "Взаимодействие зарядов"):
		ph = opn("vzaim")
	if(txt == "Электрического поля"):
		ph = opn("poten")
	if(txt == "Точечный заряд"):
		ph = opn("potto")
	if(txt == "Конденсаторы"):
		ph = opn("konds")

	if(ph != "0"):
		tBot.send_photo(cid, ph)