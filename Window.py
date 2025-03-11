import tkinter
from tkinter import PhotoImage
import canvas


class Window():
    def __init__(self):
        self.window = tkinter.Tk() # Create a window
        self.window.title("Choose Your Own Adventure") # Set the title of the window
        self.window.geometry("1000x600")
        self.window.configure(bg="black")
        #make the frame transparent
        # window.attributes('-alpha', 0.5)

    ## FUNCTIONS ##

    def makeFrame(self, width, height):
        frame = tkinter.Frame(self.window, width=200, height=100, bg="black")
        return frame

    def makeLabel(self, text):
        label = tkinter.Label(self.window, text=text, fg="white", bg="black", font=("Courier", 40))
        return label

    def makeButton(self, text, command):
        button = tkinter.Button(self.window, text=text, command=command, fg="white", bg="grey", font=("Courier", 20))
        return button

    def makeInput(self):
        input = tkinter.Entry(self.window, fg="white", bg="grey", borderwidth=4, relief="groove", font=("Courier", 20))
        return input
    
    # def pack(self, object, x, y):
    #     object.pack(side="top", padx=x, pady=y)
