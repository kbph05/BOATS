import window
import image #, cutscenes, choices

class Game:

    ## CONSTRUCTOR ##
    def __init__(self):
        self.name = ""
        self.gameWin = window.Window()
    
    ## MENU ##
    def menu(self, frame):

        frame.destroy() # destroy the disclaimer frame

        titleFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image('a.PNG')

        testImage.drawImage(titleFrame, testImage.image, "pink", "left")
        testImage.drawImage(titleFrame, testImage.image, "pink", "left")
        testImage.drawImage(titleFrame, testImage.image, "pink", "left")
        testImage.drawImage(titleFrame, testImage.image, "pink", "left") 

        menuFrame = self.gameWin.makeFrame(1300, 1300)
        startButton = self.gameWin.makeButton(menuFrame, testImage.image, "white", (lambda: self.intro(menuFrame)))
    
    # def intro(self, frame):
        
    #     frame.destroy() # destroy the menu frame

    #     introFrame = self.gameWin.makeFrame(1300, 1000)
    #     testImage = image.Image('a.PNG')

    #     nameLabel = self.gameWin.makeLabel(introFrame, "What is your name?", "pink", "top", 20)
    #     startButton = self.gameWin.makeButton(introFrame, testImage.image, "white", (lambda: self.disclaimer(introFrame)))
    #     nameLabel = self.gameWin.makeInput(introFrame)
    #     self.name = nameLabel.get()

    # def disclaimer(self, frame):

    #     frame.destroy() # destroy the intro framk

    #     disclaimerFrame = self.gameWin.makeFrame(1300, 1300)
    #     testImage = image.Image(self.alphabet[1])

    #     disclaimerLabel = self.gameWin.makeLabel(disclaimerFrame, "**TEST GAME**\n This is a test game for the Choose Your Own Adventure game."
    #     "\nIt is not the final game and is only for testing purposes.\nThe final game will have a proper storyline, choices, dialogs, and character "
    #     "animations.\n\n**CUTSCENE HERE**\n\nPress Enter to continue!", "pink", "top", 20)
    #     continueButton = self.gameWin.makeButton(disclaimerFrame, testImage.image , "white", (lambda: self.stage1(disclaimerFrame)))
    