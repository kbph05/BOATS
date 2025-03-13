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
    

        