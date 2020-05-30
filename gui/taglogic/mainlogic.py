from .utilities import musicpath, coverspath, replchars, PhotoImage, rmbytes, expath
from eyed3 import load, log
from os import listdir, remove
from tkinter.messagebox import showinfo, showerror
from tkinter import TclError
from os.path import splitext
log.setLevel('ERROR')
songs = (song for song in listdir(musicpath))
def nextsong(varsdict, imgbtn):
    try:
        global tags, song, album
        song = musicpath + next(songs)
        if splitext(song)[1] in ['.mp3', '.MP3', '.Mp3']: 
            MP3 = load(song)
            try:
                tags = MP3.tag
                album = tags.album
                artist = tags.artist
                varsdict['Título'].set(rmbytes(tags.title))
                varsdict['Artista'].set(rmbytes(artist))
                varsdict['Género'].set(rmbytes(str(tags.genre)))
                varsdict['Álbum'].set(rmbytes(album))
                try:
                    cover2show = PhotoImage(file=coverspath + replchars(album) + '.png')
                    imgbtn['image'] = cover2show
                    imgbtn.image = cover2show
                except TclError:
                    showerror('Tagger - Error en cover', 'El cover del ábum %s de %s está erróneo, prueba elimimando la carpeta covers y volviendo a ejecutar getcovers.py' % (album, artist)) 
                    nextsong(varsdict, imgbtn)
            except AttributeError:
                showerror('Tagger - MP3 Corrupto', 'El archivo MP3 (' + song + ') está corrupto y nuestro interprete no puede trabajar con él, este tipo de archivos los pasamos a la carpeta songs/untagged/')
        else:
            remove(song)
            nextsong(varsdict, imgbtn)
    except StopIteration:
        showinfo('Tagger - Información', 'No encuentro más canciones para taggear, revisa si en la ruta que me pasaste aún quedan canciones, si no es así, es porque ya taggeaste todo, puedes ver las canciones taggeadas en tu carpeta de exportación/taggeds/')
def savetags(varsdict, imgbtn):
    title = varsdict['Título'].get()
    artist = varsdict['Artista'].get()
    tags.title = title
    tags.artist = artist
    tags.genre = varsdict['Género'].get()
    tags.album = varsdict['Álbum'].get()
    tags.images.set(3, open(coverspath + album + '.png', 'rb').read(), 'image/png')
    tags.save()
    try:
        open(expath + 'taggeds/' + artist + ' - ' + title + '.mp3', 'wb').write(open(song, 'rb').read())
        remove(song)
        showinfo('Tagger - ¡Canción Taggeada!', '%s de %s ya fue taggeada con exito, la puedes encontrar en la carpeta songs/tagged/.' % (title, artist))
    except ValueError:
        showerror('Tagger - Error', 'Uno de los metadatos de esta canción contiene bytes infiltrados, prueba a borrar las casillas de título y artista y volverlas a llenar.')
    nextsong(varsdict, imgbtn)