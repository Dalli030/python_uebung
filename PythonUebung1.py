#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

linesymbol   = '-'                  # Zeichen f�r die Menu Linie
greetingtext = 'MOIN MOIN'          # Begr��ungstext
askname      = 'Wie hei�t du? '     # Frage nach Name

width         = len(greetingtext)*2 # Wie breit das Menu wird

line = linesymbol * width 

print(line)
print(greetingtext.center(width," "))
print(line)
name = input(askname)
print('\nMoin moin,',name)
