import game
import window 
import image
import tkinter

# MAIN CLASS
def importFiles():
    pass
    # gameWindow = window.Window()
    # gameWindow.importAlphabet(["a", "b", "c", "d", "e", "f", "g", "h", 
    #             "i", "j", "k", "l", "m", "n", "o", "p", 
    #             "q", "r", "s", "t", "u", "v", "w", "x", 
    #             "y", "z"])
    # gameWindow.importNumbers("0", "1", "2", "3", "4", "5", "6", "7", 
    #            "8", "9")
    # gameWindow.importSymbols("!", "@", "#", "$", "%", "?", "&", "*", 
    #            "(", ")", "-", "+", "/", ":")

    # gameWindow.importMap("images/map.png")
    # gameWindow.importImage("images/Chrystal.png")

def runGame():
    newGame = game.Game() # BRUH WHY THE-oh i get it now
    frame = newGame.gameWin.makeFrame(1300, 1300)
    newGame.menu(frame)
    newGame.gameWin.window.mainloop()

importFiles()
runGame()
