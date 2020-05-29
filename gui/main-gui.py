try:
    try:
        from changecover import changecover
        from taglogic.mainlogic import nextsong, savetags
        from tkinter import *
        mainroot = Tk()
        mainroot.title('Tagger - ¡Taggea tus canciones!')
        mainroot.geometry('621x350')
        mainroot.resizable(0,0)
        mainframe = Frame(mainroot, bd=5, relief='raised')
        mainframe.pack(fill='both', expand=1)
        titlevar = StringVar()
        artistvar = StringVar()
        genrevar = StringVar()
        albumvar = StringVar()
        usermetas = {'Título' : titlevar, 'Artista' : artistvar, 'Género' : genrevar, 'Álbum' : albumvar}
        i = 0
        for var in usermetas:
            Label(mainframe, text=var + ':', font=('Trebuchet MS', 15)).grid(row=i, column=0, padx=5, pady=5)
            Entry(mainframe, width=30, textvariable=usermetas[var], font=('Trebuchet MS', 12)).grid(row=i, column=1, padx=5, pady=5, columnspan=2)
            i += 1
        savebtn = Button(mainframe, text='< Guardar >', font=('Trebuchet MS', 10), command=lambda:savetags(usermetas))
        savebtn.grid(row=5, column=1, padx=5)
        nextbtn = Button(mainframe, text='Siguiente >', font=('Trebuchet MS', 10), command=lambda:nextsong(usermetas, imgbtn))
        nextbtn.grid(row=5, column=2, padx=5)
        acpimg = PhotoImage(file='gui/imgs-data/acplace.png')
        imgbtn = Button(mainframe, width=250, height=250, image=acpimg, command=lambda:changecover(albumvar.get(), imgbtn, [savebtn, nextbtn, imgbtn]))
        imgbtn.grid(row=0, column=3,padx=5, pady=5, rowspan=6)
        Label(mainframe, text='GLAX © Copyright 2020', font=('Trebuchet MS', 10)).place(x=5, y=315)
        mainroot.mainloop()
    except ModuleNotFoundError:
        print('- El programa con GUI no se puede ejecutar debido a la ausencia de una dependencia (PIL/Pillow)\n> Prueba a ejecutar en la terminal: pip install PIL o con pip install Pillow.')
except IndexError:
    print('- La rutas en user-music-path.txt no son correctas, recuerda que tienen que estar en formato: ruta de la música, ruta de exportación.')