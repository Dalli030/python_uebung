#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import datetime

greetingtext = 'GEBURTSTAG'          # Begrüßungstext
question     = 'Wieviel Punkte wirst du in der Prüfung erreichen (1-100)? '     # Frage nach Name
width        = len(greetingtext)*2 # Wie breit das Menu wird
question     = 'Wann wurdest du gebohren?'
qyear        = 'Welches Jahr? '
qmonth       = 'Welchen Monat? '
qday         = 'Welchen Tag? '
bd_past      = 'Dein Geburtstag ist dieses Jahr schon vorbei.'
bd_today     = 'Dein Geburtstag ist heute.'
bd_future    = 'Dein Geburtstag kommt dieses Jahr noch.'
bd_indays    = 'Dein Geburtstag ist in @1 Tagen.'
bd_yold      = 'Du bist also @1 Jahre alt und wurdest am @2 gebohren'

def drawtitle(greetingtext, linesymbol = "-"): # just drawing the title
    line = linesymbol * width
    print(line)
    print(greetingtext.center(width," "))
    print(line)

def calc_bd(year,month,day):
    print(qyear)


drawtitle(greetingtext,'-')
print(question)
is_num = True
'''
# just for testing
year = 1980
month = 1
day = 1
'''
while is_num:   # ask for bd year
    try:
        is_num = False
        year = int(input(qyear))
        if year < 0 or year > 3000:
            is_num = True
    except ValueError:
        is_num = True

is_num = True
while is_num:   # ask for bd month
    try:
        is_num = False
        month = int(input(qmonth))
        if month < 1 or month > 12:
            is_num = True
    except ValueError:
        is_num = True
is_num = True
while is_num:
    try:
        is_num = False
        day = int(input(qday))
        if day < 1 or day > 31:
            is_num = True
    except ValueError:
        is_num = True

        
today = datetime.date.today()
yearsold = today.year - year - ((today.month, today.day) < (month, day)) # Alter ausrechnen

bd_days = datetime.date(today.year,month,day) - today
bd_daysnxt = datetime.date(today.year+1,month,day) - today
bddaysstr = str(bd_days)    # workaround because i can nor read the days out of the date
bddaysstr = bddaysstr[:bddaysstr.find(' ')] # convert the date to a string and cut the day-str out
bddaysstrnxt = str(bd_daysnxt)    # if bd in next year i do it again
bddaysstrnxt = bddaysstrnxt[:bddaysstrnxt.find(' ')]
if int(bddaysstr) < 0:
    bddaysstr = bddaysstrnxt


bd_yold = bd_yold.replace('@1',str(yearsold))
bd_yold = bd_yold.replace('@2',str(datetime.date(year,month,day)))
print(bd_yold)
bd_indays = bd_indays.replace('@1',str(bddaysstr))
print(bd_indays)

if today == datetime.date(today.year,month,day):
    print(bd_today)
elif today > datetime.date(today.year,month,day):
    print(bd_past)
elif today < datetime.date(today.year,month,day):
    print(bd_future)

