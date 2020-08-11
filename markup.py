from telebot.types import KeyboardButton as kb
from telebot.types import ReplyKeyboardMarkup as rp

non 	 	 = kb("non")
back_butt	 = kb("Назад")
main_butt	 = kb("К выбору основных тем")
back_list	 = kb("Предыдущая страница")
frwd_list	 = kb("Следующая страница")

###MAIN###
main_mech    = kb("Механика")
main_ther	 = kb("Термодинамика")
main_eles    = kb("Электростатика")
main_bugs  	 = kb("Ошибки и предложения")
main = rp(True)
main.row(main_mech, main_ther, main_eles)
main.row(main_bugs)

###BUGS###
bugs_bugs	 = kb("Ошибка")
bugs_advi	 = kb("Предложение")
bugs = rp(True)
bugs.row(bugs_bugs,bugs_advi)
bugs.row(back_butt)


###MECHANICS###
mech_kine    = kb("Кинематика")
mech_dynm    = kb("Динамика")
mech_stat    = kb("Статика")
mech_lawm    = kb("Законы сохранения в механике")
mech_impl    = kb("Импульс")
mech = rp(True)
mech.row(mech_kine,mech_dynm,mech_stat)
mech.row(mech_impl,mech_lawm)
mech.row(back_butt)


#ИМПУЛЬС
impl_impl    = kb("Импульс силы")
impl_lawi    = kb("Закон сохранения импульса")
impl_imom    = kb("Момент импульса")
impl = rp(True)
impl.row(impl_impl,impl_imom)
impl.row(impl_lawi)
impl.row(back_butt,main_butt)


#ЗАКОНЫ СОХРАНЕНИЯ
lawm_mwork   = kb("Механичекая работа")
lawm_engk    = kb("Кинетическая энергия")
lawm_engp    = kb("Потенциальная энергия")
lawm_gravw   = kb("Работа силы тяжести")
lawm_meche   = kb("Полная механическая энергия")
lawm_deff    = kb("Упругая дефформация тела")
lawm_powr    = kb("Мощность")
lawm = rp(True)
lawm.row(lawm_engp,lawm_powr,lawm_engk)
lawm.row(lawm_mwork,lawm_gravw)
lawm.row(lawm_deff,lawm_meche)
lawm.row(back_butt,main_butt)


#ПОТЕНЦИАЛЬНАЯ ЭНЕРГИЯ
engp_grav    = kb("Поднятое тело")
engp_uprw    = kb("Упругое деформирование")
engp = rp(True)
engp.row(engp_grav,engp_uprw)
engp.row(back_butt,main_butt)


#СТАТИКА
stat_levr   = kb("Рычаг")
stat_momf   = kb("Момент силы")
stat = rp(True)
stat.row(stat_levr,stat_momf)
stat.row(back_butt,main_butt)


#КИНЕМАТИКА
kine_fall    = kb("Свободное падение")
kine_circ    = kb("Движение по окружности")
kine_dvzh    = kb("Движение тел вверх/вниз")
kine_move    = kb("Движение с постоянным ускорением")
kine = rp(True)
kine.row(kine_fall,kine_circ)
kine.row(kine_dvzh,kine_move)
kine.row(back_butt,main_butt)


#ТЕЛА ВВ,ВН
dvzh_time    = kb("Время подъема")
dvzh_hmax    = kb("Максимальная высота подъема")
dvzh = rp(True)
dvzh.row(dvzh_hmax)
dvzh.row(dvzh_time,non)
dvzh.row(back_butt,main_butt)


###DYNAMICS###
dynm_forc    = kb("Силы")
dynm_coef    = kb("Пружины")
dynm_pres    = kb("Давления")
dynm_kosm    = kb("Космические")
dynm_laws    = kb("Законы Ньютона")
dynm_grav    = kb("Всемирное тяготение")
dynm = rp(True)
dynm.row(dynm_kosm,dynm_pres, dynm_coef)
dynm.row(dynm_grav,dynm_forc, dynm_laws)
dynm.row(back_butt,main_butt)


#ДАВЛЕНИЯ
pres_pres    = kb("Давление")
pres_liqd    = kb("Давление в жидкости")
pres = rp(True)
pres.row(pres_pres,pres_liqd)
pres.row(back_butt,main_butt)


#ЗАКОНЫ НЬЮТОНА
laws_1       = kb("1 закон")
laws_2       = kb("2 закон")
laws_3	     = kb("3 закон")
laws = rp(True)
laws.row(laws_1,laws_2,laws_3)
laws.row(back_butt,main_butt)


#СИЛЫ
forc_fric    = kb("Сила трения")
fors_arch    = kb("Сила Архимеда")
forc_upr     = kb("Сила упругости")
forc = rp(True)
forc.row(forc_upr,fors_arch, forc_fric)
forc.row(back_butt,main_butt)


#ПРУЖИНЫ
coef_parr	 = kb("Параллельное соединение")
coef_posl    = kb("Последовательное соединение")
coef = rp(True)
coef.row(coef_parr,coef_posl)
coef.row(back_butt,main_butt)


#ВСЕМ ТЯГОТЕНИЕ
grav_tagt	 = kb("Закон всемирного тяготения")
grav_speed	 = kb("Скорость спутника на круговой орбите")
grav_uskr	 = kb("Ускорение свободного падения на некоторой высоте")
grav = rp(True)
grav.row(grav_tagt,grav_uskr,grav_speed)
grav.row(back_butt,main_butt)


#КОСМИЧЕСКИЕ
kosm_perv	 = kb("Первая космическая")
kosm_secd    = kb("Вторая космическая")
kosm_thrd    = kb("Третья космическая")
kosm = rp(True)
kosm.row(kosm_perv,kosm_secd,kosm_thrd)
kosm.row(back_butt,main_butt)


###ELECTROSTATICS###
eles_lawK    = kb("Закон Кулона")
eles_efld    = kb("Напряженность электрического\nполя")
eles_e2pp    = kb("Электрическое поле\nмежду пластинами")
eles_fors    = kb("Сила на заряд")
eles_pote    = kb("Потенциал")
eles_capa    = kb("Электроемкость")
eles = rp(True)
eles.row(eles_lawK,eles_fors)
eles.row(eles_efld,eles_e2pp)
eles.row(eles_pote,eles_capa)
eles.row(back_butt)

capa_ekon    = kb("Емкость конденсатора")
capa_plos    = kb("Плоский конденсатор")
capa_sphe    = kb("Сферический конденсатор")
capa = rp(True)
capa.row(capa_ekon,capa_plos)
capa.row(capa_sphe)
capa.row(back_butt,main_butt)


pote_vzam    = kb("Взаимодействие зарядов")
pote_elep    = kb("Электрического поля")
pote_toch    = kb("Точечный заряд")
pote = rp(True)
pote.row(pote_vzam,pote_elep)
pote.row(pote_toch)
pote.row(back_butt,main_butt)

###THERMODYNAMICS###
ther_innr	 = kb("Внутренняя энергия")
ther_ings	 = kb("Внутренняя энергия идеального газа")
ther_trde	 = kb("Виды теплообмена")
ther_work	 = kb("Работа газа")
ther_htam	 = kb("Количество теплоты")
ther_phaz	 = kb("Фазовые переходы")
ther = rp(True)
ther.row(ther_innr, ther_trde)
ther.row(ther_work, ther_htam)
ther.row(ther_phaz, ther_ings)
ther.row(back_butt, frwd_list)


###HEATTRADE###
trde_cond	 = kb("Теплопроводность")
trde_conv	 = kb("Конвекция")
trde_rays	 = kb("Излучение")
trde = rp(True)
trde.row(trde_cond, trde_conv, trde_rays)
trde.row(back_butt, main_butt)


###PHAZES###
phaz_melt	 = kb("Плавление")
phaz_crys	 = kb("Кристализация")
phaz_vapr	 = kb("Парообразование")
phaz_cond	 = kb("Конденсация")
phaz = rp(True)
phaz.row(phaz_melt, phaz_crys)
phaz.row(phaz_vapr, phaz_cond)
phaz.row(back_butt, main_butt)

term2_isot  = kb("Изотермический процесс")
term2_isoh  = kb("Изохорный процесс")
term2_isob  = kb("Изобарный процесс")
term2_adia  = kb("Адиабатный процесс")
term2_kopd  = kb("КПД")
term2 = rp(True)
term2.row(term2_adia, term2_isob)
term2.row(term2_isoh, term2_isot)
term2.row(term2_kopd)
term2.row(back_butt, back_list)