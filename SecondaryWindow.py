from tkinter import *


# Creates a new window separate from the root window
# width : the pixel width of the screen
# height : the pixel height of the screen
# title : the title of the window as a string
# resizable : boolean value that determines whether the screen is resizable
# background : the hexcode of the background color as a string
# icon : file path of the window's icon as a string
class SecondaryWindow(Toplevel):
    def __init__(self, width, height, title, resizable, background, icon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(width=width, height=height, background=background)
        self.title(title)
        self.focus()
        self.resizable(width=resizable, height=resizable)
        self.wm_iconphoto(False, PhotoImage(file=icon))


# Creates a new secondary window that cannot have multiple copies
# If there is an attempt to open a new version of this window, this window will pull focus
# alive : boolean value that keeps track of whether the window is open or not
class PersistentSecondaryWindow(SecondaryWindow):
    alive = False

    def __init__(self, width, height, title, resizable, background, icon, *args, **kwargs):
        super().__init__(width, height, title, resizable, background, icon, *args, **kwargs)
        self.__class__.alive = True

    def destroy(self):  # overrides destroy, so we can open the window again in the future
        self.__class__.alive = False
        return super().destroy()
