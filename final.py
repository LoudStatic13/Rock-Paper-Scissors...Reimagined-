#----------------------------------imports-------------------------------------------

from tkinter import * 
import random
from PIL import Image, ImageTk

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
 
def scissor():
    global player
    player = 3
    computerChoice()

#computer decision
def computerChoice():
    computer = random.randint(1,3)
    if computer == 1:
        computerRock()
    elif computer == 2:
        computerPaper() 
    elif com_choice == 3:
        computerScissor()

#outcomes of the game 
def computerRock():
    if player == 1:
        outcome.config(text="It's a tie!")
    elif player == 2:
        outcome.config(text="You won!")
    elif player == 3:
        outcome.config(text="You lose!")
 
def computerPaper():
    if player == 1:
        outcome.config(text="You lose!")
    elif player == 2:
        outcome.config(text="It's a tie!")
    elif player == 3:
        outcome.config(text="You won!")
 
def computerScissor():
    if player == 1:
        outcome.config(text="You won!")
    elif player == 2:
        outcome.config(text="You lose!")
    elif player == 3:
        outcome.config(text="It's a tie!")
 
def exitApp():
    root.destroy()
    exit()

#---------------------------Windows-----------------------------------------

#Homepage
home = Tk()
home.title("Rock, Paper, Scissors...Reimagined?!?!")
home.geometry("640x480")

#Labels
Label(home,text = "Rock, Paper, Scissors...Reimagined?!?!", font = ("TimesNewRoman",16)).grid(row = 0, sticky = N , pady = 15, padx = 130)

#Buttons
newGame = Button(home, text = "New Game", font = ("TimesNewRoman", 12)).grid(row = 1, sticky = N, pady = 15, padx = 130)
scoreboard = Button(home, text = "Scoreboard", font = ("TimesNewRoman", 12)).grid(row = 2, sticky = N, pady = 15, padx = 130)
settings = Button(home, text = "Settings", font = ("TimesNewRoman", 12)).grid(row = 3, sticky = N, pady = 15, padx = 130)



home.mainloop()













