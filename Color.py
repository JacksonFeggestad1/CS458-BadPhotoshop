import cv2
import numpy as np
#Class for switching colors with Fuzzy Logic (see .zip folder in Teams)
class FuzzyColor:
    def __init__(self):
        return

class ColorConverter:
    def __int__(self):
        return

    def BGR2HSV(self, img):
        return cv2.cvtColor(img, cv2.BGR2HSV)

    def HSV2BGR(self, img):
        return cv2.cvtColor(img, cv2.HSV2BGR)

#Class for controlling the BGR values of an image (layer) with GUI sliders
class BGRController:
    def __init__(self, img):
        self.origImg = np.copy(img)
        self.newImg = np.copy(img)
        return

    # The update function that will get called when sliders are changed
    # def updateColor(self, red, green, blue):
    def updateColor(self, colorValue, color):
        # The CORRECT way to do it, but SOMEBODY doesn't like switch cases
        # match color:
        #     case "red":
        #         self.newImg[::,::,2] = (self.origImg[::,::,2]*(colorValue/255)).astype(int)
        #     case "green":
        #         self.newImg[::,::,1] = (self.origImg[::,::,1]*(colorValue/255)).astype(int)
        #     case "blue":
        #         self.newImg[::,::,0] = (self.origImg[::,::,0]*(colorValue/255)).astype(int)
        #     case _:
        #         self.newImg = self.origImg

        # The WRONG way to do it
        if color == "red":
            self.newImg[::,::,2] = (self.origImg[::,::,2]*(colorValue/255)).astype(int)
        elif color == "green":
            self.newImg[::,::,1] = (self.origImg[::,::,1]*(colorValue/255)).astype(int)
        elif color == "blue":
            self.newImg[::,::,0] = (self.origImg[::,::,0]*(colorValue/255)).astype(int)
        else:
            self.newImg = self.origImg
        
        return self.newImg
