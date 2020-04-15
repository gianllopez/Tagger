from sys import platform
from os import makedirs, mkdir, system
from PIL import Image
from tkinter import PhotoImage
musicpath = open('user-music-path.txt', 'r').readline().replace('\\', '/') + '/'
coverspath = 'gui/imgs-data/covers/'
def replchars(expression, mode='replace'):
    dictchars = {
        '\\' : '(char1)',
        '/' : '(char2)',
        ':' : '(char3)',
        '*' : '(char4)',
        '?' : '(char5)',
        '"' : '(char6)',
        '<' : '(char7)',
        '>' : '(char8)',
        '|' : '(char9)'
                }
    for char in dictchars:
        if mode == 'replace':
            expression = expression.replace(char, dictchars[char])
        if mode == 'unreplace':
            expression = expression.replace(dictchars[char], char)
    return expression
def intbtns(state, btnslist, root):
    for btn in btnslist:
        btn['state'] = state
        if state == 'normal':
            root.destroy()
            
rmbytes = lambda exp : exp.replace('\x00', '; ').strip()

def mkdirs():
    makedirs('songs/taggeds', exist_ok=True)
    try:
        mkdir('songs/untaggeds')
        mkdir('gui/imgs-data/covers')
    except FileExistsError:
        pass

def noNone(npt, var):
    if npt == '' or npt == None:
        npt = var
    if '=' in npt:
        npt = npt.replace('=', var)
    return npt.title()

def clearshell():
    os = platform
    if os == 'win32':
        system('cls')
    if os == 'darwin' or os == 'linux':
        system('clear')