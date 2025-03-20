import window
import image #, cutscenes, choices

class Game:

    ## CONSTRUCTOR ##
    def __init__(self):
        self.alphabet = [None] * 25
        self.numbers  = [None] * 9
        self.symbols  = [None] * 13
        self.name = ""
        self.gameWin = window.Window()
        # bring the imported alphabet here:
        self.alphabet = self.importAlphabet(self.alphabet)
    
    ## MENU ##
    def menu(self, frame):

        self.gameWin.destroyFrames() # destroy the disclaimer frame

        # frame array so that all frames can be destroyed

        titleFrame = self.gameWin.makeFrame(1300, 1300)
        letter1 = image.Image('a.png')
        letter2 = image.Image('c.png')

        letter1.drawImage(titleFrame, letter1.image, "pink", "left")
        letter2.drawImage(titleFrame, letter2.image, "pink", "left")
        letter1.drawImage(titleFrame, letter1.image, "pink", "left")
        letter2.drawImage(titleFrame, letter2.image, "pink", "left") 

        menuFrame = self.gameWin.makeFrame(1300, 1300)
        startButton = self.gameWin.makeButton(menuFrame, letter2.image, "white", (lambda: self.intro(menuFrame)))
        settingsButton = self.gameWin.makeButton(menuFrame, letter1.image, "white", (lambda: self.settings(menuFrame)))

    def settings(self, frame):
        
        self.gameWin.destroyFrames() # destroy the menu frame

        settingsFrame = self.gameWin.makeFrame(1300, 1300)
        letter1 = image.Image('a.png')

        audioButton = self.gameWin.makeButton(settingsFrame, letter1.image, "white", (lambda: self.settings(settingsFrame))) # command will be different
        musicButton = self.gameWin.makeButton(settingsFrame, letter1.image, "white", (lambda: self.settings(settingsFrame))) # command will be different
        backButton =  self.gameWin.makeButton(settingsFrame, letter1.image, "white", (lambda: self.menu(settingsFrame)))
    

    def intro(self, frame):
        
        self.gameWin.destroyFrames() # destroy the menu frame

        introFrame = self.gameWin.makeFrame(1300, 1000)
        testImage = image.Image('a.png')

        nameLabel = self.gameWin.makeLabel(introFrame, "What is your name?", "pink", "top", 20)
        # startButton = self.gameWin.makeButton(introFrame, testImage.image, "white", (lambda: self.disclaimer(introFrame)))
        nameLabel = self.gameWin.makeInput(introFrame)
        backButton =  self.gameWin.makeButton(introFrame, testImage.image, "white", (lambda: self.menu(introFrame)))
        self.name = nameLabel.get()

    # def disclaimer(self, frame):

    #     frame.destroy() # destroy the intro framk

    #     disclaimerFrame = self.gameWin.makeFrame(1300, 1300)
    #     testImage = image.Image(self.alphabet[1])

    #     disclaimerLabel = self.gameWin.makeLabel(disclaimerFrame, "**TEST GAME**\n This is a test game for the Choose Your Own Adventure game."
    #     "\nIt is not the final game and is only for testing purposes.\nThe final game will have a proper storyline, choices, dialogs, and character "
    #     "animations.\n\n**CUTSCENE HERE**\n\nPress Enter to continue!", "pink", "top", 20)
    #     continueButton = self.gameWin.makeButton(disclaimerFrame, testImage.image , "white", (lambda: self.stage1(disclaimerFrame)))
    
    def importAlphabet(self, alphabet):
        alphabetFont = ["a.png", "c.png"]
        for i, letter in enumerate(alphabetFont):
            alphabet[i] = image.Image(alphabetFont[i])
        return alphabet