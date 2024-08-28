from tkinter import Frame, Label
from PIL import ImageTk, Image
from random import randint
from threading import Timer

from SecondaryWindow import SecondaryWindow

# If adding new advertisements add their file path to this list
advertisement_list = ["./advertisements/blueEyesFella.png", "./advertisements/lmr.png",
                      "./advertisements/smokingBug.png", "./advertisements/beans.png",
                      "./advertisements/beans2.png", "./advertisements/bear.png",
                      "./advertisements/cow.png", "./advertisements/doyoufish.png",
                      "./advertisements/garbanzo.png", "./advertisements/horseonbalcony.png",
                      "./advertisements/sungod.png", "./advertisements/povbear.png"]


class AdvertisementWindow(SecondaryWindow):
    def __init__(self, screenwidth, screenheight, image, *args, **kwargs):
        int_width = int(image.width)
        int_height = int(image.height)

        # Random screen position with padding
        pos_x = randint(10, screenwidth - int_width)
        pos_y = randint(10, screenheight - int_height)

        super().__init__(0, 0, "Awesome Advertisement: Log In to Stop", False, "#282828", "./icons/payus.png", *args, **kwargs)

        # Sets the screen width, height, x-position, and y-position to the ones we provided
        self.geometry('%dx%d+%d+%d' % (int_width, int_height, pos_x, pos_y))

        image_frame = Frame(self, width=int_width, height=int_height)
        ad_photo = ImageTk.PhotoImage(image)
        photo_label = Label(image_frame, image=ad_photo)

        # Avoids garbage collection
        photo_label.image = ad_photo

        image_frame.pack()
        image_frame.place(anchor="center", relx=0.5, rely=0.5)

        photo_label.pack()


# Displays advertisements for users who are not logged in
def display_advertisement(app, screenwidth, screenheight):
    if not app.logged_in:
        # Chooses a random file path from the advertisements array
        image_path = advertisement_list[randint(0, len(advertisement_list) - 1)]
        image = Image.open(image_path)

        # Finds the aspect ratio of the image
        aspect = image.width / image.height

        # Chooses a random width from 200 pixels to the screenheight adjusted for padding
        random_width = randint(200, screenheight - 10)

        # Uses the aspect ratio and the random width to find the random height of the image
        random_height = int(random_width * aspect)

        # Creates the advertisement window using the provided sizes
        AdvertisementWindow(screenwidth, screenheight, image.resize((random_width, random_height)))

        image.close()

        # Starts the next timer
        app.thread = Timer(randint(5, 30), lambda: display_advertisement(app, screenwidth, screenheight))
        app.thread.start()
