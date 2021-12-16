#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import random

linesymbol   = '-'                  # Zeichen f�r die Menu Linie
greetingtext = 'PR�FUNGS ORAKLE'          # Begr��ungstext
question     = 'Wieviel Punkte wirst du in der Pr�fung erreichen? '     # Frage nach Name
to_low       = 'Du schaffst mehr, versuche es noch einmal? '
to_high      = 'Leider nicht so viele, probiere es noch einmal? '
match        = 'Richtig geraten!'
width         = len(greetingtext)*2 # Wie breit das Menu wird
line = linesymbol * width

def guess():
    points = random.randrange(1, 100)
    guessnr = int(input(question))
    while guessnr != points:
        if guessnr <= points:
            ask = to_low
        elif guessnr >= points:
            ask = to_high
        guessnr = int(input(ask))
    print(match)

   
print(line)
print(greetingtext.center(width," "))
print(line)

guess()