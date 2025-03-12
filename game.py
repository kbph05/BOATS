import window

class Game:

    ## CONSTRUCTOR ##
    def __init__(self):
        self.name = ""
        self.gameWin = window.Window( )
    
    ## MENU ##
    def menu(self):
     
        menuFrame = self.gameWin.makeFrame(1300, 1300)
        
        titleLabel = self.gameWin.makeLabel(menuFrame, "Choose Your Own Adventure", 20)
        startButton = self.gameWin.makeButton(menuFrame, "Start", (lambda: self.intro(menuFrame)))
    
    def intro(self, frame):
        
        frame.destroy() # destroy the menu frame

        introFrame = self.gameWin.makeFrame(1300, 1000)
    
        nameLabel = self.gameWin.makeLabel(introFrame, "What is your name?", 20)
        startButton = self.gameWin.makeButton(introFrame, "Start",  (lambda: self.disclaimer(introFrame)))
        nameLabel = self.gameWin.makeInput(introFrame)
        self.name = nameLabel.get()

    def disclaimer(self, frame):

        frame.destroy() # destroy the intro frame

        disclaimerFrame = self.gameWin.makeFrame(1300, 1300)
        
        disclaimerLabel = self.gameWin.makeLabel(disclaimerFrame, "**TEST GAME**\n This is a test game for the Choose Your Own Adventure game.\nIt is not the final game and is only for testing purposes.\nThe final game will have a proper storyline, choices, dialogs, and character animations.\n\n**CUTSCENE HERE**\n\nPress Enter to continue!", 20)
        continueButton = self.gameWin.makeButton(disclaimerFrame, "Continue", (lambda: self.stage1(disclaimerFrame)))
        
    ## FIRST STAGE ##     
    def stage1(self, frame):

        frame.destroy() # destroy the disclaimer frame
        
        stage1Frame = self.gameWin.makeFrame(1300, 1300)

        stage1Label = self.gameWin.makeLabel(stage1Frame, "You find yourself in a dark room with two doors. The first door is red, the second is white! Which door do you want to choose?", 12)
        self.gameWin.makeButton(stage1Frame, "Red", (lambda: self.redDoor(stage1Frame)))
        self.gameWin.makeButton(stage1Frame, "White", (lambda: self.whiteDoor(stage1Frame)))

    ## RED DOOR ##
    def redDoor(self, frame):

        frame.destroy()

        redDoorFrame = self.gameWin.makeFrame(1300, 1300)
        
        self.gameWin.makeLabel(redDoorFrame, "You walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!\nWhat do you want to do? Accept or Decline?", 20)
        self.gameWin.makeButton(redDoorFrame, "Accept", (lambda: self.acceptMission(redDoorFrame)))
        self.gameWin.makeButton(redDoorFrame, "Decline", (lambda: self.declineMission(redDoorFrame)))
            
    def acceptMission(self, frame):

        frame.destroy()

        acceptFrame = self.gameWin.makeFrame(1300, 1300)
        self.gameWin.makeLabel(acceptFrame, "SUCCESS! You helped the scientist save the world! In gratitude, the scientist builds a time machine and sends you home!", 20)

    def declineMission(self, frame):

        frame.destroy()

        declineFrame = self.gameWin.makeFrame(1300, 1300)
        self.gameWin.makeLabel(declineFrame, "Too bad! You declined the scientists offer and now you are stuck in the future!", 20)

    ## WHITE DOOR ##
    def whiteDoor(self, frame):

        frame.destroy()

        whiteDoorFrame = self.gameWin.makeFrame(1300, 1300)
        self.gameWin.makeLabel(whiteDoorFrame, "You walk through the white door and are now in the past! You meet a princess who asks you to go on a quest.\nDo you want to accept her offer and go on the quest, or do you want to stay where you are?", 20)
        self.gameWin.makeButton(whiteDoorFrame, "Accept The Quest", (lambda: self.acceptQuest(whiteDoorFrame)))
        self.gameWin.makeButton(whiteDoorFrame, "Decline And Stay", (lambda: self.declineQuest(whiteDoorFrame)))

    def acceptQuest(self, frame):

        frame.destroy()

        acceptQuest = self.gameWin.makeFrame(1300,1300)
        self.gameWin.makeLabel("QUEST ACCEPTED")
        self.gameWin.makeButton("click")
    
    def declineQuest(self, frame):

        frame.destroy()

        declineQuest = self.gameWin.makeFrame(1300,1300)
        self.gameWin.makeLabel(declineQuest, "QUEST DECLINED")
        self.gameWin.makeButton(declineQuest, "click")
    
    
