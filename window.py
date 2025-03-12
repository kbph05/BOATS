import tkinter
from tkinter import PhotoImage
import canvas


class Window():
    def __init__(self):
        self.window = tkinter.Tk() # Create a window
        self.window.title("Choose Your Own Adventure") # Set the title of the window
        self.window.geometry("1500x1000")
        self.window.configure(bg="white")
        # self.frame = self.tkinter.Frame(self.window, width=200, height=100, bg="black")
        # make the frame transparent
        # window.attributes('-alpha', 0.5)

    ## FUNCTIONS ##

    def makeFrame(self, width, height):
        frame = tkinter.Frame(self.window, width=200, height=100, bg="white")
        frame.pack(side="top", padx=10, pady=10)
        return frame

    def makeLabel(self, frame, text, fontSize):
        label = tkinter.Label(frame, text=text, fg="black", bg="white", font=("Arial", fontSize))
        label.pack(side="top", padx=10, pady=10)
        return label

    def makeButton(self, frame, text, command):
        button = tkinter.Button(frame, text=text, command=command, fg="black", bg="grey", font=("Courier", 20))
        button.pack(side="top", padx=10, pady=10)
        return button

    def makeInput(self, frame):
        input = tkinter.Entry(frame, fg="black", bg="grey", borderwidth=4, relief="groove", font=("Arial", 20))
        input.pack(side="top", padx=10, pady=10)
        return input
    
    # function to get values of inputs