# imports bases.
from tkinter.messagebox import showinfo, showerror
from urllib.request import urlopen, Request
from .utilities import replchars
from tkinter import PhotoImage
from PIL import Image

# code base.
def cctrigger(reqdata):         

    # this function examine the user way to give the new cover path and apply it to the old cover .png.
    def getpath(way):
        newcoverpath = 'img-content/covers/' + replchars(reqdata['default-album']) + '.png'
        path = reqdata['path-stringvar'].get()
        if way == 'WEB':
            towrite = urlopen(Request(path, headers={'User-Agent' : 'Mozilla/5.0'})).read()
        else:
            towrite = open(path, 'rb').read()
        open(newcoverpath, 'wb').write(towrite)
        Image.open(newcoverpath).resize((203, 201)).save(newcoverpath, 'png')
        newimg = PhotoImage(file=newcoverpath)
        coverbtn = reqdata['btn-for-showcover']
        coverbtn['image'] = newimg
        coverbtn.image = newimg

    # after of the last function, changes must to apply.
    try:
        if reqdata['rbtn-stringvar'].get() == 'PC':
            command = getpath(way='PC') 
        else:
            command  = getpath(way='WEB')
    # catch all the exceptions and just eval those who matter, if try doesn't raise any error, the else make his own.
    except Exception as error:
        name = error.__class__.__name__
        if name == 'FileNotFoundError':
            showerror('Tagger - Cover no encontrado', 'Asegúrate que la ruta del cover que estás pasando es la correcta, ya que este no ha sido encontrado.', parent=reqdata['main-parent'])
        if name in ('URLError', 'HTTPError'):
            showerror('Tagger - Error de red', 'La imagen no pudo ser descargada, asegúrate de estar conectado a internet o confirma si la URL que pasaste es correcta.', parent=reqdata['main-parent'])
    else:
        showinfo('Tagger - ' + reqdata['default-album'], 'Cover actualizado de manera exitosa, no olvides guardar tags para aplicarlo.')
        return command