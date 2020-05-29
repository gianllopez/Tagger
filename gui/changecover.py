from taglogic import changecoverfunction, intbtns
from tkinter.messagebox import showinfo
from tkinter import *
from threading import Thread
def changecover(songalbum, imgbtn2, btnslist):
    caroot = Toplevel()
    intbtns('disabled', btnslist, caroot)
    caroot.title('Tagger - ' + songalbum)
    caroot.geometry('380x200')
    caroot.resizable(0,0)
    caframe = Frame(caroot, bd=5, relief='raised')
    caframe.pack(fill='both', expand=1)
    Label(caframe, text='¿Donde tienes el cover?' , font=('Trebuchet MS', 15)).grid(row=0, column=0, columnspan=2)
    rbtnvar = StringVar(value='web')
    pathvar = StringVar()
    pathentry = Entry(caframe, textvariable=pathvar, font=('Trebuchet MS', 10), width=34)
    pathentry.grid(row=2, column=1, sticky='w')
    Radiobutton(caframe, text='En la PC:', font=('Trebuchet MS', 12), variable=rbtnvar, value='pc', command=lambda:pathentry.grid(row=1, column=1, sticky='w')).grid(row=1, column=0, sticky='w', padx=5, pady=5)
    Radiobutton(caframe, text='En la Web:', font=('Trebuchet MS', 12), variable=rbtnvar, value='web', command=lambda:pathentry.grid(row=2, column=1, sticky='w')).grid(row=2, column=0, sticky='w', padx=5, pady=5)
    btn = Button(caframe, text='Aplicar >>', font=('Trebuchet MS', 12), width=26, command=lambda:changecoverfunction(songalbum, rbtnvar, btn, pathvar, imgbtn2, btnslist, caroot))
    btn.grid(row=3, column=1, pady=10)
    Button(caframe, text='Ayuda', font=('Trebuchet MS', 12), width=10, command=lambda:showinfo('Tagger - Ayuda', 'Si tienes el cover ya descargado en tu PC, selecciona tal opción y copias y pegas la ruta del cover (recuerda que este tiene que estar en formato .PNG) y en caso de que lo quieras de la web, los buscas y lo pasas a una nueva ventana (CLICK DERECHO + ABRIR IMAGEN EN UNA NUEVA PESTAÑA) copias el link, lo pegas y presionas el botón aplicar.')).grid(row=3, column=0, pady=10)
    caroot.protocol('WM_DELETE_WINDOW', lambda:intbtns('normal', btnslist, caroot))
    caroot.mainloop()