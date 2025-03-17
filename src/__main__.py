import game
import image
import tkinter

# Global variables

# def importNumbers():
#     numbersFont = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]
#     numbers = image.Image(numbersFont[0])
#     return numbers

# def importSymbols():
#     symbolsFont = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "+", "/", ":"]
#     symbols = image.Image(symbolsFont[0])
#     return symbols

# def importMap():
#     mapFont = ["map.png"]
#     map = image.Image(mapFont[0])
#     return map

def runGame():
    frame = newGame.gameWin.makeFrame(1300, 1300)
    newGame.menu(frame)
    newGame.gameWin.window.mainloop()


#########################


newGame = game.Game()
# alphabet = importAlphabet()
# numbers = importNumbers()
# symbols = importSymbols()
# map = importMap()

runGame()
