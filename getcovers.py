from taglogic import (
    MUSICPATH, COVERSPATH, EXPATH, # main constants.
    rmbytes, replchars # data transformers.
    )
from os import listdir, remove, mkdir
from eyed3 import load, log
from os.path import splitext
from PIL import Image

# this for cycle create the folders of the covers and exported music.
for x in [COVERSPATH, EXPATH + 'taggeds', EXPATH + 'untaggeds']:
    try:
        mkdir(x)
    except FileExistsError:
        pass

# setting the eyed3 log to onlye rrors.
log.setLevel('ERROR')

# code base.
print('>>> Extrayendo cover de cada álbum:')
for mp3 in listdir(MUSICPATH):
    song = MUSICPATH + mp3
    if splitext(song)[1] in ['.mp3', '.MP3', '.Mp3']:
        MP3 = load(song)
        try:
            tags = MP3.tag
            album = replchars(tags.album)
            print('> Extrayendo cover del álbum %s de %s. ' % (replchars(album, 'unreplace'), rmbytes(tags.artist)))
            if album + '.png' not in listdir(COVERSPATH):
                c2c = COVERSPATH + album + '.jpg' 
                open(c2c, 'wb').write(tags.images[0].image_data)
                Image.open(c2c).resize((203, 201)).save(c2c.replace('jpg', 'png'), 'png')
                remove(c2c)
        except AttributeError:
            open(EXPATH + 'untaggeds/' + mp3, 'wb').write(open(song, 'rb').read())
            print('> Problemas con %s.' % mp3)    
    else:
        remove(song)
print('>>> Ya se extrajeron todos los covers de las canciones taggeables, revisa tu carpeta de exportación/untaggeds/ para ver los .mp3 con errores. Ahora abre main-gui.py para empezar a taggear.')