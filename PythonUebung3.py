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
bd_indays    = 'Dein Geburtstag ist in xx Tagen.'
bd_yold      = 'Du bist also XX Jahre alt und wurdest am XXX gebohren'

def drawtitle(greetingtext, linesymbol = "-"): # just drawing the title
    line = linesymbol * width
    print(line)
    print(greetingtext.center(width," "))
    print(line)

def calc_bd(year,month,day):
    print('')


drawtitle(greetingtext,'-')
print(question)
year = 1988
month = 1
day = 12
today = datetime.date.today()
birthday = datetime.date(year, month, day)
difdays = today-birthday
print(today)
print(difdays)