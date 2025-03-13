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

        menuFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("test.png")

        testImage.drawImage(menuFrame, testImage.image)
        titleLabel = self.gameWin.makeLabel(menuFrame, "BOATS", 20)
        startButton = self.gameWin.makeButton(menuFrame, testImage.image, (lambda: self.intro(menuFrame)))
    
    def intro(self, frame):
        
        frame.destroy() # destroy the menu frame

        introFrame = self.gameWin.makeFrame(1300, 1000)
        testImage = image.Image("k.png")
        testImage.drawImage(introFrame, testImage.image)

        nameLabel = self.gameWin.makeLabel(introFrame, "What is your name?", 20)
        startButton = self.gameWin.makeButton(introFrame, testImage.image,  (lambda: self.disclaimer(introFrame)))
        nameLabel = self.gameWin.makeInput(introFrame)
        self.name = nameLabel.get()

    def disclaimer(self, frame):

        frame.destroy() # destroy the intro framk

        disclaimerFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("k.png")
        testImage.drawImage(disclaimerFrame, testImage.image)

        disclaimerLabel = self.gameWin.makeLabel(disclaimerFrame, "**TEST GAME**\n This is a test game for the Choose Your Own Adventure game.\nIt is not the final game and is only for testing purposes.\nThe final game will have a proper storyline, choices, dialogs, and character animations.\n\n**CUTSCENE HERE**\n\nPress Enter to continue!", 20)
        continueButton = self.gameWin.makeButton(disclaimerFrame, testImage.image , (lambda: self.stage1(disclaimerFrame)))
        
    ## FIRST STAGE ##     
    def stage1(self, frame):

        frame.destroy() # destroy the disclaimer frame
        
        stage1Frame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("k.png")
        testImage.drawImage(stage1Frame, testImage.image)

        self.gameWin.makeLabel(stage1Frame, "You find yourself in a dark room with two doors. The first door is red, the second is white! Which door do you want to choose?", 12)
        self.gameWin.makeButton(stage1Frame, testImage.image, (lambda: self.redDoor(stage1Frame)))
        self.gameWin.makeButton(stage1Frame, testImage.image, (lambda: self.whiteDoor(stage1Frame)))

    ## RED DOOR ##
    def redDoor(self, frame):

        frame.destroy()

        redDoorFrame = self.gameWin.makeFrame(1300, 1300)
        testImage = image.Image("k.png")
        testImage.drawImage(redDoorFrame, testImage.image)

        self.gameWin.makeLabel(redDoorFrame, "You walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!\nWhat do you want to do? Accept or Decline?", 20)
        self.gameWin.makeButton(redDoorFrame, testImage.image, (lambda: self.acceptMission(redDoorFrame)))
        self.gameWin.makeButton(redDoorFrame, testImage.image, (lambda: self.declineMission(redDoorFrame)))
            
    def acceptMission(self, frame):

        frame.destroy()

        acceptFrame = self.gameWin.makeFrame(1300, 1300)

        self.gameWin.makeLabel(acceptFrame, "SUCCESS! You helped the scientist save the world! In gratitude, the scientist builds a time machine and sends you home!", 20)

    def declineMission(self, frame):

        frame.destroy()

        declineFrame = self.gameWin.makeFrame(1300, 1300)

        self.gameWin.makeLabel(declineFrame, "Too bad! You declined the scientists offer and now you are stuck in the future!", 20)

    # ## WHITE DOOR ##
    # def whiteDoor(self, frame):

    #     frame.destroy()

    #     whiteDoorFrame = self.gameWin.makeFrame(1300, 1300)
    #     testImage = image.Image("k.png")
    #     testImage.drawImage(whiteDoorFrame, testImage.image)

    #     self.gameWin.makeLabel(whiteDoorFrame, "You walk through the white door and are now in the past! You meet a princess who asks you to go on a quest.\nDo you want to accept her offer and go on the quest, or do you want to stay where you are?", 20)
    #     self.gameWin.makeButton(whiteDoorFrame, "k.png", (lambda: self.acceptQuest(whiteDoorFrame)))
    #     self.gameWin.makeButton(whiteDoorFrame, "k.png", (lambda: self.declineQuest(whiteDoorFrame)))

    # def acceptQuest(self, frame):
    #     frame.destroy()

    #     acceptQuest = self.gameWin.makeFrame(1300,1300)
    #     testImage = image.Image("k.png")
    #     testImage.drawImage(acceptQuest, testImage.image)

    #     self.gameWin.makeLabel(acceptQuest, "QUEST ACCEPTED")
    #     self.gameWin.makeButton(acceptQuest, "k.png", (lambda: self.menu(acceptQuest)))
    
    # def declineQuest(self, frame):

    #     frame.destroy()

    #     declineQuest = self.gameWin.makeFrame(1300,1300)
    #     testImage = image.Image("k.png")
    #     testImage.drawImage(declineQuest, testImage.image)

    #     self.gameWin.makeLabel(declineQuest, "QUEST DECLINED")
    #     self.gameWin.makeButton(declineQuest, "k.png", (lambda: self.menu(declineQuest)))
    
    
