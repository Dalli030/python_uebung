#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
# https://github.com/Dalli030/python-grundlagen/tree/master/04%20todo

import datetime
import pickle

greetingtext = 'TODO-LISTE'          # Begr��ungstext
mainmenu1       = 'Wilkommen in der TODO-Liste. Was m�chtest du tun? '
mainmenu2       = 'Eintr�ge [A]nzeigen, [H]inzuf�gen, [L]�chen oder b[E]enden? '
loadtxt         = '... Lade Eintr�ge aus @1 ...'
entrytxt        = '... @1 Eintr�ge geladen ...'

width        = len(greetingtext)*2 # Wie breit das Menu wird

# Initial variables for testing
todos = ['Aufr�umen', 'Ein Buch Lesen', 'Sport machen']

def writetodo(todos):
    with open('todo.dat', 'wb') as fp:
        pickle.dump(todos, fp)

def readtodo(todos):       # no error correction
    with open ('todo.dat', 'rb') as fp:
        todos = pickle.load(fp)
    return todos

def addtodo(todos):
    todos.append(input('Welche Aufgabe hinzuf�gen? '))
    print('Wurde hinzugef�gt...')
    return todos

def showtodo(todos):    # Output should be "- Task"
    for line in todos:
        print('- ',line)

def deltodo(todos):
    i = 0
    for line in todos:
        i += 1
        print(i,' ',line)
    deltask = int(input('Welche TODO soll gel�scht werden? '))
    if deltask < 1 or deltask > i:
        print('Ung�ltige Eingabe!')
        return todos
    todos.pop(deltask-1)
    return todos

def drawtitle(greetingtext, linesymbol = "-"): # just drawing the title
    line = linesymbol * width
    print(line)
    print(greetingtext.center(width," "))
    print(line)

todos = readtodo(todos)
counttodo = len(todos)
loadtxt = loadtxt.replace('@1',str(counttodo))
drawtitle(greetingtext,'-')
print(loadtxt)
print(entrytxt)
print(mainmenu1)
exitpro = True
while exitpro:
    menuent = input(mainmenu2)
    if menuent == 'H':
        # print('Hinzuf�gen')
        todos = addtodo(todos)
    elif menuent == 'A':    # 
        showtodo(todos)
    elif menuent == 'L':
        todos = deltodo(todos)
    elif menuent == 'E':    # need to add a save function
        print('Wird beendet...')
        writetodo(todos)
        exitpro = False
    elif menuent == "R":
        todos = ['Aufr�umen', 'Ein Buch Lesen', 'Sport machen']
        writetodo(todos)
        print('Datensatz resetet...')


