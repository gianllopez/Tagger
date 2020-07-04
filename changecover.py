from tkinter.messagebox import showinfo
from taglogic import TKBase, cctrigger
from tkinter import *

def change_cover(default_album, coverbtndisplay):

    # ChangeCover GUI's Window Config.  
    ccroot = Toplevel()

    ccroot.grab_set()

    cctkb = TKBase({
        'window' : {
            'size' : { 'width' : 500, 'height' : 250 },
            'title' : 'Tagger - ' + default_album,
            'variable' : ccroot,
        },
        'canvas' : { 'image-background' : 'img-content/backgrounds/ccbg.png' }
    })

    # GUI's Main Label.
    Label(cctkb.canvas, text='Cambio de Cover', font=('Bahnschrift', 17), width=38).grid(
        row=0, column=0, 
        pady=10, columnspan=3
    )

    # New Cover path Entry.
    pathvar = StringVar()
    pathentry = Entry(cctkb.canvas, textvariable=pathvar, width=35, font=('Bahnschrift', 13))
    pathentry.grid(row=1, column=1, sticky='w')

    # Path on PC option.
    rbtnvar = StringVar(value='PC')
    rbtnpccnf = {
        'execute >>> on-click' : lambda:pathentry.grid(row=1, column=1, sticky='w'),
        'grid' : { 'row' : 1, 'column' : 0, 'padding-y' : 15 },
        'font-style' : ('Bahnschrift', 13),
        'rbtn-var' : rbtnvar,
        'text' : 'En la PC',
        'rbtn-value' : 'PC',
        'width' : 10,
    }
    cctkb.RadiobuttonGen(rbtnpccnf)
    
    # Path on Web option
    rbtnwebcnf = rbtnpccnf.copy()
    rbtnwebcnf['text'] = 'En la Web'
    rbtnwebcnf['rbtn-value'] = 'WEB'
    rbtnwebcnf['grid']['row'] = 2
    rbtnwebcnf['execute >>> on-click'] = lambda:pathentry.grid(row=2, column=1, sticky='w')
    rbtnweb = cctkb.RadiobuttonGen(rbtnwebcnf)
    
    # Help button config.
    helpbtncnf = {
        'btn-bg-image' : 'img-content/icons/help.png',
        'grid' : { 'row' : 3, 'column' : 1 },
        'height' : 40,
        'width' : 40,
    }
    helptbn = cctkb.ButtonGen(helpbtncnf)
    helptbn['command'] = lambda:showinfo('Tagger - Ayuda', 'Si tienes el cover ya descargado en tu PC, selecciona tal opción y copias y pegas la ruta del cover (recuerda que este tiene que estar en formato .PNG) y en caso de que lo quieras de la web, los buscas y lo pasas a una nueva ventana (CLICK DERECHO + ABRIR IMAGEN EN UNA NUEVA PESTAÑA) copias el link, lo pegas y presionas el botón aplicar.', parent=ccroot),        

    # Button for trigger the song cover change.
    changebtncnf = helpbtncnf.copy()
    changebtncnf['btn-bg-image'] = 'img-content/icons/change.png'
    changebtncnf['grid']['column'] = 0
    changebtn = cctkb.ButtonGen(changebtncnf)

    data = {
        'default-album' : default_album,
        'path-stringvar' : pathvar, 
        'btn-for-showcover' : coverbtndisplay,
        'rbtn-stringvar' : rbtnvar,
        'main-parent' : ccroot
    }
    
    changebtn['command'] = lambda:cctrigger(reqdata=data)
    
    ccroot.mainloop()