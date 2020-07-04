try:
    from taglogic import nextsong, savetags, TKBase
    from tkinter import Tk, Label, Entry, StringVar
    from changecover import change_cover
    from random import choice
    from os import listdir
    
    # random background selection.
    bgs = listdir(bgpath := 'img-content/backgrounds/')
    bgs.remove('ccbg.png')
    
    # main GUI window config.
    mainroot = Tk()
    maintkb = TKBase({
        'window' : {
            'variable' : mainroot,
            'title' : 'Tagger - ¡Taggea tus canciones!',
            'size' : { 'width' : 540, 'height' : 500 }
        },
        'canvas' : { 'image-background' : bgpath + choice(bgs) }
    })

    # main data variables and their order into a dictionarie.
    titlesv = StringVar()
    artistsv = StringVar()
    albumsv = StringVar()
    genresv = StringVar()
    dictvars = {'Título' : titlesv, 'Artista' : artistsv, 'Álbum' : albumsv, 'Género' : genresv}
    
    # for cycle that make the main entries and labels.
    i = 0
    for x in dictvars:
        Label(maintkb.canvas, text=x + ':', font=('Bahnschrift', 15), width=7, bg='white').grid(row=i, column=0, padx=10, pady=15)
        Entry(maintkb.canvas, textvariable=dictvars[x], font=('Bahnschrift', 14), width=20).grid(row=i, column=1, padx=5, pady=15, columnspan=2)
        i += 1
    
    # SAVE button config and creation.
    savebtncnf = {
        'btn-bg-image' : 'img-content/icons/save.png',
        'width' : 45,
        'height' : 45,            
        'grid' : { 'row' : 4, 'column' : 1 }
    }
    savebtn = maintkb.ButtonGen(savebtncnf)

    # NEXT button config and creation.
    nextbtncnf = savebtncnf.copy()
    nextbtncnf['btn-bg-image'] = 'img-content/icons/next.png'
    nextbtncnf['grid']['column'] = 2
    nextbtn = maintkb.ButtonGen(nextbtncnf)

    # CHANGE-COVER button config and creation.
    coverbtncnf = nextbtncnf.copy()
    coverbtncnf['btn-bg-image'] = 'img-content/icons/acplace.png'
    coverbtncnf['width'] = 201
    coverbtncnf['height'] = 203
    coverbtncnf['grid'] = { 'row' : 0, 'column' : 3, 'padding-x' : 5, 'padding-y' : 15, 'rows >>> to-take' : 4 }
    coverbtn = maintkb.ButtonGen(coverbtncnf)

    # commands to execute on click of the last three buttons. The x variable contains the default_album value.
    x = StringVar()
    savebtn['command'] = lambda:savetags(dictvars, coverbtn)
    nextbtn['command'] = lambda:nextsong(dictvars, coverbtn, x)
    coverbtn['command'] = lambda:change_cover(default_album=x.get(), coverbtndisplay=coverbtn)

    # Copyrights label.
    Label(maintkb.canvas, text='Copyrights © 2020', font=('Bahnschrift', 15), width=50).place(x=0, y=455)

    mainroot.mainloop()
except Exception:
    print('Algo estás haciendo mal, revisa la documentación y sigue los pasos de uso.', e)