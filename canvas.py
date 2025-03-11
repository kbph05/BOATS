import tkinter
from tkinter import PhotoImage

class Canvas():
    def __init__(self):
        self.canvas = tkinter.Canvas(self.window, width=800, height=600, bg="black")
        self.canvas.pack(side="top", padx=10, pady=10)

    def drawOval(self):
        oval = self.canvas.create_oval(0, 0, 800, 600, fill="blue")

    def drawRectangle(self):
        rectangle = self.canvas.create_rectangle(0, 0, 800, 600, fill="red")
        