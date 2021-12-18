#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

from operator import truediv
import random

linesymbol   = '-'                  # Zeichen für die Menu Linie
greetingtext = 'PRÜFUNGS ORAKLE'          # Begrüßungstext
question     = 'Wieviel Punkte wirst du in der Prüfung erreichen (1-100)? '     # Frage nach Name
to_low       = 'Du schaffst mehr, versuche es noch einmal? '
to_high      = 'Leider nicht so viele, probiere es noch einmal? '
match        = 'Richtig geraten!'
width         = len(greetingtext)*2 # Wie breit das Menu wird
line = linesymbol * width

def ask_int(question):  # Asking for a number between 1-100
    it_is = True
    while it_is:
        try:            # is it a valid enter?
            anser = int(input(question))
            it_is = False
        except ValueError:
            it_is = True
        if anser <= 100 or anser >= 0:  
            it_is = True
    return anser

def guess():
    points = random.randrange(1, 100)

    question     = 'Wieviel Punkte wirst du in der Prüfung erreichen (1-100)? '
    guessnr = ask_int(question)

    while guessnr != points:
        if guessnr <= points:
            ask = to_low
            guessnr = ask_int(ask)
        elif guessnr >= points:
            ask = to_high
            guessnr = ask_int(ask)
    print(match)

    

print(line)
print(greetingtext.center(width," "))
print(line)

guess()