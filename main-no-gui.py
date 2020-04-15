from gui.taglogic import musicpath, remove, listdir, load, log, splitext, rmbytes, noNone, mkdirs, clearshell
mkdirs()
log.setLevel('ERROR')
for mp3 in listdir(musicpath):
    song = musicpath + mp3
    process = lambda yesorno, name : open('songs/%s/' % yesorno + '/' + name, 'wb').write(open(song, 'rb').read())
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
        tags.save()
        process('taggeds', tags.artist + ' - ' + tags.title + '.mp3')
        remove(song)            
    except AttributeError: 
        if splitext(mp3)[1] in ['.mp3', '.MP3', '.Mp3']:
            process('untaggeds', mp3)
            remove(song)
            input('> El archivo (%s) presenta problemas y no se puede taggear, encuentralo en songs/untaggeds/' % mp3)
        else:
            remove(song)