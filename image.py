import window
import tkinter
from tkinter import PhotoImage

class Image:
    def __init__(self, imageName):
        self.image = PhotoImage(file=imageName)

    def drawImage(self, frame, image):
        label = tkinter.Label(frame, image=self.image)
        label.image = image
        label.pack()
        return label
    
    def resizeImage(self, width, height):
        self.image = self.image.zoom(width, height)
        return self.image
    

        