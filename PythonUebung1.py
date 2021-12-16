#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

linesymbol   = '-'                  # Zeichen f�r die Menu Linie
greetingtext = 'Moin moin'          # Begr��ungstext
askname      = 'Wie hei�t du? '     # Frage nach Name

err_tittolong = "Der Titel darf nicht l�nger als Titelline sein (",width,") sein" 
width         = len(greetingtext)*2 # Wie breit das Menu wird

line = linesymbol * width 
if len(greetingtext)>width:
    print(err_tittolong) 
    quit()
print(line)
print(greetingtext.center(width," "))
print(line)
name = input(askname)
print('\nMoin moin,',name)
