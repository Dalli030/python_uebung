#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
# https://github.com/Dalli030/python-grundlagen/tree/master/04%20todo

import datetime
import pickle

greetingtext = 'TODO-LISTE'          # Begrüßungstext
mainmenu1       = 'Wilkommen in der TODO-Liste. Was möchtest du tun? '
mainmenu2       = 'Einträge [A]nzeigen, [H]inzufügen, [L]öchen oder b[E]enden? '
loadtxt         = '... Lade Einträge aus @1 ...'
entrytxt        = '... @1 Einträge geladen ...'

width        = len(greetingtext)*2 # Wie breit das Menu wird

# Initial variables for testing
todos = ['Aufräumen', 'Ein Buch Lesen', 'Sport machen']

def writetodo(todos):
    with open('todo.dat', 'wb') as fp:
        pickle.dump(todos, fp)

def readtodo(todos):       # no error correction
    with open ('todo.dat', 'rb') as fp:
        todos = pickle.load(fp)
    return todos

def addtodo(todos):
    todos.append(input('Welche Aufgabe hinzufügen? '))
    print('Wurde hinzugefügt...')
    return todos

def showtodo(todos):    # Output should be "- Task"
    for line in todos:
        print('- ',line)

def deltodo(todos):
    i = 0
    for line in todos:
        i += 1
        print(i,' ',line)
    deltask = int(input('Welche TODO soll gelöscht werden? '))
    if deltask < 1 or deltask > i:
        print('Ungültige Eingabe!')
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
        # print('Hinzufügen')
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
        todos = ['Aufräumen', 'Ein Buch Lesen', 'Sport machen']
        writetodo(todos)
        print('Datensatz resetet...')


