import cv2
import numpy as np

class Filter:
    def __init__(self, img):
        self.img = img
        self.sharpen3 = np.array([[0,-1,0],
                             [-1,5,-1],
                             [0,-1,0]])

        self.sobelX = np.array([[1.0,0,-1],
                   [2,0,-2],
                   [1,0,-1]])

        self.sobelY = Sobel_Y = np.array([[1.0,2,1],
                    [0,0,0],
                    [-1,-2,-1]])

        self.gaussianUnsharp5 = np.array([[1,4,6,4,1.0],
                        [4,16,24,16,4],
                        [6,24,-476,24,6],
                        [4,16,24,16,4],
                        [1,4,6,4,1]])/(-256)
        self.customFilters = []
        # Add some way to read custom filters from the database to fill this list
        return

    def sobelX(self):
        return cv2.filter2D(self.img, -1, self.sobelX)

    def sobelY(self):
        return cv2.filter2D(self.img, -1, self.sobelY)

    def sharpen3(self):
        return cv2.filter2D(self.img, -1, self.sharpen3)

    def gaussianUnsharp5(self):
        return cv2.filter2D(self.img, -1, self.gaussianUnsharp5)

    def addCustom(self, filter):
        self.customFilters.append(filter)
        # Add code to update the user's saved filters
        return
