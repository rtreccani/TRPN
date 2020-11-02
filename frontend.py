import os
import curses, textwrap, time
from curses import wrapper
from curses.textpad import Textbox

currentFriend = 'Alex Jones'

def lSize():
    return(int(curses.COLS/3))

def rSize():
    return(curses.COLS - int(curses.COLS/3))

def createScreen():
    #main screen init
    s = curses.initscr()
    s.clear()
    return(s)

def addFriendsToWindow(w, selected):
    w.border()
    w.refresh()
    
def weirdTerminationStuff(x):
    inputWin.border()
    if x == 10:
        x = 7
        messageReadyFlag = True
    else:
        messageReadyFlag = False
    return x

def createContactsWindow(s):
    w = curses.newwin(curses.LINES-1, lSize(), 1, 1)
    w.border()
    s.refresh()
    return(w)

def createMessageWindow(s):
    w = curses.newwin(curses.LINES-4, rSize()-1, 1, lSize()+1)
    w.border()
    s.refresh()
    return(w)

def createInputDerwin(s):
    temp = curses.newwin(3, rSize()-1, curses.LINES-3, lSize()+1)
    temp.border()
    s.refresh()
    derWin = temp.derwin(1,1)
    temp.refresh()
    return(derWin)

def enableEditing(d):
    b = Textbox(d)
    return(b)

def fillMessageWindow(w, offset):
    # file = open("messages/Alex Jones/messages.txt")
    # lines = file.readlines()
    # i=0
    # for line in reversed(lines):
    #     direction = line[0:1]
    #     if(i >= offset):
    #         if(i < (curses.LINES - 10)):
    #             if(direction == 'r'):
    #                 w.addstr(curses.LINES-6-i, 1, line[1:])
    #             elif(direction == 's'):
    #                 w.addstr(curses.LINES-6-i, 1, line[1:].rjust(rSize()-2))
    #             else:
    #                 w.addstr(curses.LINES-6-i, 1, 'invalid header char')
    #     i=i+1
    w.border()
    w.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    screen = createScreen()
    leftWin = createContactsWindow(screen)
    rightWin = createMessageWindow(screen)
    addFriendsToWindow(leftWin, 0)
    fillMessageWindow(rightWin, 0)
    screen.refresh()

    inputWin = createInputDerwin(screen)
    inputWin.refresh()
    inputWin.standout()
    editor = enableEditing(inputWin)
    editor.edit(weirdTerminationStuff)
    editor.gather()
    inputWin.standend()

    while(1==1):


        x=screen.getkey()
        if(x == 'q'):
            break

wrapper(main)