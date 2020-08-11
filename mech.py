import vars
import markup
import telebot as tb
from logger import Logger as log
from main_func import logout, opn, back

tBot = tb.TeleBot(vars.token)

def reply(cid,txt,theme):
    mes = "0"
    ph = "0"

    if(txt == "Механика"):
        tBot.send_message(cid, "Выберите раздел", reply_markup=markup.mech)
        vars.cid_theme[cid]="mech"
        vars.main_theme[cid]="mech"
    if(txt == "Кинематика"):
        tBot.send_message(cid, "Кинематика", reply_markup=markup.kine)
        vars.cid_theme[cid]="kine"
    if(txt == "Статика"):
        tBot.send_message(cid, "Статика", reply_markup=markup.stat)
        vars.cid_theme[cid]="stat"
    if(txt == "Динамика"):
        tBot.send_message(cid, "Динамика", reply_markup=markup.dynm)
        vars.cid_theme[cid]="dinm"
    if(txt == "Давления"):
        tBot.send_message(cid, "Давления", reply_markup=markup.pres)
        vars.cid_theme[cid]="pres"
    if(txt == "Законы сохранения в механике"):
        tBot.send_message(cid,"Законы сохранения в механике",reply_markup=markup.lawm)
        vars.cid_theme[cid]="lawm"
    if(txt == "Потенциальная энергия"):
        tBot.send_message(cid, "Потенциальная энергия",reply_markup=markup.engp)
        vars.cid_theme[cid]="engp"
    if(txt == "Равномерное движение"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.move)
        vars.cid_theme[cid]="move"
    if(txt == "Движение тел вверх/вниз"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.dvzh)
        vars.cid_theme[cid]="dvzh"
    if(txt == "Законы Ньютона"):
        tBot.send_message(cid, "Выберите закон", reply_markup=markup.laws)
        vars.cid_theme[cid]="laws"
    if(txt == "Силы"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.forc)
        vars.cid_theme[cid]="forc"
    if(txt == "Пружины"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.coef)
        vars.cid_theme[cid]="coef"
    if(txt == "Всемирное тяготение"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.grav)
        vars.cid_theme[cid]="grav"
    if(txt == "Импульс"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.impl)
        vars.cid_theme[cid]="impl"
    if(txt == "Космические"):
        tBot.send_message(cid, "Выберите формулу", reply_markup=markup.kosm)
        vars.cid_theme[cid]="kosm"
    


    if(txt == "non"):
        mes = "Здесь определённо должно быть что-то, что появится в будщем (но возможно админ просто забыл это убрать:) и было бы не плохо ему об этом сообщить)"
    if(txt == "1 закон"):
        mes = "Если на тело нет внешних воздействий, то данное тело сохраняет состояние покоя или равномерного прямолинейного движения относительно Земли.\n(Нет формулы)"
    if(txt == "2 закон"):
        ph = opn("laws_2")
        tBot.send_message(cid,"Сила, действующая на тело, равна произведению массы тела на сообщаемое этой силой ускорение, причем направления силы и ускорения совпадают.\nЕсли на тело действует сила, то оно приобретает ускорение.")
    if(txt == "3 закон"):
        ph = opn("laws_3")
    if(txt == "Ускорение свободного падения на некоторой высоте"):
        ph = opn("grav_2")
    if(txt == "Закон всемирного тяготения"):
        ph = opn("grav_1")
    if(txt == "Скорость спутника на круговой орбите"):
        ph = opn("grav_3")
    if(txt == "Сила упругости"):
        ph = opn("forc_2")
    if(txt == "Сила трения"):
        ph = opn("forc_1")
    if(txt == "Сила Архимеда"):
        ph = opn("arhf")
    if(txt == "Давление"):
        ph = opn("pres")
    if(txt == "Давление в жидкости"):
        ph = opn("liqp")
    if(txt == "Последовательное соединение"):
        ph = opn("parl")
    if(txt == "Параллельное соединение"):
        ph = opn("posl")
    if(txt == "Средняя скорость перемещения"):
        ph = opn("move_1")
    if(txt == "Перемещение по x"):
        ph = opn("move_2")
    if(txt == "Движение по окружности"):
        ph = opn("circ")
    if(txt == "Свободное падение"):
        ph = opn("fall")
    if(txt == "Движение с постоянным ускорением"):
        ph = opn("xdis")
    if(txt == "Максимальная высота подъема"):
        ph = opn("hmax")
    if(txt == "Время подъема"):
        ph = opn("time")
    if(txt == "Первая космическая"):
        ph = opn("kosm_1")
        mes = "Минимальная скорость с которой должно двигаться тело чтобы оторваться от поверхности планеты"
    if(txt == "Вторая космическая"):
        ph = opn("kosm_2")
        mes = "Минимальная горизонтальная скорость, которую необходимо придать объекту, чтобы он совершал движение по круговой орбите вокруг планеты и не начал падать"
    if(txt == "Третья космическая"):
        ph = opn("kosm_3")
        mes = "Минимальная скорость, которую необходимо придать находящемуся вблизи поверхности Земли телу, чтобы оно могло преодолеть гравитационное притяжение Земли и Солнца и покинуть пределы Солнечной системы"
    if(txt == "Момент силы"):
        mes = "M - момент силы (N*m)\nf - Приложенная сила (N)\nr - расстояние от центра вращения до места приложения силы (m)\nl - длина перепендикуляра, опущенного из центра вращения на линию действия силы (m)\na - угол, между вектором силы F и вектором положения r"
        ph = opn("mom")
    if(txt == "Рычаг"):
        mes = "F1 - Нагрузка (N)\nF2 - Сила уравновешевающая нагрузку F1 (N)\nl1 - Плечо нагрузки (m)\nl2 - Плечо силы уравновешивающей нагрузку F1 (m)"
        ph = opn("lev")
    if(txt == "Поднятое тело"):
        ph = opn("peg")
    if(txt == "Упругое деформирование"):
        ph = opn("pes")
    if(txt == "Мощность"):
        ph = opn("powr")
    if(txt == "Кинетическая энергия"):
        ph = opn("engk")
    if(txt == "Механичекая работа"):
        ph = opn("mechw")
    if(txt == "Работа силы тяжести"):
        ph = opn("gravw")
    if(txt == "Упругая дефформация тела"):
        ph = opn("workd")
    if(txt == "Полная механическая энергия"):
        ph = opn("ener")
    if(txt == "Импульс силы"):
        ph = opn("impl")
    if(txt == "Закон сохранения импульса"):
        ph = opn("ilaw")
    if(txt == "Момент импульса"):
        ph = opn("imom")
    if(mes != "0"):
        tBot.send_message(cid,mes)
    if(ph != "0"):
        tBot.send_photo(cid,ph)