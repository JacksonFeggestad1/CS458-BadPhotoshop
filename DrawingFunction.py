import cv2
import numpy as np
import keyboard
import ctypes
from tkinter.colorchooser import askcolor

def drawShit(height, width, path):
    global areDrawiwing, winder, windowLocation, bgr_track, img, font, imgWithDrawing
    areDrawiwing = False
    font = cv2.FONT_HERSHEY_SIMPLEX
    winder = "Do Draw"
    windowLocation = [(400, 30), (490, 90)]

    # Declaring and naming the window
    imgWithDrawing = np.zeros((height, width, 3), np.uint8)
    img = path
    cv2.namedWindow(winder)

    # Function name says it all
    # is required to work
    def ahhIHateMyLife(x):
        pass

    # This is the function that will change the color of the drawing
    def change_color():
        global red, green, blue
        colors = askcolor(title="Tkinter Color Chooser")
        # Checks if a color was selected
        if colors[1]:
            red, green, blue = colors[0]

    # Does the actual drawing when called
    def draw_circle(event, x, y, flags, param):
        global areDrawiwing, img
        # When the left mouse is clicked and the mouse is moving we start drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            areDrawiwing = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if areDrawiwing:
                cv2.circle(img, (x,y), cv2.getTrackbarPos("Brush Size", winder), (blue, green, red), -1)
                cv2.circle(imgWithDrawing, (x,y), cv2.getTrackbarPos("Brush Size", winder), (blue, green, red), -1)

        elif event == cv2.EVENT_LBUTTONUP:
            areDrawiwing = False
            cv2.circle(img, (x,y), cv2.getTrackbarPos("Brush Size", winder), (blue, green, red), -1)
            cv2.circle(imgWithDrawing, (x,y), cv2.getTrackbarPos("Brush Size", winder), (blue, green, red), -1)

    # Brush size bar
    cv2.createTrackbar("Brush Size", winder, 4, 8, ahhIHateMyLife)

    # Locks the function to the window
    cv2.setMouseCallback(winder, draw_circle)

    change_color()

    # Main thread
    while(1):
        cv2.imshow(winder, img)
        cv2.setWindowProperty(winder, cv2.WND_PROP_TOPMOST, 1)

        key = cv2.waitKey(1) & 0xff

        if key == ord('q'):
            break
        if key == ord('p'):
            change_color()

    cv2.destroyAllWindows()
    return(imgWithDrawing)