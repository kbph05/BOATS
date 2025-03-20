import tkinter

class Window():
    def __init__(self):
        # Window
        self.window = tkinter.Tk() # Create a window
        self.window.title("BOATS") # Set the title of the window
        self.window.geometry("1000x700")
        self.window.configure(bg="pink")
        self.frames = [None]

        # Image
        # self.alphabet = self.importAlphabet()
        # self.numbers = self.importNumbers()
        # self.symbols = self.importSymbols()
        # self.map = self.importMap()


    ## FUNCTIONS ##

    def makeFrame(self, width, height):
        frame = tkinter.Frame(self.window, width=200, height=100, bg="pink")
        frame.pack(side="top", padx=10, pady=10)
        self.frames.append(frame)
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
    
    def destroyFrames(self):
        for frame in self.frames:
            if frame is not None:
                frame.destroy()
        self.frames = []

  

    
 
    # function to get values of inputs