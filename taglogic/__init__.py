# function that contain the logic of the change cover GUI.
from .cclogic import cctrigger 

# this functions are the base of the interaction with the user.
from .guilogic import nextsong, savetags 

# base utilities. 
from .utilities import (
    MUSICPATH, EXPATH, COVERSPATH, # user and cover paths constants.
    rmbytes, replchars # functions that transform the data for good manage and create the base dirs.
)

# module that summarize Tkinter and all his bullshit that don't respect the DRY logic.
from .tkbase import TKBase