import window
import tkinter
from tkinter import PhotoImage

class Image:
    def __init__(self, imageName):
        self.image = PhotoImage(file=imageName)

    def drawImage(self, frame, image, background, side):
        label = tkinter.Label(frame, image=self.image, bg=background)
        label.image = image
        label.pack(side=side)
        return label

    def resize(self, width, height):
        self.image = self.image.zoom(width, height)
        return self
    
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
  
        