#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


greetingtext = 'GEBURTSTAG'          # Begrüßungstext
question     = 'Wieviel Punkte wirst du in der Prüfung erreichen (1-100)? '     # Frage nach Name
width        = len(greetingtext)*2 # Wie breit das Menu wird
question     = 'Wann wurdest du gebohren?'
qyear        = 'Welches Jahr? '
qmonth       = 'Welchen Monat? '
qday         = 'Welchen Tag? '
bd_past      = 'Dein Geburtstag ist dieses Jaht schon vorbei.'
bd_today     = 'Dein Geburtstag ist heute.'
bd_future    = 'Dein Geburtstag kommt dieses Jahr noch.'
bd_indays    = 'Dein Geburtstag ist in xx Tagen.'

def drawtitle(greetingtext, linesymbol = '-'): # just drawing the title
    line = linesymbol * width
    print(line)
    print(greetingtext.center(width," "))
    print(line)

drawtitle(greetingtext,'-')
print(question)
