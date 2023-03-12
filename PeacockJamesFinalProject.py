#----------------------------------imports-------------------------------------------

from tkinter import * 
import random

#--------------------------main functions of the game--------------------------------

#player decision
def rock():
    global player
    player = 1
    computerChoice()
 
def paper():
    global player
    player = 2
    computerChoice()
 
def scissors():
    global player
    player = 3
    computerChoice()

#computer decision
def computerChoice():
    computer = random.randint(1,3) #Uses random to choose rock, paper, or scissors
    if computer == 1:
        computerRock()
    elif computer == 2:
        computerPaper() 
    elif computer == 3:
        computerScissor()

#outcomes of the game that also change the font color of the outcome label to display whether a win, loss, or tie occurred.  
def computerRock(): 
    if player == 1:
        outcome.config( text = "It's a tie!", fg = "black") 
        playerChose.config( text = "Player: Rock")
        computerChose.config( text = "Computer: Rock")

    elif player == 2:
        outcome.config( text = "You won!", fg = "green")
        playerChose.config( text = "Player: Paper")
        computerChose.config( text = "Computer: Rock")

    elif player == 3:
        outcome.config( text = "You lose!", fg = "red")
        playerChose.config( text = "Player: Scissors")
        computerChose.config( text = "Computer: Rock")
 
def computerPaper():
    if player == 1:
        outcome.config( text = "You lose!", fg = "red")
        playerChose.config( text = "Player: Rock")
        computerChose.config( text = "Computer: Paper")

    elif player == 2:
        outcome.config( text = "It's a tie!", fg = "black")
        playerChose.config( text = "Player: Paper")
        computerChose.config( text = "Computer: Paper")

    elif player == 3:
        outcome.config( text = "You won!", fg = "green")
        playerChose.config( text = "Player: Scissors")
        computerChose.config( text = "Computer: Paper")

 
def computerScissor():
    if player == 1:
        outcome.config( text = "You won!", fg = "green")
        playerChose.config( text = "Player: Rock")
        computerChose.config( text = "Player: Scissors")

    elif player == 2:
        outcome.config( text = "You lose!", fg = "red")
        playerChose.config( text = "Player: Paper")
        computerChose.config( text = "Player: Scissors")

    elif player == 3:
        outcome.config( text = "It's a tie!", fg = "black")
        playerChose.config( text = "Player: Scissors")
        computerChose.config( text = "Player: Scissors")

#closes application
def exitApp():
    home.destroy()
    exit()

#Gameplay Page
def startGame():
    game = Tk()
    game.title("New Game!")
    game.geometry("640x480")
   
    #displays the outcome of the game 
    global outcome
    outcome = Label(game, text = " ", font = ("Times New Roman", 20))
    outcome.pack( side = TOP, padx = 5, pady = 5)

    #Shows what the player chose
    global playerChose
    playerChose = Label(game, text = " ", font = ("Times New Roman", 20))
    playerChose.pack( side = LEFT)

    #Shows what the computer randomly chose
    global computerChose
    computerChose = Label(game, text = " ", font = ("Times New Roman", 20))
    computerChose.pack( side = RIGHT)

    global header
    header = Label(game, text = "CHOOSE \n YOUR \n WEAPON", font = ("Times New Roman", 20))
    header.pack( side = TOP, padx = 5, pady = 5)
    
    #Buttons to choose for gameplay
    global rockChoice
    rockChoice = Button(game, text = "Rock", font = ("Times New Roman", 12), command = rock).pack(padx = 5, pady = 20, anchor = "center")

    global paperChoice
    paperChoice = Button(game, text = "Paper", font = ("Times New Roman", 12), command = paper).pack(padx = 5, pady =20, anchor = "center")

    global scissorsChoice
    scissorsChoice = Button(game, text = "Scissors", font = ("Times New Roman", 12), command = scissors).pack(padx = 5, pady = 20, anchor = "center")

   

#Settings Message
def settings():
    empty = Tk()
    empty.title("Settings")
    setting = Message(empty, text = "Maybe the real settings were the friends we made along the way.", font = ("Times New Roman", 20)).pack()

#Scoreboard Message
def scoreboard():
    scores = Tk()
    scores.title("Scoreboard")
    positiveAffirmation = Message(scores, text = "Who keeps score when you're having fun?", font = ("Times New Roman", 16)).pack()

#------------------------------Interface-----------------------------------------


#Homepage
home = Tk()
home.title("Rock, Paper, Scissors...Reimagined?!?!")
home.geometry("640x480")
header = Label(home, text = "Rock, Paper, Scissors...Reimagined?!?!", font = ("Times New Roman", 16)).grid(row = 0, sticky = N , pady = 15, padx = 130)

#homepage buttons
newGame = Button(home, text = "New Game", font = ("Times New Roman", 12), command = startGame).grid(row = 1, sticky = N, pady = 15, padx = 130)

scoreboard = Button(home, text = "Scoreboard", font = ("Times New Roman", 12), command = scoreboard).grid(row = 2, sticky = N, pady = 15, padx = 130)

settings = Button(home, text = "Settings", font = ("Times New Roman", 12), command = settings).grid(row = 3, sticky = N, pady = 15, padx = 130)

exit = Button(home, text = "Exit", font = ("Times New Roman", 12), command = exitApp).grid(row = 4, sticky = N, pady = 15, padx = 130)


home.mainloop()















