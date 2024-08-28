import os
import sys
import uuid
import numpy as np
import cv2
import keyboard
import requests
from tkinter import *
from tkinter import filedialog, simpledialog
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image
from datetime import datetime
from threading import Timer

from Color import BGRController

class Application:
    # Pass in the root as a parameter to the constructor.
    def __init__(self, root, right_frame, layer_notebook_frame, selected_layer_label, logged_in):
        self.draw = False
        self.orientationIsVertical = False
        self.baseImageWidth = 0
        self.baseImageHeight = 0
        self.lineThickness = 14
        self.selectedLayer = 0
        self.selectedColorSpace = 0
        self.isFullScreen = False
        self.imagePath = "./testImages/personalTestImages/blueEyesFella.png"
        self.theme_var = IntVar(root)  # variable that keeps track of what theme is being applied
        self.theme_var.set(0)
        self.logged_in = logged_in
        self.thread = Timer(1.0, lambda: print("Hi :)"))

        # Setting a default imgLabel and color values
        self.imgLabel = None
        self.red = 1
        self.blue = 1
        self.green = 1

        # Assign the default save directory
        self.default_save_dir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "SavedImages")
        # Make sure the directory exists
        os.makedirs(self.default_save_dir, exist_ok=True)

        # GUI components that we're storing in the object
        self.root = root
        self.right_frame = right_frame
        self.layer_notebook_frame = layer_notebook_frame
        self.selected_layer_label = selected_layer_label

        self.window_name = "Code Demo"

        # List that stores each image layer
        self.layers = []

        # List that stores each precompiled layer for editing
        self.compiledLayers = []

        # List that stores buttons to select layers
        self.layerButtons = []

        # List to keep track of each color controller for each layer
        self.colorControllers = []

    # You are never going to belive what this funtion does
    def changeLineColor(self):
        colors = askcolor(title="Tkinter Color Chooser")
        if colors[1]:  # Check if a color was selected
            self.red, self.green, self.blue = colors[0]

    '''Takes the imgLabel and addLinePixel as input
    Creates a line image, adds it to the layers, and renders line on the other images'''
    def addLine(self, addLinePixel, imgLabel):
        pixelAt = int(addLinePixel.get())
        line = np.zeros((self.baseImageHeight, self.baseImageWidth, 4))

        if not self.orientationIsVertical:
            line[pixelAt - self.lineThickness // 2:pixelAt + self.lineThickness // 2, ::, 0] = self.blue
            line[pixelAt - self.lineThickness // 2:pixelAt + self.lineThickness // 2, ::, 1] = self.green
            line[pixelAt - self.lineThickness // 2:pixelAt + self.lineThickness // 2, ::, 2] = self.red
        else:
            line[::, pixelAt - self.lineThickness // 2:pixelAt + self.lineThickness // 2, 0] = self.blue
            line[::, pixelAt - self.lineThickness // 2:pixelAt + self.lineThickness // 2, 1] = self.green
            line[::, pixelAt - self.lineThickness // 2:pixelAt + self.lineThickness // 2, 2] = self.red
        self.addLayer(line)
        self.renderImage(imgLabel)
        return

    '''Takes an int as input
    Updates the self.selectedLayer variable
    Updates the compiledLayers array with the layers array'''
    def updateSelectedLayer(self, layer):
        self.selectedLayer = layer
        self.selected_layer_label.config(text=str(self.selectedLayer))
        self.compiledLayers[layer] = [self.compileLayers(uncompiled=self.layers[:layer]),
                                      self.layers[self.selectedLayer],
                                      self.compileLayers(uncompiled=self.layers[(layer+1):])]

        return

    def setImgLabel(self, imgLabel):
        self.imgLabel = imgLabel

    def getImg(self):
        return self.layers[self.selectedLayer]

    # Saves the image to the SavedImages folder with a unique name as a jpg
    def saveImage(self):
        # Getting unique identifiers for the image name
        unique_id = uuid.uuid4().hex[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Defining the unique file name
        default_filename = f"image_{timestamp}_{unique_id}.jpg"

        # Assigning the save path to the default folder
        save_path = os.path.join(self.default_save_dir, default_filename)

        # Getting the current image
        imageToSave = self.layers[self.selectedLayer]

        # Saving the image
        cv2.imwrite(save_path, imageToSave)
        return

    # The user selects the save location, file name, and file type before the image is saved
    def saveImgAs(self):
        # Asking the user for the save information
        file = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg")))
        # Taking the user input and then actually using it to save the image
        if file:
            abs_path = os.path.abspath(file.name)
            out = self.layers[self.selectedLayer]
            cv2.imwrite(abs_path, out)
        return

    '''Takes an image as input
    Adds a button to the GUI to select the layer
    Adds the layer to each of the lists we are storing: layers, compiledLayers, layerButtons, colorControllers
    Calls updateSelectedLayer to make sure that things render properly
    '''
    def addLayer(self, imgToAdd):
        numLayers = len(self.layers)
        if numLayers == 0:
            buttonLabel = "Select Base Image"
        else:
            buttonLabel = "Select Layer " + str(numLayers)
        button = ttk.Button(self.layer_notebook_frame, text=buttonLabel, command=lambda: self.updateSelectedLayer(numLayers))
        button.grid(column=0, row=numLayers)

        layerColorControllers = []
        layerColorControllers.append(BGRController(imgToAdd))
        self.colorControllers.append(layerColorControllers)

        # Add button to be able to select the new layer
        self.layerButtons.append(button)

        # Add a new entry to the compiled layer array
        self.compiledLayers.append([self.compileLayers(uncompiled = self.layers),imgToAdd,[]])

        # Add the new layer to the layers list
        self.layers.append(imgToAdd)

        # Update the compiled layers array for the selected layers
        self.updateSelectedLayer(self.selectedLayer)
        return

    def removeLayer(self, imgLabel):
        # Check to ensure we don't remove the base layer
        if self.selectedLayer == 0:
            return
        #Destroy the tkinter button
        self.layerButtons[-1].destroy()

        # Remove all the array things
        self.layers.pop(self.selectedLayer)
        self.compiledLayers.pop(self.selectedLayer)
        self.layerButtons.pop(-1)
        self.colorControllers.pop(self.selectedLayer)

        # Update the selected layer to update what we display to the user
        self.updateSelectedLayer(self.selectedLayer-1)
        self.renderImage(imgLabel)

    # Pass in the red, green, and blue sliders to the function

    def blurImg(self, blur_type, blur_value, imgLabel):
        blur_value = int(blur_value)
        temp = self.layers[self.selectedLayer]
        if blur_type == "gaussian":
            self.layers[self.selectedLayer] = cv2.GaussianBlur(self.layers[self.selectedLayer],
                                                                          (2*blur_value-1,2*blur_value-1),0)
            self.compiledLayers[self.selectedLayer][1] = self.layers[self.selectedLayer]
        elif blur_type == "box":
            self.layers[self.selectedLayer] = cv2.blur(self.layers[self.selectedLayer],
                                                          (2*blur_value-1,2*blur_value-1))
            self.compiledLayers[self.selectedLayer][1] = self.layers[self.selectedLayer]
        elif blur_type == "median":
            self.layers[self.selectedLayer] = cv2.medianBlur(self.layers[self.selectedLayer], blur_value)
            self.compiledLayers[self.selectedLayer][1] = self.layers[self.selectedLayer]

        self.renderImage(imgLabel)

        self.compiledLayers[self.selectedLayer][1] = temp
        self.layers[self.selectedLayer] = temp
        return

    def confirmBlurChanges(self, blur_type, blur_value, imgLabel):
        blur_value = int(blur_value)
        if blur_type == "gaussian":
            self.layers[self.selectedLayer] = cv2.GaussianBlur(self.layers[self.selectedLayer],
                                                               (2 * blur_value - 1, 2 * blur_value - 1), 0)
            self.compiledLayers[self.selectedLayer][1] = self.layers[self.selectedLayer]
        elif blur_type == "box":
            self.layers[self.selectedLayer] = cv2.blur(self.layers[self.selectedLayer],
                                                       (2 * blur_value - 1, 2 * blur_value - 1))
            self.compiledLayers[self.selectedLayer][1] = self.layers[self.selectedLayer]
        elif blur_type == "median":
            self.layers[self.selectedLayer] = cv2.medianBlur(self.layers[self.selectedLayer], 2*blur_value-1)
            self.compiledLayers[self.selectedLayer][1] = self.layers[self.selectedLayer]

        self.renderImage(imgLabel)
        return

    # This function grabs a random cat image from Cat api and returns its url if its valid
    def getRandomCatImage(self):
        try:
            response = requests.get('https://api.thecatapi.com/v1/images/search')
            ping = response.json()
            # Making sure it worked before returning
            if response.status_code == 200 and ping:
                randomCatimageURL = ping[0]['url']
                return randomCatimageURL
            # In case something goes wrong
            else:
                return None
        # A catch in case we have any errors to just return nothing instead of crashing
        except Exception as e:
            return None

    def setBaseImage(self, red, green, blue, imgLabel):
        self.layers = []
        self.layerButtons = []
        self.colorControllers = []
        
        # TODO: If stock cat image is not in BGRA, set to BGRA with cv2

        # Grab a random cat image url from the getRandomCatImage function
        randomCatimageURL = self.getRandomCatImage()

        # Making sure that the image is usable before we send it on
        if randomCatimageURL:
            # Converting the image from a url to a workable image
            imgURL = requests.get(randomCatimageURL)
            imageData = imgURL.content
            imageArray = np.frombuffer(imageData, np.uint8)
            img = cv2.imdecode(imageArray, cv2.IMREAD_COLOR)
            # Making sure an image was returned and not one of the None statements
            if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
                # Resize the image if it's uncomfortably large
                if img.shape[1] > 600 or img.shape[0] > 600:
                    img = cv2.resize(img, (600, 600))
                # Setting the base image
                self.baseImageHeight, self.baseImageWidth = img.shape[:2]
                # Sets the opening screen size
                self.root.minsize(max(800, self.baseImageWidth), self.baseImageHeight)
                self.addLayer(img)
                # redValue, greenValue, blueValue = self.initializeSliders()
                redValue, greenValue, blueValue = 255, 255, 255
                red.set(int(redValue))
                green.set(int(greenValue))
                blue.set(int(blueValue))
                self.renderImage(imgLabel)
            # Threw errors every once in a while until I added this now I cant get it to throw the error anymore ?
            # I will be looking into this more
            else:
                self.setBaseImage(red, green, blue, imgLabel)


    def initializeSliders(self):
        totalRed = np.average(self.layers[self.selectedLayer][::, ::, 0])
        totalGreen = np.average(self.layers[self.selectedLayer][::, ::, 1])
        totalBlue = np.average(self.layers[self.selectedLayer][::, ::, 2])
        total = totalRed + totalGreen + totalBlue
        print(total)
        print(totalRed)
        print(self.layers[self.selectedLayer][::, ::, 0])
        print(int(totalRed / total * 255))
        return int(totalRed / total * 255), int(totalGreen / total * 255), int(totalBlue / total * 255)

    '''Takes in the imgLabel as an input
    Sets the image tag of imgLabel to the result of compiledLayer'''
    def renderImage(self, imgLabel):
        imgToRender = self.compileLayers()
        imgToRender = cv2.cvtColor(imgToRender.astype('uint8'), cv2.COLOR_BGR2RGBA)
        imgToRender = ImageTk.PhotoImage(Image.fromarray(imgToRender))
        imgLabel.config(image=imgToRender)
        imgLabel.image = imgToRender
        return

    '''Takes uncompiled as a parameter
    If uncompiled is left as a default parameter, then use the pre-compiled layers for optimization
    Otherwise, take uncompiled as a list of numpy image arrays and compile them'''
    def compileLayers(self, uncompiled = [-1]):
        # For the default, use the pre-compiled layers
        if len(uncompiled) == 1 and type(uncompiled[0]) == int:
            if uncompiled == [-1]:
                uncompiled = self.compiledLayers[self.selectedLayer]

        result = np.zeros((self.baseImageHeight, self.baseImageWidth, 3))
        for i in range(len(uncompiled)):
            blackAndWhite = cv2.cvtColor(uncompiled[i].astype('uint8'), cv2.COLOR_BGR2GRAY)
            bools = (blackAndWhite != 0).astype(int)
            notBools = 1 - bools
            result[::, ::, 0] = result[::, ::, 0] * notBools + uncompiled[i][::, ::, 0] * bools
            result[::, ::, 1] = result[::, ::, 1] * notBools + uncompiled[i][::, ::, 1] * bools
            result[::, ::, 2] = result[::, ::, 2] * notBools + uncompiled[i][::, ::, 2] * bools
        return result

    def toggleOrientation(self):
        self.orientationIsVertical = not self.orientationIsVertical
        return self.orientationIsVertical