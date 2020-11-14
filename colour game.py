from tkinter import *
import random

colours = ["Red", "Blue", "Pink", "Green", "Purple", "Brown","Black", "Orange", "Yellow", "White"]
score=0
timeLeft=30

def startGame(event):
    if timeLeft == 30:
        countdown()
    nextColour()

def nextColour():
    global timeLeft
    global score

    if timeLeft>0:
        entry.focus_set()

    if entry.get().lower() == colours[0].lower():
        score+=1

    entry.delete(0,END)
    random.shuffle(colours)
    label.config(fg=colours[0], text=colours[1])
    scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeLeft
    if timeLeft>0:
        timeLeft-=1
    timeLabel.config(text="Game will be over in:" + str(timeLeft))
    timeLabel.after(1000,countdown)




root=Tk()
root.title("Colour Game")

instructionsLabel = Label(root, text="Type in the colour of the word and not the word text!")
instructionsLabel.pack()

scoreLabel= Label(root, text="Press enter to start", font=("Helvetica",12))
scoreLabel.pack()

timeLabel = Label(root, text="Time Left: " +str(timeLeft) )
timeLabel.pack()

label=Label(root, font=('Helvetica',60))
label.pack()

entry=Entry(root)
root.bind('<Return>', startGame)
entry.pack()
entry.focus_set()

root.mainloop()