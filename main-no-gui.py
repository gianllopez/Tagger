try:
    from gui.taglogic import (musicpath, # utilities                    
                            rmbytes, # utilities
                            noNone, # utilities
                            mkdirs, # utilities
                            clearshell, # utilities
                            expath, # utilities                          
                            )
    from os import remove, listdir
    from os.path import splitext
    from eyed3 import load, log
    from urllib.request import urlopen, Request, HTTPError
    mkdirs()
    log.setLevel('ERROR')
    for mp3 in listdir(musicpath):
        song = musicpath + mp3
        process = lambda yesorno, name : open('%s/%s/%s' % (expath, yesorno, name), 'wb').write(open(song, 'rb').read())
        MP3 = load(song)
        try:
            tags = MP3.tag
            title = rmbytes(tags.title)
            artist = rmbytes(tags.artist)
            genre = rmbytes(str(tags.genre))
            album = rmbytes(tags.album)
            clearshell()
            print('>>> TAGGER: ¡Taggea tus canciones! <<<')      
            tags.artist = noNone(input('> Artista (' + artist + '): '), artist)
            tags.title = noNone(input('> Título (' + title + '): '), title)
            tags.genre = noNone(input('> Género (' + genre + '): '), genre)
            tags.album = noNone(input('> Àlbum (' + album + '): '), album)
            if input('- ¿Deseas cambiar el cover? (sólo web): ').upper() == 'SI':
                covurl = input('> URL del cover: ')
                try:
                    tags.images.set(3, urlopen(Request(covurl, headers={'User-Agent' : 'Mozilla/5.0'}), timeout=30).read(), 'image/png')
                except (HTTPError, ValueError):
                    input('> El URL que acabas de pasar no es válido.')
            tags.save()
            process('taggeds', tags.artist + ' - ' + tags.title + '.mp3')
            remove(song)            
        except AttributeError: 
            if splitext(mp3)[1] in ['.mp3', '.MP3', '.Mp3']:
                process('untaggeds', mp3)
                remove(song)
                input('> El archivo (%s) presenta problemas y no se puede taggear, encuentralo en tu carpeta de exportación/untaggeds/' % mp3)
            else:
                remove(song)
except IndexError:
    print('- La rutas en user-music-path.txt no son correctas, recuerda que tienen que estar en formato: ruta de la música, ruta de exportación.')