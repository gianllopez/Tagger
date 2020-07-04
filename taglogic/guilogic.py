# main GUI imports bases.
from .utilities import MUSICPATH, COVERSPATH, replchars, rmbytes, EXPATH
from tkinter.messagebox import showinfo, showerror
from tkinter import PhotoImage
from os import listdir, remove
from os.path import splitext
from eyed3 import load, log

# main GUI code bases.

# eyed3 just log the errors.
log.setLevel('ERROR')

# it contains all the .mp3s from the path given by the user.
songs = (song for song in listdir(MUSICPATH))

# this function shows the next mp3.
def nextsong(varsdict, imgbtn, default_album):
    try:
        global tags, song, album, def_album
        song = MUSICPATH + next(songs)
        MP3 = load(song)
        tags = MP3.tag
        album = tags.album
        def_album = default_album
        def_album.set(album)
        artist = tags.artist
        varsdict['Título'].set(rmbytes(tags.title))
        varsdict['Artista'].set(rmbytes(artist))
        varsdict['Género'].set(rmbytes(str(tags.genre)))
        varsdict['Álbum'].set(rmbytes(album))
        cover = PhotoImage(file=COVERSPATH + replchars(album) + '.png')
        imgbtn['image'] = cover
        imgbtn.image = cover        
    except Exception as error:
        name = error.__class__.__name__
        if name == 'TclError':
            showerror('Tagger - Error en cover', 'El cover del ábum %s de %s está erróneo, prueba elimimando la carpeta covers y volviendo a ejecutar getcovers.py' % (album, artist)) 
            remove(song)
            nextsong(varsdict, imgbtn, default_album)
        if name == 'AttributeError':
            if  splitext(song)[1] in ('.mp3', '.Mp3', '.MP3'):
                showerror('Tagger - MP3 Corrupto', 'El archivo MP3 (' + song + ') está corrupto y nuestro interprete no puede trabajar con él, este tipo de archivos los pasamos a la carpeta songs/untagged/')
            else:
                remove(song)
        if name == 'StopIteration':
            showinfo('Tagger - Información', 'No encuentro más canciones para taggear, revisa si en la ruta que me pasaste aún quedan canciones, si no es así, es porque ya taggeaste todo, puedes ver las canciones taggeadas en tu carpeta de exportación/taggeds/')

# this function saves all the metatags, including the cover.
def savetags(varsdict, imgbtn):
    new_title = varsdict['Título'].get()
    new_artist = varsdict['Artista'].get()
    tags.title = new_title
    tags.artist = new_artist
    tags.genre = varsdict['Género'].get()
    tags.album = varsdict['Álbum'].get()
    tags.images.set(3, open(COVERSPATH + album + '.png', 'rb').read(), 'image/png')
    tags.save()
    try:
        open(EXPATH + 'taggeds/' + new_artist + ' - ' + new_title + '.mp3', 'wb').write(open(song, 'rb').read())
        remove(song)
        showinfo('Tagger - ¡Canción Taggeada!', '%s de %s ya fue taggeada con exito, la puedes encontrar en la carpeta de exportación/tagged/.' % (new_title, new_artist))
    except ValueError:
        showerror('Tagger - Error', 'Uno de los metadatos de esta canción contiene bytes infiltrados, prueba a borrar las casillas de título y artista y volverlas a llenar.')
    nextsong(varsdict, imgbtn, def_album)