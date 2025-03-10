import tkinter
from tkinter import PhotoImage
import Canvas


class Window():
    def __init__(self):
        self.window = tkinter.Tk() # Create a window
        self.window.title("Choose Your Own Adventure") # Set the title of the window
        self.window.geometry("1000x600")
        self.window.configure(bg="black")
        #make the frame transparent
        # window.attributes('-alpha', 0.5)

    def menu(self):
        frame = tkinter.Frame(self.window, width=200, height=100, bg="black")

        label = tkinter.Label(frame, text="Choose Your Own Adventure", fg="white", bg="black", borderwidth=4, relief="groove", font=("Courier", 40))
        label.pack(side="top", padx=10, pady=10)

        button = tkinter.Button(frame, text="Start", command=(lambda: self.startGame(frame)), fg="white", bg="grey", font=("Courier", 20))
        button.pack(side="bottom", padx=10, pady=130)

        frame.pack(side="top", padx=10, pady=10)

    def startGame(self, frame):
        frame.destroy()

