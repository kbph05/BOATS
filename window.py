import tkinter

class Window():
    def __init__(self):
        # Window
        self.window = tkinter.Tk() # Create a window
        self.window.title("Choose Your Own Adventure") # Set the title of the window
        self.window.geometry("1500x1000")
        self.window.configure(bg="white")

        # Image
        # self.alphabet = self.importAlphabet()
        # self.numbers = self.importNumbers()
        # self.symbols = self.importSymbols()
        # self.map = self.importMap()


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
    
    def drawImage(self, frame, image):
        label = tkinter.Label(frame, image=image)
        label.image = image
        label.pack()
        return label

    ## Importing map
    # def importMap(self, imageName):
    #     map = Image.open(imageName)
    #     return map

    # ## Importing text
    # def importAlphabet(self, letters):
    #     alphabet = {}
    #     for letter in letters:
    #         alphabet[letter] = self.importImage(letter + ".png") # add the letter image to the array
    #     return alphabet 
        
    # def importNumbers(self, numbers):
    #     m_numbers = {}
    #     for number in numbers:
    #         m_numbers[number] = self.importImage("images/" + number + ".png") # add the number image to the array
    #     return numbers 

    # def importSymbols(self, symbols):
    #     m_symbols = {}
    #     for symbol in symbols:
    #         m_symbols[symbol] = self.importImage("images/" + symbol + ".png") # add the symbol image to the array
    #     return symbols

    

    # function to get values of inputs