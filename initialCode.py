# Pre made Libraries
import time
from tkinter import *
from tkinter import ttk
from tktooltip import ToolTip
from random import randint
from threading import Timer
from tkinter import messagebox, Tk
from PIL import ImageTk, Image

# Custom Files
from ApplicationFunctions import Application
from DrawingFunction import drawShit
from Login import LoginWindowNew
from RandomizeStyle import randomizeStyle, resetStyle
from SecondaryWindow import PersistentSecondaryWindow, SecondaryWindow
from Advertisement import display_advertisement


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, width=150)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(column=0, row=0)
        scrollbar.grid(column=1, row=0)


class SettingsWindow(PersistentSecondaryWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(400, 500, "Settings", False, "#282828", "./icons/settings.png", *args, **kwargs)


class MeatWindow(SecondaryWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(root.winfo_screenwidth(), root.winfo_screenheight(), "MEAT", False, "#282828", "./icons/lmr.png", *args, **kwargs)
        resize_photo = Image.open("./icons/lmr.png")
        photo = ImageTk.PhotoImage(resize_photo.resize((root.winfo_screenwidth(), root.winfo_screenheight())))
        photo_label = Label(self, image=photo)
        photo_label.image = photo
        photo_label.pack(fill=BOTH, expand=YES)
        self.withdraw()


def colorSlider(color):
    global red, green, blue, app, imgLabel
    # The CORRECT way
    # match color:
    #     case 'red':
    #         affectedColor = red.get()
    #     case 'green':
    #         affectedColor = green.get()
    #     case 'blue':
    #         affectedColor = blue.get()
    #     case _:
    #         affectedColor = 255

    # The WRONG way
    if color == 'red':
        affectedColor = red.get()
    elif color == 'green':
        affectedColor = green.get()
    elif color == 'blue':
        affectedColor = blue.get()
    else:
        affectedColor = 255

    app.compiledLayers[app.selectedLayer][1] = app.colorControllers[app.selectedLayer][
        app.selectedColorSpace].updateColor(affectedColor, color)
    app.layers[app.selectedLayer] = app.compiledLayers[app.selectedLayer][1]
    app.renderImage(imgLabel)
    return


def toggleOrientation():
    global app, showOrientationLabel
    app.toggleOrientation()
    if (app.orientationIsVertical):
        showOrientationLabel.config(text="Vertical")
    else:
        showOrientationLabel.config(text="Horizontal")
    return


def showOption(event=None):
    global lastUpdated
    option = toolOptionsVar.get()
    option_list = []
    index = 0
    # Removes the elements currently being displayed in
    for i in lastUpdated:
        i.grid_forget()
    if option == "addLine":  # If the selected tool is the addLine function
        global addLineToolOptions  # List of elements associated with addLine
        option_list = addLineToolOptions
    elif option == "brushTool":  # If the selected tool is the brushTool
        global brushToolOptions
        option_list = brushToolOptions
    elif option == "blur":  # If the selected tool is the blur tool
        global blurToolOptions
        option_list = blurToolOptions
    for i in option_list:  # Displays elements within notebook
        i.grid(column=1, row=index, sticky="WENS")
        index += 1
    lastUpdated = option_list  # Keeps track of the selected tool


def open_settings_window():
    if not SettingsWindow.alive:  # creates a new window if the settings window is not open
        root.settings_window = SettingsWindow()
    else:  # if it is open bring it into focus
        root.settings_window.focus()


def open_login_window():
    if not LoginWindowNew.alive:
        root.login_window = LoginWindowNew(app)
    else:
        root.login_window.focus()


def set_theme():
    option = app.theme_var.get()

    ttkFrameSide = [left_frame, right_frame, notebook_frame, layer_controls_frame]
    ttkFrameOptions = [color_notebook_frame, option_notebook_frame, gaussian_frame, box_frame, median_frame, ]
    ttkFrameMain = [middle_frame]

    ttkLabels = [orientationLabel, showOrientationLabel, RedLabel, GreenLabel, BlueLabel, selectedLayerLabel]
    ttkNotebook = [upper_notebook, lower_notebook]
    ttkButtons = [quitButton, drawShitButton, addLineButton, orientationToggleButton, removeLayerButton]
    menu = [fileTab, editTab]

    # These styles don't change based on theme
    # style.configure("TButton", relief="flat")
    style.configure("TNotebook.Tab", font=("Helvetica", 10))

    resetStyle(option, "Side.TFrame", ttkFrameSide)
    resetStyle(option, "Options.TFrame", ttkFrameMain)
    resetStyle(option, "Main.TFrame", ttkFrameOptions)

    resetStyle(option, "TTKNotebook", ttkNotebook)
    resetStyle(option, "TTKLabel", ttkLabels)
    resetStyle(option, "TTKButton", ttkButtons)
    resetStyle(option, "Menu", menu)

    # if option == 0:  # Dark theme
    #     # Dark Theme Colors: #121212, #282828, #3f3f3f, #575757, #717171, #8b8b8b

    #     style.configure("Side.TFrame", background="#282828")
    #     style.configure("Options.TFrame", background="#575757")
    #     style.configure("Main.TFrame", background="#121212")
    #     style.configure("TLabel", background="#575757", font=('Helvetica', 12), foreground="white", **label_paddings)
    #     style.configure("TNotebook", background="#3f3f3f")
    # elif option == 1:  # Light theme
    #     # Light Theme Colors: #E9EFF3, C9CED2, C0C7CB B3B8BB

    #     style.configure("Side.TFrame", background="#C9CED2")
    #     style.configure("Options.TFrame", background="#C0C7CB")
    #     style.configure("Main.TFrame", background="#E9EFF3")
    #     style.configure("TLabel", background="#C0C7CB", foreground="black", font=('Helvetica', 12), **label_paddings)
    #     style.configure("TNotebook", background="#B3B8BB")

# Passes the window size parameters and calls the drawing function
def drawShitDriver():
    # API_KEY = 'live_g3H406XGWmpTltKYtlPAqr2WiPKEQ6YM19r6mVEYkWNg3G8PATxL95JMHKqIA2hv'

    H = app.baseImageHeight
    W = app.baseImageWidth
    tmpimg = drawShit(H, W, app.getImg())
    app.addLayer(tmpimg)
    app.renderImage(imgLabel)


def randomStyle():
    # Separate ttkFrames
    ttkFrameSide = [left_frame, right_frame, notebook_frame, layer_controls_frame]
    ttkFrameOptions = [color_notebook_frame, option_notebook_frame, gaussian_frame, box_frame, median_frame, ]
    ttkFrameMain = [middle_frame]

    ttkFrame = [color_notebook_frame, layer_notebook_frame, option_notebook_frame, left_frame, middle_frame,
                right_frame, notebook_frame, layer_controls_frame]
    ttkLabels = [orientationLabel, showOrientationLabel, RedLabel, GreenLabel, BlueLabel, selectedLayerLabel]
    ttkNotebook = [upper_notebook, lower_notebook]
    ttkButtons = [quitButton, drawShitButton, addLineButton, orientationToggleButton, removeLayerButton,
                  removeLayerButton]
    menu = [fileTab, editTab]

    randomizeStyle("TTKFrame", ttkFrame)
    # randomizeStyle("Side.TFrame", ttkFrameSide)
    # randomizeStyle("Main.TFrame", ttkFrameMain)
    # randomizeStyle("Options.TFrame", ttkFrameOptions)
    randomizeStyle("TTKNotebook", ttkNotebook)
    randomizeStyle("TTKLabel", ttkLabels)
    randomizeStyle("TTKButton", ttkButtons)
    randomizeStyle("Menu", menu)


def keybind_validate(keybind, event=None):
    if app.logged_in:
        if keybind == "fullscreen":
            app.isFullScreen = not app.isFullScreen
            root.attributes("-fullscreen", app.isFullScreen)
        elif keybind == "theme1":
            app.theme_var.set(0)
            set_theme()
        elif keybind == "theme2":
            app.theme_var.set(1)
            set_theme()
        elif keybind == "brush":
            toolOptionsVar.set("brushTool")
            showOption()
    else:
        open_login_window()


# Thread cleanup function, called on window close
def cleanup():
    if messagebox.askokcancel("Please Don't Quit, Pretty Please, Like Really Pretty Please", "Are you sure you want to quit?"):
        app.thread.cancel()
        root.destroy()


root = Tk()

lastUpdated = []  # Keeps track of the options shit

root.title("Bad Photoshop")

# Cleans up threads so we don't have errors on program close
root.protocol("WM_DELETE_WINDOW", cleanup)

# root.wm_iconphoto(False, PhotoImage(file=r".\icons\lmr.png"))

root.resizable(width=True, height=True)  # Allows the screen to be resized

working_pane = PanedWindow(root, orient=HORIZONTAL,
                           background="#717171")  # Need to use paned windows for adjustable frames
working_pane.pack(expand=True, fill=BOTH)

# -----------------Style-------------------
style = ttk.Style(root)

label_paddings = {'padx': 0, 'pady': 2}

# -------------------Frame-------------------
left_frame = ttk.Frame(working_pane, width=85, style="Side.TFrame", padding=10)
middle_frame = ttk.Frame(working_pane, width=600, padding=10, style="Main.TFrame")
right_frame = ttk.Frame(working_pane, width=180, padding=10, style="Side.TFrame")
notebook_frame = ttk.Frame(right_frame, style="Side.TFrame")  # Might be redundant
layer_controls_frame = ttk.Frame(right_frame, style="Side.TFrame")

# -----------------Notebooks-------------------
upper_notebook = ttk.Notebook(notebook_frame)
color_notebook_frame = ttk.Frame(upper_notebook, width=175, height=150, style="Options.TFrame")

lower_notebook = ttk.Notebook(notebook_frame)
layer_notebook_frame = ttk.Frame(lower_notebook, width=175, height=200)
scroll_frame = ScrollableFrame(layer_notebook_frame)

option_notebook_frame = ttk.Frame(lower_notebook, width=175, height=200, style="Options.TFrame")

gaussian_frame = ttk.Frame(option_notebook_frame, style="Options.TFrame")
box_frame = ttk.Frame(option_notebook_frame, style="Options.TFrame")
median_frame = ttk.Frame(option_notebook_frame, style="Options.TFrame")

selectedLayerLabel = ttk.Label(layer_controls_frame, text="0")  # This needs to be declared before app

# -------------Create Application Object-----------
app = Application(root, right_frame, scroll_frame.scrollable_frame, selectedLayerLabel, False)

# -------------------Menu-------------------
menuBar = Menu(root, relief="flat")  # Creates the menu bar at the top of the screen

# Commands for creating and filling the file tab
fileTab = Menu(menuBar, tearoff=False,
               relief="flat")  # Creates the file tab, if want the menu to be movable set tearoff = True

# Creates the commands under the file tab
fileTab.add_command(label="Log In", command=open_login_window)
fileTab.add_separator()
fileTab.add_command(label="New (N/A)", command=None)
fileTab.add_command(label="Open", command=lambda: app.setBaseImage(red, green, blue, imgLabel))
fileTab.add_command(label="Save", command=app.saveImage)
fileTab.add_command(label="Save as", command=app.saveImgAs)
fileTab.add_command(label="Settings", command=open_settings_window)
fileTab.add_separator()
fileTab.add_command(label="Exit", command=root.quit)

# Commands for creating and filling the edit tab
editTab = Menu(menuBar, tearoff=False)

# Creates the commands under the edit tab
editTab.add_command(label="Undo (N/A)")
editTab.add_command(label="Redo (N/A)")

# Commands for changing the style of the program
styleTab = Menu(menuBar, tearoff=False)

# Submenus for Style Tab
themeTab = Menu(styleTab, tearoff=False)
themeTab.add_radiobutton(label="Dark Theme", variable=app.theme_var, value=0, command=set_theme)
themeTab.add_radiobutton(label="Light Theme", variable=app.theme_var, value=1, command=set_theme)
themeTab.add_separator()
themeTab.add_command(label="Random Colors :) (N/A)", command=randomStyle)

# Creates the commands under the style tab
styleTab.add_cascade(label="Themes", menu=themeTab)

# Adds the individual tabs to the toolbar
menuBar.add_cascade(label="File", menu=fileTab)
menuBar.add_cascade(label="Edit", menu=editTab)
menuBar.add_cascade(label="Style", menu=styleTab)
root.config(menu=menuBar)

# ----------------Labels---------------------
imgLabel = ttk.Label(middle_frame)

orientationLabel = ttk.Label(option_notebook_frame, text="Orientation:")

showOrientationLabel = ttk.Label(option_notebook_frame, text="Horizontal")

RedLabel = ttk.Label(color_notebook_frame, text="Red")

GreenLabel = ttk.Label(color_notebook_frame, text="Green")

BlueLabel = ttk.Label(color_notebook_frame, text="Blue")

layerLabel = ttk.Label(layer_controls_frame, text="Selected Layer: ")

gaussian_label = ttk.Label(gaussian_frame, text="Gaussian")

box_label = ttk.Label(box_frame, text="Box")

median_label = ttk.Label(median_frame, text="Median")

# ----------------Button-----------------
quitButton = ttk.Button(right_frame, text="Exit", command=root.quit)

drawShitButton = ttk.Button(option_notebook_frame, text="Paint Brush", command=drawShitDriver)

addLineButton = ttk.Button(option_notebook_frame, text="Add Line", command=lambda: app.addLine(addLinePixel, imgLabel))

orientationToggleButton = ttk.Button(option_notebook_frame, text="Toggle", command=toggleOrientation)

changeLineColorButton = ttk.Button(option_notebook_frame, text="Change Color", command=lambda: app.changeLineColor())

removeLayerButton = ttk.Button(layer_controls_frame, text="Remove Layer", command=lambda: app.removeLayer(imgLabel))

blurType = StringVar()  # Type of blur for the blur, used for radio buttons
gaussianBlurButton = ttk.Radiobutton(gaussian_frame, variable=blurType, value="gaussian")
boxBlurButton = ttk.Radiobutton(box_frame, variable=blurType, value="box")
medianBlurButton = ttk.Radiobutton(median_frame, variable=blurType, value="median")

# If the changes are not confirmed, they will be discarded when another edit is made.
confirmBlurChangesButton = ttk.Button(option_notebook_frame, text="Confirm Changes",
                                      command=lambda: app.confirmBlurChanges(blurType.get(), blurSlider.get(),
                                                                             imgLabel))

# ----------------Text Fields---------------------
addLinePixel = Entry(option_notebook_frame)

# -----------------Slider-------------------
red = Scale(color_notebook_frame, from_=1, to=255, orient=HORIZONTAL)
red.configure(background="#D95757", foreground="white", font=("Helvetica", 8, "bold"), highlightbackground="#575757",
              sliderrelief="flat", sliderlength=7)
red.bind('<B1-Motion>', lambda r: colorSlider('red'))

green = Scale(color_notebook_frame, from_=1, to=255, orient=HORIZONTAL)
green.configure(background="#70BE7C", foreground="white", font=("Helvetica", 8, "bold"), highlightbackground="#575757",
                sliderrelief="flat", sliderlength=7)
green.bind('<B1-Motion>', lambda g: colorSlider('green'))

blue = Scale(color_notebook_frame, from_=1, to=255, orient=HORIZONTAL)
blue.configure(background="#6257D9", foreground="white", font=("Helvetica", 8, "bold"), highlightbackground="#575757",
               sliderrelief="flat", sliderlength=7)
blue.bind('<B1-Motion>', lambda b: colorSlider('blue'))

blurSlider = Scale(option_notebook_frame, from_=1, to=7, orient=HORIZONTAL,
                   command=lambda f: app.blurImg(blurType.get(), f, imgLabel))
blurSlider.configure(background="#6257D9", foreground="white", font=("Helvetica", 8, "bold"),
                     highlightbackground="#575757",
                     sliderrelief="flat", sliderlength=7)

# -----------------Toolbar-------------------
# Holds the option value
toolOptionsVar = StringVar()

# Icons for the radio buttons
tkAddLineImage = PhotoImage(file="./icons/add_line_icon.png")  # Add Line tool unselected
tkAddLineImageSelected = PhotoImage(file="./icons/add_line_icon_selected.png")  # Add Line tool selected

tkBrushImage = PhotoImage(file="./icons/brush_icon.png")  # Brush Tool unselected
tkBrushImageSelected = PhotoImage(file="./icons/brush_icon_selected.png")  # Brush Tool selected

tkBlur = PhotoImage(file="./icons/blur_icon.png")
tkBlurSelected = PhotoImage(file="./icons/blur_icon_selected.png")

# Creates the style map for images and backgrounds used in the radio button
base_style_design = [('selected', "#575757"), ('active', "#575757"), ('!disabled', "#3f3f3f")]
style.map("addLineDesign.Toolbutton", image=[('selected', tkAddLineImageSelected), ('active', tkAddLineImageSelected),
                                             ('!disabled', tkAddLineImage)], background=base_style_design)
style.map("brushDesign.Toolbutton",
          image=[('selected', tkBrushImageSelected), ('active', tkBrushImageSelected), ('!disabled', tkBrushImage)],
          background=base_style_design)
style.map("blurDesign.Toolbutton",
          image=[('selected', tkBlurSelected), ('active', tkBlurSelected), ('!disabled', tkBlur)],
          background=base_style_design)

# base_style.configure("base_style.addLineDesign.Toolbutton", width=20)

# List of options for each tool
addLineToolOptions = [showOrientationLabel, orientationToggleButton, addLinePixel, addLineButton, changeLineColorButton]
brushToolOptions = [drawShitButton]
blurToolOptions = [blurSlider, gaussian_frame, box_frame, median_frame, confirmBlurChangesButton]

# The radio button that represents the tool
addLineToolButton = ttk.Radiobutton(left_frame, command=showOption, variable=toolOptionsVar, value="addLine",
                                    style="style.addLineDesign.Toolbutton")
brushToolButton = ttk.Radiobutton(left_frame, command=showOption, variable=toolOptionsVar, value="brushTool",
                                  style="style.brushDesign.Toolbutton")
blurToolButton = ttk.Radiobutton(left_frame, command=showOption, variable=toolOptionsVar, value="blur",
                                 style="style.blurDesign.Toolbutton")

# Tooltip for the radio buttons
ToolTip(addLineToolButton, msg="Add Line Tool")
ToolTip(brushToolButton, msg="Brush Tool")
ToolTip(blurToolButton, msg="Blur Tool")
ToolTip(quitButton, msg="Quit", delay=0)

# -----------------Canvas Management-------------------
app.setBaseImage(red, green, blue, imgLabel)

root.rowconfigure(1, weight=1)

left_frame.grid(column=0, row=1, sticky="WENS")
middle_frame.grid(column=1, row=1, sticky="WENS")
right_frame.grid(column=2, row=1, sticky="WENS")

notebook_frame.grid(column=0, row=0, sticky="WENS")

notebook_frame.rowconfigure(0, weight=1, pad=10)
notebook_frame.rowconfigure(1, weight=1, pad=10)
notebook_frame.columnconfigure(0, weight=1)
notebook_frame.columnconfigure(1, weight=1)
notebook_frame.columnconfigure(2, weight=1)

left_frame.grid_propagate(False)
middle_frame.grid_propagate(True)
right_frame.grid_propagate(False)

color_notebook_frame.grid_propagate(False)
layer_notebook_frame.grid_propagate(False)
option_notebook_frame.grid_propagate(False)

# Centers the picture
middle_frame.columnconfigure(0, weight=1)
middle_frame.rowconfigure(0, weight=1)
imgLabel.grid(column=0, row=0)

# Positions items in the left frame
addLineToolButton.grid(column=0, row=0)
brushToolButton.grid(column=1, row=0)
blurToolButton.grid(column=0, row=1)
left_frame.columnconfigure((0, 1), pad=10)
left_frame.rowconfigure((0, 1), pad=10)

# Positions items in the right frame
quitButton.grid(column=0, row=10)

RedLabel.grid(column=0, row=1)
red.grid(column=1, row=1)

GreenLabel.grid(column=0, row=2)
green.grid(column=1, row=2)

BlueLabel.grid(column=0, row=3)
blue.grid(column=1, row=3)
scroll_frame.grid(column=0, row=0)

layer_controls_frame.grid(column=1, row=0)

removeLayerButton.grid(row=1, column=0)
layerLabel.grid(row=0, column=0)
selectedLayerLabel.grid(row=0, column=1)

gaussianBlurButton.grid(row=0, column=0)
gaussian_label.grid(row=0, column=1)

boxBlurButton.grid(row=0, column=0)
box_label.grid(row=0, column=1)

medianBlurButton.grid(row=0, column=0)
median_label.grid(row=0, column=1)

# Creates the window using each frame
working_pane.add(left_frame)
working_pane.add(middle_frame)
working_pane.add(right_frame)

upper_notebook.add(color_notebook_frame, text="Colors")

lower_notebook.add(layer_notebook_frame, text="Layers")
lower_notebook.add(option_notebook_frame, text="Options")

upper_notebook.grid(column=0, row=0)
lower_notebook.grid(column=0, row=1)

upper_notebook.columnconfigure(0, weight=1)
lower_notebook.columnconfigure(0, weight=1)

color_notebook_frame.columnconfigure(0, pad=10)
color_notebook_frame.rowconfigure((0, 1, 2), pad=10)

# -------------------Keybinds-------------------

root.bind("<Control-o>",
          lambda x: app.setBaseImage(red, green, blue, imgLabel) if app.logged_in else open_login_window())
root.bind("<F11>", lambda x: keybind_validate("fullscreen"))
root.bind("<Control-Key-1>", lambda x: keybind_validate("theme1"))
root.bind("<Control-Key-2>", lambda x: keybind_validate("theme2"))
root.bind("<Control-b>", lambda x: keybind_validate("brush"))
root.bind("<Control-s>", lambda x: app.saveImage if app.logged_in else open_login_window())
root.bind("<Control-S>", lambda x: app.saveImgAs if app.logged_in else open_login_window())

set_theme()

if not app.logged_in:
    app.thread = Timer(randint(5, 30), lambda: display_advertisement(app, root.winfo_screenwidth(), root.winfo_screenheight()))
    app.thread.start()

root.mainloop()
