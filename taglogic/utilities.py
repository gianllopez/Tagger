from os import mkdir

paths = open('user-music-path.txt', 'r').read().replace('\\', '/').split(', ')
MUSICPATH = paths[0] + '/'
EXPATH = paths[1] + '/'
COVERSPATH = 'img-content/covers/'

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

rmbytes = lambda exp : exp.replace('\x00', '; ').strip()