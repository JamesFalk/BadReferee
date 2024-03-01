import random
from tkinter import Tk, Canvas, NW, Button, Label
from PIL import Image, ImageTk
from pygame import mixer

# Initializing the Sound Mixer
mixer.init()

# Creating the Main Window
root = Tk(); root.title("Bad Referee")

# Create the Canvas
canvas = Canvas(root, width=300, height=450)
canvas.pack()

# Placing a Button on the Form
btnX = 110; btnY=10; btnW=8; btnH=2
btnPlayBall = Button(root, text="PlayBall", width=btnW, height=btnH)
btnPlayBall.place(x=btnX, y=btnY)

# Load and ReSize Image File
imgFile = "BadReferee.jpg"
imgX = 20; imgY = 60; imgW = 250; imgH = 200
image = Image.open(imgFile)
image = image.resize((imgW, imgH), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
# Draw image
canvas.create_image(imgX, imgY, anchor=NW, image=img)

# Placing the Label
lblX = 15; lblY = 265
lblBadRefCall = Label(root, text="- - -", wraplength=250)
lblBadRefCall.place(x=lblX, y=lblY)

# Naming the Variables
RfL = ["Psycho Ted", "Dumb Neddy", "Drunk Nelson", "Blind Lenny", "Sleepy Hecho",
       "Beligerant Barry", "Crooked Larry", "Super Thompson", "Honest Franky",
       "Goodshoes Bobby", "Mean Mattheson", "Obsessed Dingleton",
       "Obnoxious Pickleson", "Cranky Shortwall"]

PlL = ["Fatso Joe", "Turbo Freddy", "Idle Kip", "Dancey Duke", "High Nelly",
       "Sloppy Biff", "Goofy Johnson", "Juggalo Jerry", "Conniving Terrance", "Hyper Wangston"]

PtL = ["offsides", "unsportsmanlike conduct", "unnecessary roughness", "delay of game",
       "facemasking", "holding", "pass interference", "roughing the passer",
       "mowing the kicker", "punching the retriever", "illegal formation"]

DL = ["no", "5", "10", "15", "20", "30", "50"]

NdL = [" repeat first", " and its second", " and its third", " and its fourth", ", turnover on"]

def btnPlayBall_click(PlayBall):
       rf = round((len(RfL) - 1) * random.random())
       pl = round((len(PlL) - 1) * random.random())
       pt = round((len(PtL) - 1) * random.random())
       di = round((len(DL) - 1) * random.random())
       nd = round((len(NdL) - 1) * random.random())
       lblBadRefCall.config(text="Referee " + str(RfL[rf]) + " flags player " + str(PlL[pl]) + " on the play ... " \
                             + str(PtL[pt]) + ", a " + DL[di] + " yard penalty" + NdL[nd] + " down!")
       mixer.music.load('tweet.wav'); mixer.music.play()

btnPlayBall.bind("<Button-1>", btnPlayBall_click)

root.mainloop()