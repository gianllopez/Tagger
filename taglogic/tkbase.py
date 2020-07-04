from tkinter import Canvas, PhotoImage, Button, Radiobutton

# main TKBase Class.
class TKBase:
    
    # main TKBase constructor.
    def __init__(self, config):        
    
        # set te default window configuration adding just the posibility to change the usual options.
        root_config = config['window']
        self.root = root_config['variable']
        self.root.title(root_config['title'])
        self.root.geometry('{width}x{height}'.format(**root_config['size']))
        self.root.resizable(0, 0)

        # set the canvas configuration with the usual options too.
        canvas_config = config['canvas']
        self.canvas = Canvas(self.root, bd=canvas_config.get('border-width', 0), relief='raised')  
        background = PhotoImage(file=canvas_config['image-background'])
        self.canvas.create_image(0, 0, anchor='nw', image=background)
        self.canvas.background = background
        self.canvas.pack(fill='both', expand=True)

    # this function add to the given widget the options that have all the widgets.
    def globalSettings(self, config, widget):        

        # only this four.
        for x in (glob := { 'font' : 'font-style', 'height' : 'height', 'width' : 'width' }):
            widget[x] = config.get(glob[x], None)
        widget['bg'] = 'white'

        # add to the element the option to grid positioning.
        if 'grid' in config:
            grid = config['grid']
            return widget.grid(
                row = grid['row'], 
                column = grid['column'], 
                padx = grid.get('padding-x', 0), 
                pady = grid.get('padding-y', 0),
                columnspan = grid.get('columns >>> to-take', 1), 
                rowspan = grid.get('rows >>> to-take', 1),
                sticky = grid.get('sticky', None),
            )

        # add to the element the option to place positioning.
        if 'place' in config:
            place = config['place']
            return widget.place(x=place['x'], y=place['y'])   

    def ButtonGen(self, config):
        btn = Button(
            self.canvas, 
            text=config.get('text', None), 
        )    
        image = PhotoImage(file=config['btn-bg-image'])
        btn['image'] = image
        btn.image = image
        self.globalSettings(config=config, widget=btn)
        return btn

    def RadiobuttonGen(self, config):
        rbtn = Radiobutton(self.canvas,
            text=config['text'],
            variable=config['rbtn-var'],
            value=config['rbtn-value'],
            command=config['execute >>> on-click']
        )
        self.globalSettings(config=config, widget=rbtn)
        return rbtn