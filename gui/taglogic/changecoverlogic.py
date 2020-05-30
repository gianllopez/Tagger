from .utilities import replchars, PhotoImage, intbtns
from urllib.request import urlopen, Request, URLError, HTTPError
from tkinter.messagebox import showinfo, showerror
from PIL import Image
def changecoverfunction(albumsv, rbtnvar, applybtn, pathvar, imgbtn1, btns, root):         
    def getpath(func):
        newcoverpath = 'gui/img-content/covers/' + replchars(albumsv) + '.png'
        if func == urlopen:
            towrite = func(Request(pathvar.get(), headers={'User-Agent' : 'Mozilla/5.0'})).read()
        else:
            towrite = func(pathvar.get(), 'rb').read()
        open(newcoverpath, 'wb').write(towrite)
        Image.open(newcoverpath).resize((203, 201)).save(newcoverpath, 'png')
        newimg = PhotoImage(file=newcoverpath)
        imgbtn1['image'] = newimg
        imgbtn1.image = newimg
    command = applybtn['command']
    if rbtnvar.get() == 'pc':
        try:
            command = getpath(open)
        except FileNotFoundError:
            showerror('Tagger - Cover no encontrado', 'Asegúrate que la ruta del cover que estás pasando es la correcta, ya que este no ha sido encontrado.')
    else:
        try:
            command = getpath(urlopen)
        except (URLError, HTTPError):
            showerror('Tagger - Error de red', 'La imagen no pudo ser descargada, asegúrate de estar conectado a internet o confirma si la URL que pasaste es correcta.')
        else:
            showinfo('Tagger - ' + albumsv, 'Cover actualizado exitosamente. No olvides guardar tags para aplicarlo.')
            intbtns('normal', btns, root)