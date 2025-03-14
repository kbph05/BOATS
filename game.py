import window
import image #, cutscenes, choices

class Game:

    ## CONSTRUCTOR ##
    def __init__(self):
        self.name = ""
        self.gameWin = window.Window( )
    
    ## MENU ##
    def menu(self, frame):

        frame.destroy() # destroy the disclaimer frame

        titleFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("a.PNG")

        testImage.drawImage(titleFrame, testImage.image, "pink", "left")
        testImage.drawImage(titleFrame, testImage.image, "pink", "left")
        testImage.drawImage(titleFrame, testImage.image, "pink", "left")
        testImage.drawImage(titleFrame, testImage.image, "pink", "left") 

        menuFrame = self.gameWin.makeFrame(1300, 1300)
        titleLabel = self.gameWin.makeLabel(menuFrame, "BOATS", "pink", "top", 20)
        startButton = self.gameWin.makeButton(menuFrame, testImage.image, "white", (lambda: self.intro(menuFrame)))
    
    def intro(self, frame):
        
        frame.destroy() # destroy the menu frame

        introFrame = self.gameWin.makeFrame(1300, 1000)
        testImage = image.Image("a.PNG")

        nameLabel = self.gameWin.makeLabel(introFrame, "What is your name?", "pink", "top", 20)
        startButton = self.gameWin.makeButton(introFrame, testImage.image, "white", (lambda: self.disclaimer(introFrame)))
        nameLabel = self.gameWin.makeInput(introFrame)
        self.name = nameLabel.get()

    def disclaimer(self, frame):

        frame.destroy() # destroy the intro framk

        disclaimerFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("a.PNG")

        disclaimerLabel = self.gameWin.makeLabel(disclaimerFrame, "**TEST GAME**\n This is a test game for the Choose Your Own Adventure game."
        "\nIt is not the final game and is only for testing purposes.\nThe final game will have a proper storyline, choices, dialogs, and character "
        "animations.\n\n**CUTSCENE HERE**\n\nPress Enter to continue!", "pink", "top", 20)
        continueButton = self.gameWin.makeButton(disclaimerFrame, testImage.image , "white", (lambda: self.stage1(disclaimerFrame)))
        
    ## FIRST STAGE ##     
    def stage1(self, frame):

        frame.destroy() # destroy the disclaimer frame
        
        stage1Frame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("a.PNG")

        self.gameWin.makeLabel(stage1Frame, "You find yourself in a dark room with two doors. The first door is red, the second is white! Which door do you want to choose?", "pink", "top", 12)
        self.gameWin.makeButton(stage1Frame, testImage.image, "white", (lambda: self.redDoor(stage1Frame)))
        self.gameWin.makeButton(stage1Frame, testImage.image, "white", (lambda: self.whiteDoor(stage1Frame)))

    ## RED DOOR ##
    def redDoor(self, frame):

        frame.destroy()

        redDoorFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("a.PNG")

        self.gameWin.makeLabel(redDoorFrame, "You walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!\nWhat do you want to do? Accept or Decline?", "pink", "top", 20)
        self.gameWin.makeButton(redDoorFrame, testImage.image, "white", (lambda: self.acceptMission(redDoorFrame)))
        self.gameWin.makeButton(redDoorFrame, testImage.image, "white", (lambda: self.declineMission(redDoorFrame)))
            
    def acceptMission(self, frame):

        frame.destroy()

        acceptFrame = self.gameWin.makeFrame(1300, 1300)

        self.gameWin.makeLabel(acceptFrame, "SUCCESS! You helped the scientist save the world! In gratitude, the scientist builds a time machine and sends you home!", "pink", "top", 20)

    def declineMission(self, frame):

        frame.destroy()

        declineFrame = self.gameWin.makeFrame(1300, 1300)

        self.gameWin.makeLabel(declineFrame, "Too bad! You declined the scientists offer and now you are stuck in the future!", "pink", "top", 20)
    
    
