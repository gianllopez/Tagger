from tkinter import Toplevel, Canvas, PhotoImage, Label, StringVar, Entry, Radiobutton, Button
from taglogic import changecoverfunction, intbtns
from tkinter.messagebox import showinfo
def changecover(songalbum, imgbtn2, btnslist):
    caroot = Toplevel()
    intbtns('disabled', btnslist, caroot)
    caroot.title('Tagger - xxxxx') # songalbum
    caroot.geometry('500x250')
    caroot.resizable(0,0)
    cacanvas = Canvas(caroot, bd=2, relief='raised')
    cacanvas.pack(fill='both', expand=1)
    background = PhotoImage(file='gui/imgs-data/backgrounds/ccbg.png')
    cacanvas.create_image(0, 0, anchor='nw', image=background)
    Label(cacanvas, text=' Cambio de Cover ', font=('Bahnschrift', 17), width=38, bg='white').grid(row=0, column=0, pady=10, columnspan=3)
    rbtnvar = StringVar(value='pc')
    pathvar = StringVar()
    pathentry = Entry(cacanvas, textvariable=pathvar, font=('Bahnschrift', 13), width=35)
    pathentry.grid(row=1, column=1, sticky='w')
    Radiobutton(cacanvas, text='En la PC:', font=('Bahnschrift', 13), bg='white', variable=rbtnvar, width=10, value='pc', command=lambda:pathentry.grid(row=1, column=1, sticky='w')).grid(row=1, column=0, pady=15)
    Radiobutton(cacanvas, text='En la Web:', font=('Bahnschrift', 13), bg='white', variable=rbtnvar, width=10, value='web', command=lambda:pathentry.grid(row=2, column=1, sticky='w')).grid(row=2, column=0, pady=15)
    helpicon = PhotoImage(file='gui/imgs-data/icons/help.png')
    changeicon = PhotoImage(file='gui/imgs-data/icons/change.png')
    changebtn = Button(cacanvas, image=changeicon, width=40, height=40, bg='white', command=lambda:changecoverfunction(songalbum, rbtnvar, changebtn, pathvar, imgbtn2, btnslist, caroot))
    changebtn.grid(row=3, column=1)
    Button(cacanvas, image=helpicon, width=40, height=40, bg='white', command=lambda:showinfo('Tagger - Ayuda', 'Si tienes el cover ya descargado en tu PC, selecciona tal opción y copias y pegas la ruta del cover (recuerda que este tiene que estar en formato .PNG) y en caso de que lo quieras de la web, los buscas y lo pasas a una nueva ventana (CLICK DERECHO + ABRIR IMAGEN EN UNA NUEVA PESTAÑA) copias el link, lo pegas y presionas el botón aplicar.')).grid(row=3, column=0)
    caroot.protocol('WM_DELETE_WINDOW', lambda:intbtns('normal', btnslist, caroot))
    caroot.mainloop()