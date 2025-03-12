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
        stage1Label = self.gameWin.makeLabel(stage1Frame, f"Hello {self.name}! You find yourself in a dark room with two doors. The first door is red, the second is white! Which door do you want to choose?", 12)
        redDoor = self.gameWin.makeButton(stage1Frame, "Red", (lambda: self.redDoor(stage1Frame)))
        whiteDoor = self.gameWin.makeButton(stage1Frame, "White", (lambda: self.whiteDoor(stage1Frame)))

    ## RED DOOR ##
    def redDoor(self, frame):

        frame.destroy()

        redDoorFrame = self.gameWin.makeFrame(1300, 1300)
        self.gameWin.makeLabel(redDoorFrame, "You walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!\n", 20)
        
        acceptDecline = self.gameWinmakeInput(redDoorFrame, "What do you want to do? Accept or Decline?")
        self.gameWin.makeButton(redDoorFrame, "Accept", (lambda: self.accept(redDoorFrame)))
        self.gameWin.makeButton(redDoorFrame, "Decline", (lambda: self.decline(redDoorFrame)))
            
    def accept(self, frame):

        frame.destroy()

        acceptFrame = self.gameWin.makeFrame(1300, 1300)
        self.gameWin.makeLabel(acceptFrame, "SUCCESS! You helped the scientist save the world! In gratitude, the scientist builds a time machine and sends you home!", 20)

    def decline(self, frame):

        frame.destroy()

        declineFrame = self.gameWin.makeFrame(1300, 1300)
        self.gameWin.makeLabel(declineFrame, "Too bad! You declined the scientists offer and now you are stuck in the future!", 20)

    ## WHITE DOOR ##
    #def whiteDoor(self):
    
    


# def endGame(self):
#     print(f"Welcome to {name}'s Choose Your Own Adventure game! As you follow the story, you will be presented with choices that decide your fate. Take care and choose wisely (hint!). Let's begin!")
#     print("You find yourself in a dark room with two doors. The first door is red, the second is white!")

#     door_choice = input("Which door do you want to choose? red=red door or white=white door. ")

#     if door_choice == "red":
#         print("Great, you walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!")

#         choice_one = input("What do you want to do? 1=Accept or 2=Decline. ")

#         if choice_one == "1":
#             print("""_____________SUCCESS_____________
#     You helped the scientist save the world! In gratitude, the scientist builds a time machine and sends you home!""")

#         else:
#             print("""___________GAME OVER____________
#     Too bad! You declined the scientists offer and now you are stuck in the future!""")

#     else:
#         print("Great, you walked through the white door and now you are in the past! You meet a princess who asks you to go on a quest.")

#         quest_choice = input("Do you want to accept her offer and go on the quest, or do you want to stay where you are? 1=Accept and go on the quest or 2=Stay. ")

#         if quest_choice == "1":
#             print("The princess thanks you for accepting her offer. You begin the quest. ")

#             choice_two = input("You come accross a mysterious door in a tree, and it is unlocked. Do you 1=Open the door and investigate or 2=Ignore the door and continue on your journey? ")

#             if choice_two == "1":
#                 print("Well done. You have just discovered the very first obamium in the tree and finished the princeses' request. Yet, that obamium looks very tempting to take")

#                 obamium_choice = input("Back at her castle, you make a plan to take the obamium at night. Do you 1=procceed with the plan, 2=save it for later, or 3=gonna give it up, let it down, run around, and desert it? ")

#                 if obamium_choice == "1":
#                     print("Spectacular! you have aquired the rarest material of the planet: THE OBAMIUM.")

#                     escape_choice = input("Now you must run. Do you decide to escape through the 1=the window, 2=the trapdor, 3=the front gates with 39 guards, or 4=PORTAL. ")
                    
#                     if escape_choice == "4":
#                         print("""__________SUCCESS___________
#     You are now the most powerfull person on the planet. You decided to use the obamium to go back to monke and live your best life!""")

#                     elif escape_choice == "3":
#                         print("""__________SUCCESS____________
#     It was lucky that you found that sleeping potion that put all 39 guards into a deep sleep.""")
                        
#                     elif escape_choice == "1":
#                         print("""_________GAME OVER__________
#     You fall in a moat of crocodiles...""")
                        
#                     elif escape_choice == "2":
#                         print("""___________GAME OVER__________
#     You climb in to the dark chamber only to find your only source of light disappear as the door closes on you.""")
                    
#                 elif obamium_choice == "2":
#                     print("""__________GAME OVER___________
#     The princesses guards found it when you left the castle the following day and now your in prison for treason.""")
                    
#                 elif obamium_choice == "3":
#                     print("""__________SUCCESS...SORT OF____________
#     You remained honest and did not steal the obamium. You have been rewarded to go back home via magic potion but you feel sad that you did not get the obamium back. If only you could find the white door again and start over...oh wait""")
#                     #RESTART CODE?
                    
#             else:
#                 print("""_________GAME OVER___________
#     You sure lack curiosity :/""")

                
#         else:
#             print("""___________GAME OVER____________
#     Well, I guess your story ends here!""")