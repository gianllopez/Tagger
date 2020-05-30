try:
    try:
        from changecover import changecover
        from taglogic.mainlogic import nextsong, savetags
        from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, StringVar
        from os import listdir
        from random import choice
        root = Tk()
        root.title('Tagger - ¡Taggea tus canciones!')
        root.geometry('540x500')
        root.resizable(0, 0)
        canvas = Canvas(root)
        canvas.pack(fill='both', expand=True)
        bgpath = 'gui/imgs-data/backgrounds/'
        bgs = listdir(bgpath)
        bgs.remove('ccbg.png')
        background = PhotoImage(file=bgpath + choice(bgs))
        canvas.create_image(0, 0, anchor='nw', image=background)
        titlesv = StringVar()
        artistsv = StringVar()
        albumsv = StringVar()
        genresv = StringVar()
        dictvars = {'Título' : titlesv, 'Artista' : artistsv, 'Álbum' : albumsv, 'Género' : genresv}
        i = 0
        for x in dictvars:
            Label(canvas, text=x + ':', font=('Bahnschrift', 15), width=7, bg='white').grid(row=i, column=0, padx=10, pady=15)
            Entry(canvas, textvariable=dictvars[x], font=('Bahnschrift', 14), width=20).grid(row=i, column=1, padx=5, pady=15, columnspan=2)
            i += 1
        saveicon = PhotoImage(file='gui/imgs-data/icons/save.png')
        savebtn = Button(canvas, bg='white', image=saveicon, width=45, height=45, command=lambda:savetags(dictvars, coverbtn))
        savebtn.grid(row=4, column=1)
        nexticon = PhotoImage(file='gui/imgs-data/icons/next.png')
        nextbtn = Button(canvas, bg='white', image=nexticon, width=45, height=45, command=lambda:nextsong(dictvars, coverbtn))
        nextbtn.grid(row=4, column=2)
        cvplace = PhotoImage(file='gui/imgs-data/icons/acplace.png')
        coverbtn = Button(canvas, image=cvplace, height=203, width=201, command=lambda:changecover(albumsv.get(), coverbtn, [savebtn, nextbtn, coverbtn] ))
        coverbtn.grid(row=0, column=3, padx=5, pady=15, rowspan=4)
        Label(canvas, text='GLAX Copyrights © 2020', font=('Bahnschrift', 15), width=50, bg='white').place(x=0, y=455)
        root.mainloop()
    except ModuleNotFoundError:
        print('- El programa con GUI no se puede ejecutar debido a la ausencia de una dependencia (PIL/Pillow)\n> Prueba a ejecutar en la terminal: pip install PIL o con pip install Pillow.')
except IndexError:
    print('- La rutas en user-music-path.txt no son correctas, recuerda que tienen que estar en formato: ruta de la música, ruta de exportación.')