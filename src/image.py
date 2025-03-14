import os
import window
import tkinter
from tkinter import PhotoImage

class Image:
        
    def __init__(self, imageName):
        # Get the absolute path to the project directory
        imagePath = os.path.join(os.getcwd(), "characters", imageName)
        self.image = PhotoImage(file=imagePath)  

    # METHODS:

    # DRAWING
    def drawImage(self, frame, image, background, side):
        label = tkinter.Label(frame, image=self.image, bg=background)
        label.image = image
        label.pack(side=side)
        return label

    # RESIZING
    def resize(self, width, height):
        self.image = self.image.zoom(width, height)
        return self

    # CROPPING
    def crop(self, x1, y1, x2, y2):
        self.image = self.image.crop((x1, y1, x2, y2))
        return self