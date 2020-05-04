from gui.taglogic import listdir, remove, replchars, load, musicpath, coverspath, Image, splitext, log, rmbytes, mkdirs, clearshell, expath
mkdirs()
log.setLevel('ERROR')
clearshell()
print('>>> Extrayendo covers de cada álbum:')
for mp3 in listdir(musicpath):
    song = musicpath + mp3
    if splitext(song)[1] in ['.mp3', '.MP3', '.Mp3']:
        MP3 = load(song)
        try:
            tags = MP3.tag
            album = replchars(tags.album)
            print('> Extrayendo cover del álbum %s de %s. ' % (replchars(album, 'unreplace'), rmbytes(tags.artist)))
            if album + '.png' not in listdir(coverspath):
                c2c = coverspath + album + '.jpg' 
                open(c2c, 'wb').write(tags.images[0].image_data)
                Image.open(c2c).resize((250, 250)).save(c2c.replace('jpg', 'png'), 'png')
                remove(c2c)
        except AttributeError:
            open(expath + 'untaggeds/' + mp3, 'wb').write(open(song, 'rb').read())
            remove(song)
            print('> Problemas con %s.' % mp3)    
    else:
        remove(song)
print('>>> Ya se extrajeron todos los covers de las canciones taggeables, revisa tu carpeta de exportación/untaggeds/ para ver los .mp3 con errores. Ahora abre gui/main-gui.py si quieres usar una interfaz o main-no-gui si quieres correrlo en consola y ¡A TAGGEAR!')