from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import random

cursors = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "man", "mouse",
        "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "trek"]
font = ["System", "Terminal", "Fixedsys", "Modern", "Roman", "Script", "Courier", "MS Serif", "MS Sans Serif",
            "Small Fonts", "Bell Gothic Std Black", "Bell Gothic Std Light", "Eccentric Std", "Stencil Std",
            "Tekton Pro", "Tekton Pro Cond", "Tekton Pro Ext", "Trajan Pro", "Rosewood Std Regular",
            "Prestige Elite Std", "Poplar Std", "Orator Std", "OCR A Std", "Nueva Std Cond", "Minion Pro SmBd",
            "Minion Pro Med", "Minion Pro Cond", "Mesquite Std", "Lithos Pro Regular", "Kozuka Mincho Pro R",
            "@Kozuka Mincho Pro R", "Kozuka Mincho Pro M", "@Kozuka Mincho Pro M", "Kozuka Mincho Pro L",
            "@Kozuka Mincho Pro L", "Kozuka Mincho Pro H", "@Kozuka Mincho Pro H", "Kozuka Mincho Pro EL",
            "@Kozuka Mincho Pro EL", "Kozuka Mincho Pro B", "@Kozuka Mincho Pro B", "Kozuka Gothic Pro R",
            "@Kozuka Gothic Pro R", "Kozuka Gothic Pro M", "@Kozuka Gothic Pro M", "Kozuka Gothic Pro L",
            "@Kozuka Gothic Pro L", "Kozuka Gothic Pro H", "@Kozuka Gothic Pro H", "Kozuka Gothic Pro EL",
            "@Kozuka Gothic Pro EL", "Kozuka Gothic Pro B", "@Kozuka Gothic Pro B", "Hobo Std", "Giddyup Std",
            "Cooper Std Black", "Charlemagne Std", "Chaparral Pro", "Brush Script Std", "Blackoak Std", "Birch Std",
            "Adobe Garamond Pro", "Adobe Garamond Pro Bold", "Adobe Kaiti Std R", "@Adobe Kaiti Std R",
            "Adobe Heiti Std R", "@Adobe Heiti Std R", "Adobe Fangsong Std R", "@Adobe Fangsong Std R",
            "Adobe Caslon Pro", "Adobe Caslon Pro Bold", "Adobe Arabic", "Adobe Devanagari", "Adobe Hebrew",
            "Adobe Ming Std L", "@Adobe Ming Std L", "Adobe Myungjo Std M", "@Adobe Myungjo Std M", "Adobe Song Std L",
            "@Adobe Song Std L", "Kozuka Gothic Pr6N B", "@Kozuka Gothic Pr6N B", "Kozuka Gothic Pr6N EL",
            "@Kozuka Gothic Pr6N EL", "Kozuka Gothic Pr6N H", "@Kozuka Gothic Pr6N H", "Kozuka Gothic Pr6N L",
            "@Kozuka Gothic Pr6N L", "Kozuka Gothic Pr6N M", "@Kozuka Gothic Pr6N M", "Kozuka Gothic Pr6N R",
            "@Kozuka Gothic Pr6N R", "Kozuka Mincho Pr6N B", "@Kozuka Mincho Pr6N B", "Kozuka Mincho Pr6N EL",
            "@Kozuka Mincho Pr6N EL", "Kozuka Mincho Pr6N H", "@Kozuka Mincho Pr6N H", "Kozuka Mincho Pr6N L",
            "@Kozuka Mincho Pr6N L", "Kozuka Mincho Pr6N M", "@Kozuka Mincho Pr6N M", "Kozuka Mincho Pr6N R",
            "@Kozuka Mincho Pr6N R", "Letter Gothic Std", "Minion Pro", "Myriad Hebrew", "Myriad Pro",
            "Myriad Pro Cond", "Myriad Pro Light", "Rosewood Std Fill", "Marlett", "Arial", "Arabic Transparent",
            "Arial Baltic", "Arial CE", "Arial CYR", "Arial Greek", "Arial TUR", "Batang", "@Batang", "BatangChe",
            "@BatangChe", "Gungsuh", "@Gungsuh", "GungsuhChe", "@GungsuhChe", "Courier New", "Courier New Baltic",
            "Courier New CE", "Courier New CYR", "Courier New Greek", "Courier New TUR", "DaunPenh", "DokChampa",
            "Estrangelo Edessa", "Euphemia", "Gautami", "Vani", "Gulim", "@Gulim", "GulimChe", "@GulimChe", "Dotum",
            "@Dotum", "DotumChe", "@DotumChe", "Impact", "Iskoola Pota", "Kalinga", "Kartika", "Khmer UI", "Lao UI",
            "Latha", "Lucida Console", "Malgun Gothic", "@Malgun Gothic", "Mangal", "Meiryo", "@Meiryo", "Meiryo UI",
            "@Meiryo UI", "Microsoft Himalaya", "Microsoft JhengHei", "@Microsoft JhengHei", "Microsoft YaHei",
            "@Microsoft YaHei", "MingLiU", "@MingLiU", "PMingLiU", "@PMingLiU", "MingLiU_HKSCS", "@MingLiU_HKSCS",
            "MingLiU-ExtB", "@MingLiU-ExtB", "PMingLiU-ExtB", "@PMingLiU-ExtB", "MingLiU_HKSCS-ExtB",
            "@MingLiU_HKSCS-ExtB", "Mongolian Baiti", "MS Gothic", "@MS Gothic", "MS PGothic", "@MS PGothic",
            "MS UI Gothic", "@MS UI Gothic", "MS Mincho", "@MS Mincho", "MS PMincho", "@MS PMincho", "MV Boli",
            "Microsoft New Tai Lue", "Nyala", "Microsoft PhagsPa", "Plantagenet Cherokee", "Raavi", "Segoe Script",
            "Segoe UI", "Segoe UI Semibold", "Segoe UI Light", "Segoe UI Symbol", "Shruti", "SimSun", "@SimSun",
            "NSimSun", "@NSimSun", "SimSun-ExtB", "@SimSun-ExtB", "Sylfaen", "Microsoft Tai Le", "Times New Roman",
            "Times New Roman Baltic", "Times New Roman CE", "Times New Roman CYR", "Times New Roman Greek",
            "Times New Roman TUR", "Tunga", "Vrinda", "Shonar Bangla", "Microsoft Yi Baiti", "Tahoma",
            "Microsoft Sans Serif", "Angsana New", "Aparajita", "Cordia New", "Ebrima", "Gisha", "Kokila", "Leelawadee",
            "Microsoft Uighur", "MoolBoran", "Symbol", "Utsaah", "Vijaya", "Wingdings", "Andalus", "Arabic Typesetting",
            "Simplified Arabic", "Simplified Arabic Fixed", "Sakkal Majalla", "Traditional Arabic", "Aharoni", "David",
            "FrankRuehl", "Levenim MT", "Miriam", "Miriam Fixed", "Narkisim", "Rod", "FangSong", "@FangSong", "SimHei",
            "@SimHei", "KaiTi", "@KaiTi", "AngsanaUPC", "Browallia New", "BrowalliaUPC", "CordiaUPC", "DilleniaUPC",
            "EucrosiaUPC", "FreesiaUPC", "IrisUPC", "JasmineUPC", "KodchiangUPC", "LilyUPC", "DFKai-SB", "@DFKai-SB",
            "Lucida Sans Unicode", "Arial Black", "Calibri", "Cambria", "Cambria Math", "Candara", "Comic Sans MS",
            "Consolas", "Constantia", "Corbel", "Franklin Gothic Medium", "Gabriola", "Georgia", "Palatino Linotype",
            "Segoe Print", "Trebuchet MS", "Verdana", "Webdings", "Haettenschweiler", "MS Outlook", "Book Antiqua",
            "Century Gothic", "Bookshelf Symbol 7", "MS Reference Sans Serif", "MS Reference Specialty",
            "Bradley Hand ITC", "Freestyle Script", "French Script MT", "Juice ITC", "Kristen ITC",
            "Lucida Handwriting", "Mistral", "Papyrus", "Pristina", "Tempus Sans ITC", "Garamond", "Monotype Corsiva",
            "Agency FB", "Arial Rounded MT Bold", "Blackadder ITC", "Bodoni MT", "Bodoni MT Black",
            "Bodoni MT Condensed", "Bookman Old Style", "Calisto MT", "Castellar", "Century Schoolbook",
            "Copperplate Gothic Bold", "Copperplate Gothic Light", "Curlz MT", "Edwardian Script ITC", "Elephant",
            "Engravers MT", "Eras Bold ITC", "Eras Demi ITC", "Eras Light ITC", "Eras Medium ITC", "Felix Titling",
            "Forte", "Franklin Gothic Book", "Franklin Gothic Demi", "Franklin Gothic Demi Cond",
            "Franklin Gothic Heavy", "Franklin Gothic Medium Cond", "Gigi", "Gill Sans MT", "Gill Sans MT Condensed",
            "Gill Sans Ultra Bold", "Gill Sans Ultra Bold Condensed", "Gill Sans MT Ext Condensed Bold",
            "Gloucester MT Extra Condensed", "Goudy Old Style", "Goudy Stout", "Imprint MT Shadow", "Lucida Sans",
            "Lucida Sans Typewriter", "Maiandra GD", "OCR A Extended", "Palace Script MT", "Perpetua",
            "Perpetua Titling MT", "Rage Italic", "Rockwell", "Rockwell Condensed", "Rockwell Extra Bold",
            "Script MT Bold", "Tw Cen MT", "Tw Cen MT Condensed", "Tw Cen MT Condensed Extra Bold", "Algerian",
            "Baskerville Old Face", "Bauhaus 93", "Bell MT", "Berlin Sans FB", "Berlin Sans FB Demi",
            "Bernard MT Condensed", "Bodoni MT Poster Compressed", "Britannic Bold", "Broadway", "Brush Script MT",
            "Californian FB", "Centaur", "Chiller", "Colonna MT", "Cooper Black", "Footlight MT Light",
            "Harlow Solid Italic", "Harrington", "High Tower Text", "Jokerman", "Kunstler Script", "Lucida Bright",
            "Lucida Calligraphy", "Lucida Fax", "Magneto", "Matura MT Script Capitals", "Modern No. 20",
            "Niagara Engraved", "Niagara Solid", "Old English Text MT", "Onyx", "Parchment", "Playbill", "Poor Richard",
            "Ravie", "Informal Roman", "Showcard Gothic", "Snap ITC", "Stencil", "Viner Hand ITC", "Vivaldi",
            "Vladimir Script", "Wide Latin", "Century", "Wingdings 2", "Wingdings 3", "Arial Unicode MS",
            "@Arial Unicode MS", "Arial Narrow", "Rupee Foradian", "Rupee", "DevLys 010", "Calibri Light", "Monoton",
            "Ubuntu Medium", "Ubuntu", "Ubuntu Light", "Yatra One", "HelvLight", "Lato", "Great Vibes"]
ttkButtonStyles = ["primary", "secondary", "success", "info", "warning", "danger"]

label_paddings = {'padx': 0, 'pady': 2}

c = lambda: random.randint(0, 19)
d = lambda: random.randint(1, 5)
d2 = lambda: random.randint(1, 3)
f = lambda: random.randint(0, 418)
s = lambda: random.randint(9, 20)
b = lambda: random.randint(0, 5)

def randomizeColor():
    r = lambda: random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r(), r(), r())

def randomLabelStyle(label):
    for i in label:
        i.config(bg=randomizeColor(), fg=randomizeColor(), bd=d(), cursor=cursors[c()], font=(font[f()], s()))

def randomButtonStyle(button):
    for i in button:
        i.config(bg=randomizeColor(), fg=randomizeColor(), activebackground=randomizeColor(), activeforeground=randomizeColor(), bd=d(), font=(font[f()], s()))

def randomSliderStyle(slider):
    for i in slider:
        i.config(bg=randomizeColor(), fg=randomizeColor(), activebackground=randomizeColor(), highlightbackground=randomizeColor())

def randomizeStyle(object, group):
    j = 0
    style = ttk.Style()

    # The CORRECT way
    # match object:
    #     case "TTKFrame":
    #         for i in group:
    #             style.configure("Random{0}.TFrame".format(j), background=randomizeColor(), cursor=cursors[c()], padding=c())
    #             i.config(style="Random{0}.TFrame".format(j))
    #             j += 1
    #     case "TTKNotebook":
    #         for i in group:
    #             style.configure("Random{0}.TNotebook".format(j), background=randomizeColor(), bordercolor=randomizeColor())
    #             i.config(style="Random{0}.TNotebook".format(j))
    #             j += 1
    #     case "TTKLabel":
    #         for i in group:
    #             style.configure("Random{0}.TLabel".format(j), background=randomizeColor(), forground=randomizeColor(), font=(font[f()], s()))
    #             i.config(style="Random{0}.TLabel".format(j))
    #             j += 1
    #     case "TTKButton":
    #         for i in group:
    #             style.configure("Random{0}.TButton".format(j), background=randomizeColor(), font=(font[f()], s()), relief="flat", padding=d2(), foreground=randomizeColor())
    #             i.config(style="Random{0}.TButton".format(j))
    #             j += 1
    #     case "Menu":
    #         for i in group:
    #             i.config(bg=randomizeColor(), fg=randomizeColor(), activebackground=randomizeColor(), activeforeground=randomizeColor())
    #     case "Frame":
    #         for i in group:
    #             i.configure(bg=randomizeColor(), cursor=cursors[c()], bd=c())

    # The WRONG way
    # if object == "Side.TFrame":
    #     for i in group:
    #         style.configure("Side.TFrame", background=randomizeColor(), cursor=cursors[c()], padding=c())
    #         i.config(style="Side.TFrame")
    #         j += 1
    #         print("reset side ttk frame", i)
    # elif object == "Options.TFrame":
    #     for i in group:
    #         style.configure("Options.TFrame", background=randomizeColor(), cursor=cursors[c()], padding=c())
    #         i.config(style="Options.TFrame")
    #         j += 1
    #         print("reset options ttk frame", i)
    # elif object == "Main.TFrame":
    #     for i in group:
    #         style.configure("Main.TFrame", background=randomizeColor(), cursor=cursors[c()], padding=c())
    #         i.config(style="Main.TFrame")
    #         j += 1
    #         print("reset main ttk frame", i)
    if object == "TTKFrame":
        for i in group:
            style.configure("Random{0}.TFrame".format(j), background=randomizeColor(), cursor=cursors[c()], padding=c())
            i.config(style="Random{0}.TFrame".format(j))
            j += 1
            # print("randomized ttk frame", i)
    elif object == "TTKNotebook":
        for i in group:
            style.configure("Random{0}.TNotebook".format(j), background=randomizeColor(), bordercolor=randomizeColor())
            i.config(style="Random{0}.TNotebook".format(j))
            j += 1
            # print("randomized ttk notebook", i)
    elif object == "TTKLabel":
        for i in group:
            style.configure("Random{0}.TLabel".format(j), background=randomizeColor(), forground=randomizeColor(), font=(font[f()], s()))
            i.config(style="Random{0}.TLabel".format(j))
            j += 1
            # print("randomized ttk label", i)
    elif object == "TTKButton":
        for i in group:
            style.configure("Random{0}.TButton".format(j), background=randomizeColor(), font=(font[f()], s()), relief="flat", padding=d2(), foreground=randomizeColor())
            i.config(style="Random{0}.TButton".format(j))
            j += 1
            # print("randomized ttk button", i)
    elif object == "Menu":
        for i in group:
            i.config(bg=randomizeColor(), fg=randomizeColor(), activebackground=randomizeColor(), activeforeground=randomizeColor())
            # print("randomized menu", i)
    # elif object == "Frame":
    #     for i in group:
    #         i.configure(bg=randomizeColor(), cursor=cursors[c()], bd=c())
    #         print("randomized frame", i)
        
def resetStyle(option, object, group):
    style = ttk.Style()

    if option == 0:
        if object == "Side.TFrame":
          style.configure("Side.TFrame", background="#282828")
          for i in group:
                i.config(style="Side.TFrame")
                # print("reset side ttk frame", i)
        elif object == "Options.TFrame":
          style.configure("Options.TFrame", background="#575757")
          for i in group:
                i.config(style="Options.TFrame")
                # print("reset options ttk frame", i)
        elif object == "Main.TFrame":
          style.configure("Main.TFrame", background="#121212")
          for i in group:
                i.config(style="Main.TFrame")
                # print("reset main ttk frame", i)
        elif object == "TTKNotebook":
            style.configure("TNotebook", background="#3f3f3f")
            for i in group:
                i.config(style="TNotebook")
                # print("reset ttk notebook", i)
        elif object == "TTKLabel":
            style.configure("TLabel", background="#575757", font=('Helvetica', 12), foreground="white", **label_paddings)
            for i in group:
                i.config(style="TLabel")
                # print("reset ttk label", i)
        elif object == "TTKButton":
            style.configure("TButton", relief="flat")
            for i in group:
                i.config(style="TButton")
                # print("reset ttk button", i)
        elif object == "Menu":
            for i in group:
                i.config(background="#3f3f3f", foreground="#FFF")
                # print("reset menu", i)
    elif option == 1:
        if object == "Side.TFrame":
          style.configure("Side.TFrame", background="#C9CED2")
          for i in group:
                i.config(style="Side.TFrame")
                # print("reset side ttk frame", i)
        elif object == "Options.TFrame":
          style.configure("Options.TFrame", background="#C0C7CB")
          for i in group:
                i.config(style="Options.TFrame")
                # print("reset options ttk frame", i)
        elif object == "Main.TFrame":
          style.configure("Main.TFrame", background="#E9EFF3")
          for i in group:
                i.config(style="Main.TFrame")
                # print("reset main ttk frame", i)
        elif object == "TTKNotebook":
            style.configure("TNotebook", background="#B3B8BB")
            for i in group:
                i.config(style="TNotebook")
                # print("reset ttk notebook", i)
        elif object == "TTKLabel":
            style.configure("TLabel", background="#C0C7CB", foreground="black", font=('Helvetica', 12), **label_paddings)
            for i in group:
                i.config(style="TLabel")
                # print("reset ttk label", i)
        elif object == "TTKButton":
            style.configure("TButton", relief="flat")
            for i in group:
                i.config(style="TButton")
                # print("reset ttk button", i)
        elif object == "Menu":
            for i in group:
                i.config(background="#282828")
                # print("reset menu", i)

    return