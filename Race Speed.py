from tkinter import *
import tkinter as tk
import winsound
import random

class Home_Window:
        
    def __init__(self,master):

        
        #Play the music
        winsound.PlaySound("MusicProyect.wav",winsound.SND_LOOP | winsound.SND_ASYNC)
        
        #Main Window
        self.canvas = Canvas(master, width = 500, height = 600,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #Title "Race Speed"
        self.race = Label(self.canvas, text= "RACE", font=("fixedsys",56),fg="white",bg="black")
        self.race.place(x=180,y=10,width=150,height=70)

        self.speed = Label(self.canvas, text= "SPEED", font=("fixedsys",56),fg="red3",bg="black")
        self.speed.place(x=155,y=80,width=200,height=70)

        #Buttons
        self.play = Button(self.canvas, text = "PLAY", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.play)
        self.play.place(x=200,y=200,width=90,height=30)

        self.instr = Button(self.canvas, text = "INSTRUCTIONS", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.instructions)
        self.instr.place(x=145,y=260,width=210,height=30)

        self.highscore = Button(self.canvas, text = "HIGH SCORES", font=("fixedsys",18),fg="white",bg="black",borderwidth=0, command=self.highscores)
        self.highscore.place(x=160,y=320,width=180,height=30)

        self.credits = Button(self.canvas, text = "CREDITS", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.credits)
        self.credits.place(x=185,y=380,width=120,height=30)

        #Image Red Car
        self.redcar = PhotoImage(file = "Cars\RedCar.png")
        self.labelredcar = Label(image=self.redcar ,bg= "black")
        self.labelredcar.place(x=270, y=450, width=70, height=150)

        #Image Green Car
        self.greencar = PhotoImage(file = "Cars\GreenCar.png")
        self.labelgreencar = Label(image=self.greencar ,bg= "black")
        self.labelgreencar.place(x=140, y=450, width=70, height=150)

        #Image Blue Car
        self.bluecar = PhotoImage(file = "Cars\BlueCar.png")
        self.labelbluecar = Label(image=self.bluecar ,bg= "black")
        self.labelbluecar.place(x=20, y=450, width=70, height=150)
        
        #Image Yellow Car
        self.yellowcar = PhotoImage(file = "Cars\YellowCar.png")
        self.labelyellowcar = Label(image=self.yellowcar ,bg= "black")
        self.labelyellowcar.place(x=390, y=450, width=70, height=150)


    #Button Play pressed
    def play(self):
        Name_Win()

    #Button Instructions pressed
    def instructions(self):
        Instr_Win()

    #Button Highscore pressed
    def highscores(self):
        HighSc_Win()

    #Button Credits pressed
    def credits(self):
        Credits_Win()


#Name window
class Name_Win:

    def __init__(self):
        self.canvas = Canvas(window,width = 500, height = 600,
                             highlightthickness = 0, relief='ridge')

        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')


        #Title "Race Speed"
        self.race = Label(self.canvas, text= "RACE", font=("fixedsys",56),fg="white",bg="black")
        self.race.place(x=180,y=10,width=150,height=70)

        self.speed = Label(self.canvas, text= "SPEED", font=("fixedsys",56),fg="red3",bg="black")
        self.speed.place(x=155,y=80,width=200,height=70)
        
        #Insert the name
        self.insnom = Label(self.canvas, text= "INSERT YOUR NAME", font=("fixedsys",20),fg="white",bg="black")
        self.insnom.place(x=100,y=150,width=300,height=70)

        self.entryname = Entry(self.canvas,font=("fixedsys",20),fg="white",bg="black")
        self.entryname.place(x=160, y=250, width=180, height=40)

        #Play Button
        self.play = Button(self.canvas, text = "PLAY", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.play)
        self.play.place(x=200,y=400,width=90,height=30)

        #Back Button
        self.backbutton = Button(self.canvas, text = "BACK", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbutton.place(x=200,y=450,width=90,height=30)

        
        
    #Calling the function to play
    def play(self):
        name = self.entryname.get()
        self.file = open("Highscore.txt","a")
        self.file.write(name + " ")
        self.file.close()
        Game_Win(name)

    def backbutton(self):
        self.canvas.destroy()
        

#Game Window
class Game_Win:

    

    def __init__(self,name):

        self.canvas = Canvas(window, width = 500, height = 600,
                             highlightthickness = 0, relief='ridge')


        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')
        
        #Title "Race Speed"
        self.race = Label(self.canvas, text= "RACE", font=("fixedsys",20),fg="white",bg="black")
        self.race.place(x=10,y=10,width=70,height=30)

        self.speed = Label(self.canvas, text= "SPEED", font=("fixedsys",20),fg="red3",bg="black")
        self.speed.place(x=10,y=40,width=75,height=30)

        #Name title
        self.name = Label(self.canvas, text= name, font=("fixedsys",20),fg="red3",bg="black")
        self.name.place(x=350,y=400,width=150,height=30)

        #Hp Title
        self.life = 3
        
        self.hp = Label(self.canvas, text= "HP:" + str(self.life), font=("fixedsys",20),fg="white",bg="black")
        self.hp.place(x=350,y=450,width=70,height=30)
        
        #Time Title
        self.time = 0
        self.timelab = Label(self.canvas, text= "TIME:" + str(self.time), font=("fixedsys",20),fg="white",bg="black")
        self.timelab.place(x=345,y=30,width=140,height=30)
        self.timer()

        #Score Title
        self.score2 = 0
        self.scorelab = Label(self.canvas, text= "SCORE:" + str(self.score2), font=("fixedsys",20),fg="white",bg="black")
        self.scorelab.place(x=140,y=30,width=200,height=30)
        self.score()

        
        #Photo of the Highway
        self.img = PhotoImage(file = "Highway.png")
        self.highway = self.canvas.create_image(0,600, anchor=SW, image=self.img)

        
        #Photo of the Red car
        self.img1 = PhotoImage(file = "Cars\RedCar.png")
        self.redcar = self.canvas.create_image(135,500, anchor=SW, image=self.img1)


        #Loading the other cars
        self.img2 = PhotoImage(file = "Cars\GreenCar.png")
        self.img3 = PhotoImage(file = "Cars\BlueCar.png")
        self.img4 = PhotoImage(file = "Cars\YellowCar.png")
        self.img5 = PhotoImage(file = "Cars\WhiteCar.png")

        #Calling "Game"
        self.game()
        
        #Instructions to move with the keys
        window.bind("<KeyPress-Left>" , lambda x: self.left(x))
        window.bind("<KeyPress-Right>" , lambda x: self.right(x))
        window.bind("<KeyPress-Up>", lambda x: self.up(x))
        window.bind("<KeyPress-Down>",lambda x: self.down(x))

        
    #Loop to the timer
    def timer(self):
        if self.life == 0:
            True
        else:
            self.time += 1
            self.timelab.config(text="TIME:" +str(self.time))
            window.after(1000,self.timer)
    
    #Loop to the score
    def score(self):
        if self.life == 0:
            True
        else:
            self.score2 += 5
            self.scorelab.config(text="SCORE:" + str(self.score2))
            window.after(1000,self.score)

    #The Game        
    def game(self):
        if self.life == 0:
            self.gameover = Label(self.canvas, text= "GAME OVER", font=("fixedsys",30),fg="white",bg="black")
            self.gameover.place(x=55,y=160,width=230,height=70)

            self.yourscore = Label(self.canvas, text= "YOUR SCORE:" + str(self.score2), font=("fixedsys",20),fg="white",bg="black")
            self.yourscore.place(x=35,y=250,width=280,height=40)

            self.file = open("Highscore.txt","a")
            self.file.write(str(self.score2) + '\n')
            self.file.close()

            #Back Button
            self.backbutton = Button(self.canvas, text = "BACK", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.backbutton)
            self.backbutton.place(x=120,y=320,width=90,height=30)

        #Showing the cars randomly   
        else:
            num = random.randint(1,4)
            if num == 1:
                ran = random.randint(60,270)
                self.greencar = self.canvas.create_image(ran,90, anchor=N, image=self.img2)
                window.after(1000,self.moving_greencar)

            if num == 2:
                ran = random.randint(60,270)
                self.bluecar = self.canvas.create_image(ran,90, anchor=N, image=self.img3)
                window.after(1000,self.moving_bluecar)

            if num == 3:
                ran = random.randint(60,270)
                self.yellowcar = self.canvas.create_image(ran,90, anchor=N, image=self.img4)
                window.after(1000,self.moving_yellowcar)

            if num == 4:
                ran = random.randint(60,270)
                self.whitecar = self.canvas.create_image(ran,90, anchor=N, image=self.img5)
                window.after(1000,self.moving_whitecar)
                

#Movement of the white car    
    def moving_whitecar(self):
        
        x,y = self.canvas.coords(self.whitecar)

        #Box of the green car
        bwc = self.canvas.bbox(self.whitecar)

        #Box of the red car
        brc = self.canvas.bbox(self.redcar)
        
        if y > 500:
            self.canvas.delete(self.whitecar)
            window.after(100,self.game())

        elif bwc[0]< brc[2] < bwc[2] and bwc[1] < brc[1] < bwc[3] or bwc[0]< brc[0] < bwc[2] and bwc[1] < brc[1] < bwc[3] or bwc[0]< brc[2] < bwc[2] and bwc[1] < brc[3] < bwc[3] or bwc[0]< brc[0] < bwc[2] and bwc[1] < brc[3] < bwc[3]:
            self.canvas.delete(self.whitecar)
            if self.life == 1:
                self.life -=1
                self.hp.config(text="HP:" + str(self.life))
                window.after(1000,self.game())
                
            else:                   
                self.life -=2
                self.hp.config(text="HP:" + str(self.life))
                window.after(1000,self.game())

        else:
            self.x = 0
            self.y = 35
            self.canvas.move(self.whitecar,self.x,self.y)
            window.after(400,self.moving_whitecar)
            
        
#Movement of the yellow car
    def moving_yellowcar(self):
        x,y = self.canvas.coords(self.yellowcar)
        
        if y > 500:
            self.canvas.delete(self.yellowcar)
            window.after(100,self.game())

        else:
            if x < 60:
                self.right_yellow()
                    
            elif x > 275:
                self.left_yellow()

            else:
                self.x = 40
                self.y = 35
                self.canvas.move(self.yellowcar,self.x,self.y)
                window.after(400,self.moving_yellowcar)

    def right_yellow(self):
        #Box of the yellow car
        byc = self.canvas.bbox(self.yellowcar)

        #Box of the red car
        brc = self.canvas.bbox(self.redcar)
        
        x,y = self.canvas.coords(self.yellowcar)
        if x > 275:
            self.x = -35
            self.y = 35
            self.canvas.move(self.yellowcar,self.x,self.y)
            window.after(400,self.moving_yellowcar)

        elif byc[0]< brc[2] < byc[2] and byc[1] < brc[1] < byc[3] or byc[0]< brc[0] < byc[2] and byc[1] < brc[1] < byc[3] or byc[0]< brc[2] < byc[2] and byc[1] < brc[3] < byc[3] or byc[0]< brc[0] < byc[2] and byc[1] < brc[3] < byc[3]:
            self.canvas.delete(self.yellowcar)
            self.life -= 1
            self.hp.config(text="HP:" + str(self.life))
            window.after(100,self.game())

        else:
            self.x = 35
            self.y = 35
            self.canvas.move(self.yellowcar,self.x,self.y)
            window.after(400,self.right_yellow)

    def left_yellow(self):
        #Box of the yellow car
        byc = self.canvas.bbox(self.yellowcar)

        #Box of the red car
        brc = self.canvas.bbox(self.redcar)
        
        x,y = self.canvas.coords(self.yellowcar)
        if x < 60:
            self.x = 35
            self.y = 35
            self.canvas.move(self.yellowcar,self.x,self.y)
            window.after(400,self.moving_yellowcar)

        elif byc[0]< brc[2] < byc[2] and byc[1] < brc[1] < byc[3] or byc[0]< brc[0] < byc[2] and byc[1] < brc[1] < byc[3] or byc[0]< brc[2] < byc[2] and byc[1] < brc[3] < byc[3] or byc[0]< brc[0] < byc[2] and byc[1] < brc[3] < byc[3]:
            self.canvas.delete(self.yellowcar)
            self.life -= 1
            self.hp.config(text="HP:" + str(self.life))
            window.after(100,self.game())
                        
        else:
            self.x = -35
            self.y = 35
            self.canvas.move(self.yellowcar,self.x,self.y)
            window.after(400,self.left_yellow)
            

#Movement of the bluecar        
    def moving_bluecar(self):
        x,y = self.canvas.coords(self.bluecar)

        #Box of the blue car
        bbc = self.canvas.bbox(self.bluecar)

        #Box of the red car
        brc = self.canvas.bbox(self.redcar)
        
        if y > 500:
            self.canvas.delete(self.bluecar)
            window.after(100,self.game())

        elif bbc[0]< brc[2] < bbc[2] and bbc[1] < brc[1] < bbc[3] or bbc[0]< brc[0] < bbc[2] and bbc[1] < brc[1] < bbc[3] or bbc[0]< brc[2] < bbc[2] and bbc[1] < brc[3] < bbc[3] or bbc[0]< brc[0] < bbc[2] and bbc[1] < brc[3] < bbc[3]:
            self.canvas.delete(self.bluecar)
            self.score2 += 500
            self.scorelab.config(text="SCORE:" + str(self.score2))
            window.after(100,self.game())

        else:
            self.x = 0
            self.y = 35
            self.canvas.move(self.bluecar,self.x,self.y)
            window.after(400,self.moving_bluecar)
            
            
                
#Movement of the green car      
    def moving_greencar(self):
        
        x,y = self.canvas.coords(self.greencar)

        #Box of the green car
        bgc = self.canvas.bbox(self.greencar)

        #Box of the red car
        brc = self.canvas.bbox(self.redcar)
        
        if y > 500:
            self.canvas.delete(self.greencar)
            window.after(100,self.game())

        elif bgc[0]< brc[2] < bgc[2] and bgc[1] < brc[1] < bgc[3] or bgc[0]< brc[0] < bgc[2] and bgc[1] < brc[1] < bgc[3] or bgc[0]< brc[2] < bgc[2] and bgc[1] < brc[3] < bgc[3] or bgc[0]< brc[0] < bgc[2] and bgc[1] < brc[3] < bgc[3]:
            self.canvas.delete(self.greencar)
            self.life -=1
            self.hp.config(text="HP:" + str(self.life))
            window.after(100,self.game())

        else:
            self.x = 0
            self.y = 35
            self.canvas.move(self.greencar,self.x,self.y)
            window.after(400,self.moving_greencar)
    
            

#Movement of the red car
    def left(self,event):
        x, y = self.canvas.coords(self.redcar)
        if x < 5:
            self.x = 0
            self.y = 0
            self.canvas.move(self.redcar,self.x,self.y)
        else:
            self.x = -5
            self.y = 0
            self.canvas.move(self.redcar,self.x,self.y)
        

    def right(self,event):
        x, y = self.canvas.coords(self.redcar)
        if x > 275:
            self.x = 0
            self.y = 0
            self.canvas.move(self.redcar,self.x,self.y)
        else:
            self.x = 5
            self.y = 0
            self.canvas.move(self.redcar,self.x,self.y)

    def up(self,event):
        x, y = self.canvas.coords(self.redcar)
        if y < 175:
            self.x = 0
            self.y = 0
            self.canvas.move(self.redcar,self.x,self.y)
        else:
            self.x = 0
            self.y = -5
            self.canvas.move(self.redcar,self.x,self.y)

    def down(self,event):
        x, y = self.canvas.coords(self.redcar)
        if y > 590:
            self.x = 0
            self.y = 0
            self.canvas.move(self.redcar,self.x,self.y)
        else:
            self.x = 0
            self.y = 5
            self.canvas.move(self.redcar,self.x,self.y)

    def backbutton(self):
        self.canvas.destroy()
        
                
#Instructions
class Instr_Win:

    def __init__(self):
        self.canvas = Canvas(window,width = 500, height = 600,
                             highlightthickness = 0, relief='ridge')

        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        self.title = Label(self.canvas, text= "INSTRUCTIONS", font=("fixedsys",30),fg="white",bg="black")
        self.title.place(x=100,y=10,width=300,height=70)

        #Intructions for the controls
        self.firstint = Label(self.canvas, text="Controls for the car: UP, DOWN, RIGHT, LEFT",font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.firstint.place(x=20,y=80,width=345,height=30)

        self.up = Label(self.canvas,text = "UP = FORWARD", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.up.place(x=40,y=100,width=95,height=30)

        self.down = Label(self.canvas,text = "DOWN = BRAKE", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.down.place(x=40,y=120,width=95,height=30)


        self.right = Label(self.canvas,text = "RIGHT = GOES TO THE RIGHT", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.right.place(x=40,y=140,width=200,height=30)

        self.left = Label(self.canvas,text = "LEFT = GOES TO THE LEFT", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.left.place(x=41,y=160,width=185,height=30)

        #Intructions for the blue car
        self.bluecarinst = Label(self.canvas,text = "BLUE CAR:", font=("fixedsys",16),fg="blue",bg="black",borderwidth=0)
        self.bluecarinst.place(x=15,y=200,width=90,height=30)

        self.bluecardef = Label(self.canvas,text = "will give you 500 points.", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.bluecardef.place(x=100,y=197,width=200,height=35)

        #Instructions for the green car
        self.greencarinst = Label(self.canvas,text = "GREEN CAR:", font=("fixedsys",16),fg="green",bg="black",borderwidth=0)
        self.greencarinst.place(x=19,y=240,width=90,height=30)

        self.greencardef = Label(self.canvas,text = "will make you lose 1 HP. This car", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.greencardef.place(x=105,y=240,width=270,height=30)

        self.greencardef2 = Label(self.canvas,text = "will move in a straight line.", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.greencardef2.place(x=110,y=260,width=230,height=30)

        #Instructions for the purple car
        self.purplecarinst = Label(self.canvas,text = "YELLOW CAR:", font=("fixedsys",16),fg="yellow",bg="black",borderwidth=0)
        self.purplecarinst.place(x=25,y=300,width=90,height=30)

        self.purplecardef = Label(self.canvas,text = "will make you lose 1 HP. This car", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.purplecardef.place(x=115,y=300,width=270,height=30)

        self.purplecardef2 = Label(self.canvas,text = "will move from left to right.", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.purplecardef2.place(x=120,y=320,width=230,height=30)

        #Instructions for the truck
        self.truckinst = Label(self.canvas,text = "WHITE CAR:", font=("fixedsys",16),fg="skyblue",bg="black",borderwidth=0)
        self.truckinst.place(x=21,y=360,width=90,height=30)

        self.truckdef = Label(self.canvas,text = "will make you lose 2 HP. This car", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.truckdef.place(x=115,y=360,width=270,height=30)
        
        self.truckdef2 = Label(self.canvas,text = "will move in a straight line.", font=("fixedsys",16),fg="white",bg="black",borderwidth=0)
        self.truckdef2.place(x=120,y=380,width=230,height=30)

        #Back Button
        self.backbutton = Button(self.canvas, text = "BACK", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbutton.place(x=195,y=500,width=90,height=30)

    def backbutton(self):
        self.canvas.destroy()

#HIGH SCORES
class HighSc_Win:
    def __init__(self):
        self.canvas = Canvas(window,width = 500, height = 600,
                             highlightthickness = 0, relief='ridge')
        
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        self.file = open("Highscore.txt")

        self.highscores = Label(self.canvas,text = self.file.read(), font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.highscores.place(x=0,y=0,width=500,height=400)

        #Title "Race Speed"
        self.race = Label(self.canvas, text= "HIGH", font=("fixedsys",56),fg="white",bg="black")
        self.race.place(x=180,y=10,width=150,height=70)

        self.speed = Label(self.canvas, text= "SCORES", font=("fixedsys",56),fg="red3",bg="black")
        self.speed.place(x=135,y=80,width=250,height=70)

        #Back Button
        self.backbuttonins = Button(self.canvas, text = "BACK", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbuttonins.place(x=195,y=450,width=90,height=30)


    def backbutton(self):
        self.canvas.destroy()

#CREDITS
class Credits_Win:

    def __init__(self):
        self.canvas = Canvas(window,width = 500, height = 600,
                             highlightthickness = 0, relief='ridge')
        
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        
        #All the credits
        self.country = Label(self.canvas,text = "COSTA RICA", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.country.place(x=10,y=10,width=160,height=30)       

        self.university = Label(self.canvas,text = "ITCR", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.university.place(x=10,y=50,width=60,height=30)
        
        self.career = Label(self.canvas,text = "COMPUTER ENGINEERING", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.career.place(x=10,y=90,width=317,height=30)

        self.professor = Label(self.canvas,text = "PROF. LUIS BARBOZA ARTAVIA", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.professor.place(x=10,y=130,width=420,height=30)

        self.version = Label(self.canvas,text = "TKINTER PYTHON (3.8.1)", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.version.place(x=15,y=170,width=345,height=30)

        self.author = Label(self.canvas,text = "GONZALO ACUÑA MADRIGAL", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.author.place(x=15,y=210,width=347,height=30)

        self.year = Label(self.canvas,text = "2020", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.year.place(x=15,y=250,width=65,height=30)

        self.credits = Label(self.canvas,text = "-------------CREDITS-------------", font=("fixedsys",20),fg="white",bg="black",borderwidth=0)
        self.credits.place(x=-60,y=330,width=600,height=30)

        #Back Button
        self.backbuttonins = Button(self.canvas, text = "BACK", font=("fixedsys",18),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbuttonins.place(x=195,y=450,width=90,height=30)


    def backbutton(self):
        self.canvas.destroy()

           
if __name__ == "__main__":
    window = Tk()
    home_window = Home_Window(window)
    window.title("Race Speed")
    window.minsize(500,600)
 
    window.mainloop()
