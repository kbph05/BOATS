import tkinter

class Window():
    def __init__(self):
        # Window
        self.window = tkinter.Tk() # Create a window
        self.window.title("Choose Your Own Adventure") # Set the title of the window
        self.window.geometry("1500x1000")
        self.window.configure(bg="pink")

        # Image
        # self.alphabet = self.importAlphabet()
        # self.numbers = self.importNumbers()
        # self.symbols = self.importSymbols()
        # self.map = self.importMap()


    ## FUNCTIONS ##

    def makeFrame(self, width, height):
        frame = tkinter.Frame(self.window, width=200, height=100, bg="pink")
        frame.pack(side="top", padx=10, pady=10)
        return frame

    def makeLabel(self, frame, text, background, side, fontSize):
        label = tkinter.Label(frame, text=text, fg="white", bg=background, font=("Arial", fontSize))
        label.pack(side=side)
        return label

    def makeButton(self, frame, image, background, command):
        button = tkinter.Button(frame, command=command, image=image, bg=background)
        button.pack()
        button.image = image
        return button

    def makeInput(self, frame):
        input = tkinter.Entry(frame, fg="black", bg="grey", borderwidth=4, relief="groove", font=("Arial", 20))
        input.pack(side="top", padx=10, pady=10)
        return input

  

    

    # function to get values of inputs