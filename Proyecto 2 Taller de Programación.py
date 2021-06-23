from tkinter import *
import random
import pygame


#Main class definition
class Main_window:
    def __init__(self, master):
        
        self.master = master
        self.canvas = Canvas(master, width=800, height=800) 
        self.canvas.pack(fill=BOTH, expand = YES)
        
        #Initial configurations for the menu's canvas
        self.Menu()
        
    def Menu(self):
        #Main Menu ambiental sounds
        pygame.mixer.music.load("Recording (3).mp3")
        pygame.mixer.music.play()
        #Main Menu canvas is shown
        self.canvas = Canvas(self.master, width=1000, height=800) 
        self.canvas.place(x=0,y=0)
        
        #Create Background for menu
        self.canvas.create_image(0,0, image = BG, anchor="nw")
        
        #Welcome message
        self.canvas.create_text(400,80,text= "Welcome to Moon Light", font=("Rocks__G", 42), fill="white")
        self.canvas.create_text(200, 690, text="Enter your nickname:", font= ("Arial", 26),fill="white")

        #Player name entry
        self.player= Entry(self.master)
        self.player.window = self.canvas.create_window(200, 720, window=self.player, width= 300)
        self.nameFlag=False

        #Level 1 button
        self.Level1_button= Button(self.canvas,bg="slate blue", text="Level_1", font=("Rocks__G", 22), fg="White", command=self.Level_1)
        self.Level1_button.place(x=100, y=450)

        #Level 2 button
        self.Level2_button= Button(self.canvas,bg="slate blue", text="Level_2", font=("Rocks__G", 22), fg="White", command=self.Level_2)
        self.Level2_button.place(x=480, y=275)

        #Level 3 button
        self.Level3_button= Button(self.canvas,bg="slate blue", text="Level_3", font=("Rocks__G", 22), fg="White", command=self.Level_3)
        self.Level3_button.place(x= 500, y= 550)

        #Credits window button
        self.Credits_button= Button(self.canvas,bg="slate blue", text="Credits", font=("Rocks__G", 22), fg="White", command=self.Credits)
        self.Credits_button.place(x=600, y=660)

        #Leader Board window button
        self.Leaderboard_button= Button(self.canvas,bg="slate blue", text="Ranking", font=("Rocks__G", 22), fg="White", command=self.Leaderboard)
        self.Leaderboard_button.place(x=400, y=460)

        #Defines game score as a global int for all levels
        self.Score=0
        
    def Credits(self):
        #Credits canvas is created
        self.canvasC = Canvas(self.master,width=800, height=1000)
        self.canvasC.place(x=0, y=0)
        
        #Developer's Country info
        self.Country= Label(self.canvasC, text="Costa Rica", font=("Arial", 22))
        self.Country.place(x=300, y=25)
        
        #Developer's College info
        self.College= Label(self.canvasC, text="Tecnológico de Costa Rica", font=("Arial", 22))
        self.College.place(x=200, y=75)

        #Developer's Carreer info
        self.Carreer= Label(self.canvasC, text="Ingeniería en Computadores", font=("Arial", 22))
        self.Carreer.place(x=200, y=125)

        #Developer's Class info
        self.Class_info= Label(self.canvasC, text="Taller de Programación, 2021, Grupo 04", font=("Arial", 22))
        self.Class_info.place(x=125, y=175)

        #Professor's info
        self.Professor= Label(self.canvasC, text="Luis Barboza Artavia", font=("Arial", 22))
        self.Professor.place(x=250, y=225)
        
        #Developer's name
        self.Author= Label(self.canvasC, text="Christopher Hidalgo Delgado", font=("Arial", 22))
        self.Author.place(x=200, y=375)
        
        #Button to return to main menu
        self.Menu_buttonC= Button(self.canvasC,text="Main Menu", command = self.closeall)
        self.Menu_buttonC.place(x=350, y=600)

    #Window for level1
    def Level_1(self):
        
        #Ambiental Music
        pygame.mixer.music.load("Recording (3).mp3")
        pygame.mixer.music.play()
        
        #Creates a flag to validate if a name already exists for further levels
        self.nameFlag = True
        
        #Gets the player's name entry info
        self.name = self.player.get()
        
        #Creates the window canvas for Level1
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        
        #Creates the player's space ship and it's intial coordinates
        self.ship= PhotoImage(file="Nave2.png")
        self.ship_1= self.canvas.create_image(450,720, image= self.ship)
        self.ship_coords = self.canvas.coords(self.ship_1)

        #Creates the meteorites and their bboxes
        self.meteorite=PhotoImage(file="Meteorito1.png")
        self.meteorite_1= self.canvas.create_image(450,220, image= self.meteorite)
        self.mb1= self.canvas.bbox(self.meteorite_1)
        self.meteorite_2= self.canvas.create_image(250,220, image= self.meteorite)
        self.mb2= self.canvas.bbox(self.meteorite_2)
        self.meteorite_3= self.canvas.create_image(450,120, image= self.meteorite)
        self.mb3= self.canvas.bbox(self.meteorite_3)

        #Player life is defined and labels with this info are created.
        self.Life_ship1= 3
        self.Life_ship1I = Label(self.canvas,text="P:",font=("Arial", 20))
        self.Life_ship1I.place(x=650, y=660)
        self.Life_shipL = Label(self.canvas,text="3",font=("Arial", 20))
        self.Life_shipL.place(x=700, y=660)

        #Label for the score
        self.ScoreL=Label(self.canvas,text="Score: 0",font=("Arial", 20))
        self.ScoreL.place(x=40, y=700)

        #Label for the player's name
        self.Player_name =Label(self.canvas, text=self.name, font=("Arial", 20))
        self.Player_name.place (x=700, y=700)

        #Label for the timer(seconds)
        self.Second = Label(self.canvas,text="",font=("Arial", 20))
        self.Second.place(x=60, y=740)

        #Label for the timer(minutes)
        self.Minute = Label(self.canvas,text="",font=("Arial", 20))
        self.Minute.place(x=15, y=740)

        #Label for the timer(dots)
        self.dots = Label(self.canvas,text=":",font=("Arial", 20))
        self.dots.place(x=40, y=740)

        #Button to return to main menu
        self.Menu_button= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button.place(x=700,y=740)

        #Timer second and minute variables are defined
        self.minute= 0
        self.second= 0
        
        #Function for the timer
        def Timer():
            if self.minute<=60:
                self.second+=1
                self.Score+=1
                self.ScoreL.config(text="Score:"+str(self.Score))
                #When 1 minutes is passed, player advances to level2
                if self.second>=60:
                    self.canvas.destroy()
                    self.Level_2()
            self.canvas.after(1000,Timer)
            self.Second.config(text=self.second)
            self.Minute.config(text=self.minute)
        Timer()
        
#Flags for each meteorite movement and valitates it hasn't been destroyed by collision.
        #Meteorite 1
        self.moveR=True
        self.moveL=True
        self.moveU=True
        self.moveD=True
        self.m1Flag=True

        #Meteorite 2
        self.move2R=True
        self.move2L=True
        self.move2U=True
        self.move2D=True
        self.m2Flag=True

        #Meteorite 3
        self.move3R=True
        self.move3L=True
        self.move3U=True
        self.move3D=True
        self.m3Flag=True
    #Function to randomly generate a magnitude for the movement of each meteorite every time they colide with a border.
        def coord_generator():
            #Meteorite 1
            self.xm1 = random.randint(10,30)
            self.ym1 = random.randint(10,30)
            #Meteorite 2
            self.xm2 = random.randint(10,30)
            self.ym2 = random.randint(10,30)
            #Meteorite 3
            self.xm3 = random.randint(10,30)
            self.ym3 = random.randint(10,30)
            
    #Functions for the sound of each meteorite's collision with the borders
        #Meteorite 1
        def soundsm1():
            if self.meteorite1_coords[0]+self.xm1>750 or self.meteorite1_coords[0]-self.xm1 < 50 or self.meteorite1_coords[1]+self.ym1 > 750 or self.meteorite1_coords[1]-self.ym1 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 2
        def soundsm2():
            if self.meteorite2_coords[0]+self.xm2>750 or self.meteorite2_coords[0]-self.xm2 < 50 or self.meteorite2_coords[1]+self.ym2 > 750 or self.meteorite2_coords[1]-self.ym2 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 3
        def soundsm3():
            if self.meteorite3_coords[0]+self.xm3>750 or self.meteorite3_coords[0]-self.xm3 < 50 or self.meteorite3_coords[1]+self.ym3 > 750 or self.meteorite3_coords[1]-self.ym3 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()
    #Function for the movement of all the meteorites
        def move_meteorite():
            #Meteorite 1(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m1Flag==True:
                self.meteorite1_coords= self.canvas.coords(self.meteorite_1)
                if self.meteorite1_coords[0] < 750 and self.moveR == True:
                    self.canvas.move(self.meteorite_1,self.xm1,0)
                    self.m1b= self.canvas.bbox(self.meteorite_1)
                    soundsm1()
                else:
                    if self.meteorite1_coords[0] > 50 and self.moveL == True:
                        self.canvas.move(self.meteorite_1,-(self.xm1),0)
                        self.m1b= self.canvas.bbox(self.meteorite_1)
                        self.moveR = False
                        soundsm1()
                    else:
                        self.moveR=True
                if self.meteorite1_coords[1] < 750 and self.moveD == True:
                    self.canvas.move(self.meteorite_1,0,self.ym1)
                    self.m1b= self.canvas.bbox(self.meteorite_1)
                    soundsm1()
                else:
                    if self.meteorite1_coords[1] > 50 and self.moveU == True:
                        self.canvas.move(self.meteorite_1,0,-(self.ym1))
                        self.m1b= self.canvas.bbox(self.meteorite_1)
                        self.moveD = False
                        soundsm1()
                    else:
                        self.moveD=True
            #Meteorite 2(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m2Flag==True:   
                self.meteorite2_coords= self.canvas.coords(self.meteorite_2)
                if self.meteorite2_coords[0] < 750 and self.move2R == True:
                    self.canvas.move(self.meteorite_2,self.xm2,0)
                    self.m2b= self.canvas.bbox(self.meteorite_2)
                    soundsm2()
                else:
                    if self.meteorite1_coords[0] > 50 and self.move2L == True:
                        self.canvas.move(self.meteorite_2,-(self.xm2),0)
                        self.m2b= self.canvas.bbox(self.meteorite_2)
                        self.move2R = False
                        soundsm2()
                    else:
                        self.move2R=True
                if self.meteorite2_coords[1] < 750 and self.move2D == True:
                    self.canvas.move(self.meteorite_2,0,self.ym2)
                    self.m2b= self.canvas.bbox(self.meteorite_2)
                    soundsm2()
                else:
                    if self.meteorite2_coords[1] > 50 and self.move2U == True:
                        self.canvas.move(self.meteorite_2,0,-(self.ym2))
                        self.m2b= self.canvas.bbox(self.meteorite_2)
                        self.move2D = False
                        soundsm2()
                    else:
                        self.move2D=True
            #Meteorite 3(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m3Flag==True:
                self.meteorite3_coords= self.canvas.coords(self.meteorite_3)
                if self.meteorite3_coords[0] < 750 and self.move3R == True:
                    self.canvas.move(self.meteorite_3,self.xm3,0)
                    self.m3b= self.canvas.bbox(self.meteorite_3)
                    soundsm3()
                else:
                    if self.meteorite3_coords[0] > 50 and self.move3L == True:
                        self.canvas.move(self.meteorite_3,-(self.xm3),0)
                        self.m3b= self.canvas.bbox(self.meteorite_3)
                        self.move3R = False
                        soundsm3()
                    else:
                        self.move3R=True
                if self.meteorite3_coords[1] < 750 and self.move3D == True:
                    self.canvas.move(self.meteorite_3,0,self.ym3)
                    self.m3b= self.canvas.bbox(self.meteorite_3)
                    soundsm3()
                else:
                    if self.meteorite3_coords[1] > 50 and self.move3U == True:
                        self.canvas.move(self.meteorite_3,0,-(self.ym3))
                        self.m3b= self.canvas.bbox(self.meteorite_3)
                        self.move3D = False
                        soundsm3()
                    else:
                        self.move3D=True

            self.canvas.after(70,move_meteorite)
        coord_generator()
        move_meteorite()
        
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)
        #Move ship +y
        def up(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[1] > 80:
                x=0
                y=-10
                self.canvas.move(self.ship_1,x,y)
                
            if self.Life_ship1 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb[2]<self.m1b[2] and self.m1b[1]<self.sb[1]<self.m1b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb[2]<self.m2b[2] and self.m2b[1]<self.sb[1]<self.m2b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb[2]<self.m3b[2] and self.m3b[1]<self.sb[1]<self.m3b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)        
        #Move ship +x
        def right(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_1,x,y)

            if self.Life_ship1 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb[2]<self.m1b[2] and self.m1b[1]<self.sb[1]<self.m1b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb[2]<self.m2b[2] and self.m2b[1]<self.sb[1]<self.m2b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb[2]<self.m3b[2] and self.m3b[1]<self.sb[1]<self.m3b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)        
        #Move ship -x  
        def left(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_1,x,y)

            if self.Life_ship1 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb[2]<self.m1b[2] and self.m1b[1]<self.sb[1]<self.m1b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb[2]<self.m2b[2] and self.m2b[1]<self.sb[1]<self.m2b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb[2]<self.m3b[2] and self.m3b[1]<self.sb[1]<self.m3b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)       
        #Move ship -y   
        def down(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[1] < 720:
                x=0
                y=10
                self.canvas.move(self.ship_1,x,y)
                
            if self.Life_ship1 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb[2]<self.m1b[2] and self.m1b[1]<self.sb[1]<self.m1b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb[2]<self.m2b[2] and self.m2b[1]<self.sb[1]<self.m2b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb[2]<self.m3b[2] and self.m3b[1]<self.sb[1]<self.m3b[3]:
                        self.Life_ship1 -= 1
                        self.Life_shipL.config(text=str(self.Life_ship1))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                
        #Key bindings
        self.master.bind("<w>", up)
        self.master.bind("<d>", right)
        self.master.bind("<a>", left)
        self.master.bind("<s>", down)        

    #Window for Level2    
    def Level_2(self):
        #Ambiental Music
        pygame.mixer.music.load("Recording (3).mp3")
        pygame.mixer.music.play()
        #Validates if a name is already given from level1
        if self.nameFlag==False:
            self.name = self.player.get()
        else:
            self.nameFlag=True
        #Creates the window's canvas
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        
        #Creates the meteorites and their bboxes
        self.meteorite=PhotoImage(file="Meteorito1.png")
        self.meteorite_1= self.canvas.create_image(450,220, image= self.meteorite)
        self.mb1= self.canvas.bbox(self.meteorite_1)
        self.meteorite_2= self.canvas.create_image(250,220, image= self.meteorite)
        self.mb2= self.canvas.bbox(self.meteorite_2)
        self.meteorite_3= self.canvas.create_image(450,120, image= self.meteorite)
        self.mb3= self.canvas.bbox(self.meteorite_3)
        self.meteorite_4= self.canvas.create_image(650,220, image= self.meteorite)
        self.mb4= self.canvas.bbox(self.meteorite_4)

        #Creates the player's space ship and it's intial coordinates
        self.ship2= PhotoImage(file="Nave2.png")
        self.ship_2= self.canvas.create_image(450,720, image= self.ship2)
        self.ship_coords2 = self.canvas.coords(self.ship_2)

        #Player life is defined and labels with this info are created.
        self.Life_ship2 = 3
        self.Life_ship2I = Label(self.canvas,text="P:",font=("Arial", 20))
        self.Life_ship2I.place(x=650, y=660)
        self.Life_ship2L = Label(self.canvas,text="3",font=("Arial", 20))
        self.Life_ship2L.place(x=700, y=660)

        #Label for the score
        self.ScoreL2=Label(self.canvas,text="Score:"+str(self.Score),font=("Arial", 20))
        self.ScoreL2.place(x=40, y=700)

        #Label for the player's name
        self.Player_name2 =Label(self.canvas, text=self.name, font=("Arial", 20))
        self.Player_name2.place (x=700, y=700)

        #Label for the timer(seconds2)
        self.Second2 = Label(self.canvas,text="",font=("Arial", 20))
        self.Second2.place(x=60, y=740)

        #Label for the timer(minutes2)
        self.Minute2 = Label(self.canvas,text="",font=("Arial", 20))
        self.Minute2.place(x=15, y=740)

        #Label for the timer(dots2)
        self.dots2 = Label(self.canvas,text=":",font=("Arial", 20))
        self.dots2.place(x=40, y=740)

        #Button to return to main menu
        self.Menu_button2= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button2.place(x=700,y=740)

        #Timer second2 and minute2 variables are defined
        self.minute2= 0
        self.second2= 0
        #Function for the timer
        def Timer2():
            if self.minute2<=60:
                self.second2+=1
                self.Score+=3
                self.ScoreL2.config(text="Score:"+str(self.Score))
                #When 1 minutes is passed, player advances to level3
                if self.second2>=60:
                    self.Level_3()
            self.canvas.after(1000,Timer2)
            self.Second2.config(text=self.second2)
            self.Minute2.config(text=self.minute2)
        Timer2()

#Flags for each meteorite movement and valitates it hasn't been destroyed by collision.
        #Meteorite 1
        self.moveR=True
        self.moveL=True
        self.moveU=True
        self.moveD=True
        self.m1Flag=True

        #Meteorite 2
        self.move2R=True
        self.move2L=True
        self.move2U=True
        self.move2D=True
        self.m2Flag=True

        #Meteorite 3
        self.move3R=True
        self.move3L=True
        self.move3U=True
        self.move3D=True
        self.m3Flag=True

        #Meteorite 4
        self.move4R=True
        self.move4L=True
        self.move4U=True
        self.move4D=True
        self.m4Flag=True
        
    #Function to randomly generate a magnitude for the movement of each meteorite every time they colide with a border.
        def coord_generator():
            #Meteorite 1
            self.xm1 = random.randint(10,30)
            self.ym1 = random.randint(10,30)
            #Meteorite 2
            self.xm2 = random.randint(10,30)
            self.ym2 = random.randint(10,30)
            #Meteorite 3
            self.xm3 = random.randint(10,30)
            self.ym3 = random.randint(10,30)
            #Meteorite 4
            self.xm4 = random.randint(10,30)
            self.ym4 = random.randint(10,30)
    #Functions for the sound of each meteorite's collision with the borders
        #Meteorite 1
        def soundsm1():
            if self.meteorite1_coords[0]+self.xm1>750 or self.meteorite1_coords[0]-self.xm1 < 50 or self.meteorite1_coords[1]+self.ym1 > 750 or self.meteorite1_coords[1]-self.ym1 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 2
        def soundsm2():
            if self.meteorite2_coords[0]+self.xm2>750 or self.meteorite2_coords[0]-self.xm2 < 50 or self.meteorite2_coords[1]+self.ym2 > 750 or self.meteorite2_coords[1]-self.ym2 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 3
        def soundsm3():
            if self.meteorite3_coords[0]+self.xm3>750 or self.meteorite3_coords[0]-self.xm3 < 50 or self.meteorite3_coords[1]+self.ym3 > 750 or self.meteorite3_coords[1]-self.ym3 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 4
        def soundsm4():
            if self.meteorite4_coords[0]+self.xm4>750 or self.meteorite4_coords[0]-self.xm4 < 50 or self.meteorite4_coords[1]+self.ym4 > 750 or self.meteorite4_coords[1]-self.ym4 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()
    #Function for the movement of all the meteorites
        def move_meteorite():
            #Meteorite 1(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m1Flag==True:
                self.meteorite1_coords= self.canvas.coords(self.meteorite_1)
                if self.meteorite1_coords[0] < 750 and self.moveR == True:
                    self.canvas.move(self.meteorite_1,self.xm1,0)
                    self.m1b= self.canvas.bbox(self.meteorite_1)
                    soundsm1()
                else:
                    if self.meteorite1_coords[0] > 50 and self.moveL == True:
                        self.canvas.move(self.meteorite_1,-(self.xm1),0)
                        self.m1b= self.canvas.bbox(self.meteorite_1)
                        self.moveR = False
                        soundsm1()
                    else:
                        self.moveR=True
                if self.meteorite1_coords[1] < 750 and self.moveD == True:
                    self.canvas.move(self.meteorite_1,0,self.ym1)
                    self.m1b= self.canvas.bbox(self.meteorite_1)
                    soundsm1()
                else:
                    if self.meteorite1_coords[1] > 50 and self.moveU == True:
                        self.canvas.move(self.meteorite_1,0,-(self.ym1))
                        self.m1b= self.canvas.bbox(self.meteorite_1)
                        self.moveD = False
                        soundsm1()
                    else:
                        self.moveD=True
            #Meteorite 2(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m2Flag==True:   
                self.meteorite2_coords= self.canvas.coords(self.meteorite_2)
                if self.meteorite2_coords[0] < 750 and self.move2R == True:
                    self.canvas.move(self.meteorite_2,self.xm2,0)
                    self.m2b= self.canvas.bbox(self.meteorite_2)
                    soundsm2()
                else:
                    if self.meteorite1_coords[0] > 50 and self.move2L == True:
                        self.canvas.move(self.meteorite_2,-(self.xm2),0)
                        self.m2b= self.canvas.bbox(self.meteorite_2)
                        self.move2R = False
                        soundsm2()
                    else:
                        self.move2R=True
                if self.meteorite2_coords[1] < 750 and self.move2D == True:
                    self.canvas.move(self.meteorite_2,0,self.ym2)
                    self.m2b= self.canvas.bbox(self.meteorite_2)
                    soundsm2()
                else:
                    if self.meteorite2_coords[1] > 50 and self.move2U == True:
                        self.canvas.move(self.meteorite_2,0,-(self.ym2))
                        self.m2b= self.canvas.bbox(self.meteorite_2)
                        self.move2D = False
                        soundsm2()
                    else:
                        self.move2D=True
            #Meteorite 3(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m3Flag==True:
                self.meteorite3_coords= self.canvas.coords(self.meteorite_3)
                if self.meteorite3_coords[0] < 750 and self.move3R == True:
                    self.canvas.move(self.meteorite_3,self.xm3,0)
                    self.m3b= self.canvas.bbox(self.meteorite_3)
                    soundsm3()
                else:
                    if self.meteorite3_coords[0] > 50 and self.move3L == True:
                        self.canvas.move(self.meteorite_3,-(self.xm3),0)
                        self.m3b= self.canvas.bbox(self.meteorite_3)
                        self.move3R = False
                        soundsm3()
                    else:
                        self.move3R=True
                if self.meteorite3_coords[1] < 750 and self.move3D == True:
                    self.canvas.move(self.meteorite_3,0,self.ym3)
                    self.m3b= self.canvas.bbox(self.meteorite_3)
                    soundsm3()
                else:
                    if self.meteorite3_coords[1] > 50 and self.move3U == True:
                        self.canvas.move(self.meteorite_3,0,-(self.ym3))
                        self.m3b= self.canvas.bbox(self.meteorite_3)
                        self.move3D = False
                        soundsm3()
                    else:
                        self.move3D=True
            if self.m4Flag==True:
                self.meteorite4_coords= self.canvas.coords(self.meteorite_4)
                if self.meteorite4_coords[0] < 750 and self.move4R == True:
                    self.canvas.move(self.meteorite_4,self.xm4,0)
                    self.m4b= self.canvas.bbox(self.meteorite_4)
                    soundsm4()
                else:
                    if self.meteorite4_coords[0] > 50 and self.move4L == True:
                        self.canvas.move(self.meteorite_4,-(self.xm4),0)
                        self.m4b= self.canvas.bbox(self.meteorite_4)
                        self.move4R = False
                        soundsm4()
                    else:
                        self.move4R=True
                #Meteorite 4(validates that the flag for existance is on and the position in case a sing swap is needed)
                if self.meteorite4_coords[1] < 750 and self.move4D == True:
                    self.canvas.move(self.meteorite_4,0,self.ym4)
                    self.m4b= self.canvas.bbox(self.meteorite_4)
                    soundsm4()
                else:
                    if self.meteorite4_coords[1] > 50 and self.move4U == True:
                        self.canvas.move(self.meteorite_4,0,-(self.ym4))
                        self.m4b= self.canvas.bbox(self.meteorite_4)
                        self.move4D = False
                        soundsm4()
                    else:
                        self.move4D=True
                    
            
            
            self.canvas.after(70,move_meteorite)
        coord_generator()
        move_meteorite()
        
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)
        #Move ship +y
        def up2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            if self.ship_coords2[1] > 80:
                x=0
                y=-10
                self.canvas.move(self.ship_2,x,y)
                
            if self.Life_ship2 <= 0:
                self.canvas.destroy()
                
            else:

                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb2[2]<self.m1b[2] and self.m1b[1]<self.sb2[1]<self.m1b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb2[2]<self.m2b[2] and self.m2b[1]<self.sb2[1]<self.m2b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb2[2]<self.m3b[2] and self.m3b[1]<self.sb2[1]<self.m3b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb2[2]<self.m4b[2] and self.m4b[1]<self.sb2[1]<self.m4b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)
        #Move ship +x
        def right2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            
            if self.ship_coords2[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_2,x,y)
                
            if self.Life_ship2 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb2[2]<self.m1b[2] and self.m1b[1]<self.sb2[1]<self.m1b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb2[2]<self.m2b[2] and self.m2b[1]<self.sb2[1]<self.m2b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb2[2]<self.m3b[2] and self.m3b[1]<self.sb2[1]<self.m3b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb2[2]<self.m4b[2] and self.m4b[1]<self.sb2[1]<self.m4b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)        
        #Move ship -x  
        def left2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            if self.ship_coords2[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_2,x,y)
                
            if self.Life_ship2 <= 0:
                self.canvas.destroy()
                
            else:

                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb2[2]<self.m1b[2] and self.m1b[1]<self.sb2[1]<self.m1b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb2[2]<self.m2b[2] and self.m2b[1]<self.sb2[1]<self.m2b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb2[2]<self.m3b[2] and self.m3b[1]<self.sb2[1]<self.m3b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb2[2]<self.m4b[2] and self.m4b[1]<self.sb2[1]<self.m4b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
        #Player ship movement and collision detection(validates if there is a collision with the meteorites each time the player moves the ship)        
        #Move ship -y   
        def down2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            
            if self.Life_ship2 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb2[2]<self.m1b[2] and self.m1b[1]<self.sb2[1]<self.m1b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb2[2]<self.m2b[2] and self.m2b[1]<self.sb2[1]<self.m2b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb2[2]<self.m3b[2] and self.m3b[1]<self.sb2[1]<self.m3b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb2[2]<self.m4b[2] and self.m4b[1]<self.sb2[1]<self.m4b[3]:
                        self.Life_ship2 -= 1
                        self.Life_ship2L.config(text=str(self.Life_ship2))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
            
            
        #Key bindings
        self.master.bind("<w>", up2)
        self.master.bind("<d>", right2)
        self.master.bind("<a>", left2)
        self.master.bind("<s>", down2)        

    #Window for level3
    def Level_3(self):
        
        #Ambiental Music
        pygame.mixer.music.load("Recording (3).mp3")
        pygame.mixer.music.play()
        
        #Validates if a name is already given from level1 or level2
        if self.nameFlag==False:
            self.name = self.player.get()
            
        #Creates the window canvas for Level2
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)

        #Creates the player's space ship and it's coordinates
        self.ship3= PhotoImage(file="Nave2.png")
        self.ship_3= self.canvas.create_image(450,720, image= self.ship3)
        self.ship_coords3 = self.canvas.coords(self.ship_3)

        #Creates the meteorites and their bboxes
        self.meteorite=PhotoImage(file="Meteorito1.png")
        self.meteorite_1= self.canvas.create_image(450,220, image= self.meteorite)
        self.mb1= self.canvas.bbox(self.meteorite_1)
        self.meteorite_2= self.canvas.create_image(250,220, image= self.meteorite)
        self.mb2= self.canvas.bbox(self.meteorite_2)
        self.meteorite_3= self.canvas.create_image(450,120, image= self.meteorite)
        self.mb3= self.canvas.bbox(self.meteorite_3)
        self.meteorite_4= self.canvas.create_image(450,120, image= self.meteorite)
        self.mb4= self.canvas.bbox(self.meteorite_4)
        self.meteorite_5= self.canvas.create_image(450,120, image= self.meteorite)
        self.mb5= self.canvas.bbox(self.meteorite_5)

        #Player life is defined and labels with this info are created.
        self.Life_ship3= 3
        self.Life_ship3I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship3I.place(x=650, y=660)
        self.Life_ship3L = Label(self.canvas,text="3",font=("Arial", 22))
        self.Life_ship3L.place(x=700, y=660)

        #Label for the score
        self.ScoreL3 = Label(self.canvas,text="Score:"+str(self.Score),font=("Arial", 22))
        self.ScoreL3.place(x=40, y=700)

        #Label for the player's name
        self.Player_name3 =Label(self.canvas, text=self.name, font=("Arial", 22))
        self.Player_name3.place (x=700, y=700)

        #Label for the timer(seconds3)
        self.Second3 = Label(self.canvas,text="",font=("Arial", 22))
        self.Second3.place(x=60, y=740)

        #Label for the timer(minutes3)
        self.Minute3 = Label(self.canvas,text="",font=("Arial", 22))
        self.Minute3.place(x=15, y=740)

        #Label for the timer(dots3)
        self.dots3 = Label(self.canvas,text=":",font=("Arial", 22))
        self.dots3.place(x=40, y=740)

        #Button to return to main menu
        self.Menu_button= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button.place(x=700,y=740)

        #Timer second3 and minute3 variables are defined
        self.minute3= 0
        self.second3= 0

        #Fuction for the timer
        def Timer3():
            if self.minute3<=60:
                self.second3+=0
                self.Score+=5
                self.ScoreL3.config(text="Score:"+str(self.Score))
                #When 1 minutes is passed, player advances to LeaderBoard screen
                if self.second3>=60:
                    #User's info is stored in a .txt file
                    self.ScoreInfo = str(self.name)+":"+ str(self.Score)+"\n"
                    self.ScoreBoard = open("ScoreBoard.txt","a")
                    self.ScoreBoard.write(self.ScoreInfo)
                    self.ScoreBoard.close()
                    self.canvas.destroy()
                    self.Leaderboard()
            self.canvas.after(1000,Timer3)
            self.Second3.config(text=self.second3)
            self.Minute3.config(text=self.minute3)
            
        Timer3()

#Flags for each meteorite movement and valitates it hasn't been destroyed by collision.
        #Meteorite 1
        self.moveR=True
        self.moveL=True
        self.moveU=True
        self.moveD=True
        self.m1Flag=True

        #Meteorite 2
        self.move2R=True
        self.move2L=True
        self.move2U=True
        self.move2D=True
        self.m2Flag=True

        #Meteorite 3
        self.move3R=True
        self.move3L=True
        self.move3U=True
        self.move3D=True
        self.m3Flag=True

        #Meteorite 4
        self.move4R=True
        self.move4L=True
        self.move4U=True
        self.move4D=True
        self.m4Flag=True

        #Meteorite 5
        self.move5R=True
        self.move5L=True
        self.move5U=True
        self.move5D=True
        self.m5Flag=True

    #Function to randomly generate a magnitude for the movement of each meteorite every time they colide with a border.
        def coord_generator():
            #Meteorite 1
            self.xm1 = random.randint(10,30)
            self.ym1 = random.randint(10,30)
            #Meteorite 2
            self.xm2 = random.randint(10,30)
            self.ym2 = random.randint(10,30)
            #Meteorite 3
            self.xm3 = random.randint(10,30)
            self.ym3 = random.randint(10,30)
            #Meteorite 4
            self.xm4 = random.randint(10,30)
            self.ym4 = random.randint(10,30)
            #Meteorite 5
            self.xm5 = random.randint(10,30)
            self.ym5 = random.randint(10,30)
    
    #Functions for the sound of each meteorite's collision with the borders
        #Meteorite 1
        def soundsm1():
            if self.meteorite1_coords[0]+self.xm1>750 or self.meteorite1_coords[0]-self.xm1 < 50 or self.meteorite1_coords[1]+self.ym1 > 750 or self.meteorite1_coords[1]-self.ym1 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 2
        def soundsm2():
            if self.meteorite2_coords[0]+self.xm2>750 or self.meteorite2_coords[0]-self.xm2 < 50 or self.meteorite2_coords[1]+self.ym2 > 750 or self.meteorite2_coords[1]-self.ym2 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 3
        def soundsm3():
            if self.meteorite3_coords[0]+self.xm3>750 or self.meteorite3_coords[0]-self.xm3 < 50 or self.meteorite3_coords[1]+self.ym3 > 750 or self.meteorite3_coords[1]-self.ym3 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 4
        def soundsm4():
            if self.meteorite4_coords[0]+self.xm4>750 or self.meteorite4_coords[0]-self.xm4 < 50 or self.meteorite4_coords[1]+self.ym4 > 750 or self.meteorite4_coords[1]-self.ym4 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()

        #Meteorite 5
        def soundsm5():
            if self.meteorite5_coords[0]+self.xm5>750 or self.meteorite5_coords[0]-self.xm5 < 50 or self.meteorite5_coords[1]+self.ym5 > 750 or self.meteorite5_coords[1]-self.ym5 < 50:
                pygame.mixer.music.load("Recording.mp3")
                pygame.mixer.music.play()
    #Function for the movement of all the meteorites
        def move_meteorite():
            #Meteorite 1(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m1Flag==True:
                self.meteorite1_coords= self.canvas.coords(self.meteorite_1)
                if self.meteorite1_coords[0] < 750 and self.moveR == True:
                    self.canvas.move(self.meteorite_1,self.xm1,0)
                    self.m1b= self.canvas.bbox(self.meteorite_1)
                    soundsm1()
                else:
                    if self.meteorite1_coords[0] > 50 and self.moveL == True:
                        self.canvas.move(self.meteorite_1,-(self.xm1),0)
                        self.m1b= self.canvas.bbox(self.meteorite_1)
                        self.moveR = False
                        soundsm1()
                    else:
                        self.moveR=True
                if self.meteorite1_coords[1] < 750 and self.moveD == True:
                    self.canvas.move(self.meteorite_1,0,self.ym1)
                    self.m1b= self.canvas.bbox(self.meteorite_1)
                    soundsm1()
                else:
                    if self.meteorite1_coords[1] > 50 and self.moveU == True:
                        self.canvas.move(self.meteorite_1,0,-(self.ym1))
                        self.m1b= self.canvas.bbox(self.meteorite_1)
                        self.moveD = False
                        soundsm1()
                    else:
                        self.moveD=True
            #Meteorite 2(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m2Flag==True:   
                self.meteorite2_coords= self.canvas.coords(self.meteorite_2)
                if self.meteorite2_coords[0] < 750 and self.move2R == True:
                    self.canvas.move(self.meteorite_2,self.xm2,0)
                    self.m2b= self.canvas.bbox(self.meteorite_2)
                    soundsm2()
                else:
                    if self.meteorite1_coords[0] > 50 and self.move2L == True:
                        self.canvas.move(self.meteorite_2,-(self.xm2),0)
                        self.m2b= self.canvas.bbox(self.meteorite_2)
                        self.move2R = False
                        soundsm2()
                    else:
                        self.move2R=True
                if self.meteorite2_coords[1] < 750 and self.move2D == True:
                    self.canvas.move(self.meteorite_2,0,self.ym2)
                    self.m2b= self.canvas.bbox(self.meteorite_2)
                    soundsm2()
                else:
                    if self.meteorite2_coords[1] > 50 and self.move2U == True:
                        self.canvas.move(self.meteorite_2,0,-(self.ym2))
                        self.m2b= self.canvas.bbox(self.meteorite_2)
                        self.move2D = False
                        soundsm2()
                    else:
                        self.move2D=True
            #Meteorite 3(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m3Flag==True:
                self.meteorite3_coords= self.canvas.coords(self.meteorite_3)
                if self.meteorite3_coords[0] < 750 and self.move3R == True:
                    self.canvas.move(self.meteorite_3,self.xm3,0)
                    self.m3b= self.canvas.bbox(self.meteorite_3)
                    soundsm3()
                else:
                    if self.meteorite3_coords[0] > 50 and self.move3L == True:
                        self.canvas.move(self.meteorite_3,-(self.xm3),0)
                        self.m3b= self.canvas.bbox(self.meteorite_3)
                        self.move3R = False
                        soundsm3()
                    else:
                        self.move3R=True
                if self.meteorite3_coords[1] < 750 and self.move3D == True:
                    self.canvas.move(self.meteorite_3,0,self.ym3)
                    self.m3b= self.canvas.bbox(self.meteorite_3)
                    soundsm3()
                else:
                    if self.meteorite3_coords[1] > 50 and self.move3U == True:
                        self.canvas.move(self.meteorite_3,0,-(self.ym3))
                        self.m3b= self.canvas.bbox(self.meteorite_3)
                        self.move3D = False
                        soundsm3()
                    else:
                        self.move3D=True
            #Meteorite 4(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m4Flag==True:
                self.meteorite4_coords= self.canvas.coords(self.meteorite_4)
                if self.meteorite4_coords[0] < 750 and self.move4R == True:
                    self.canvas.move(self.meteorite_4,self.xm4,0)
                    self.m4b= self.canvas.bbox(self.meteorite_4)
                    soundsm4()
                else:
                    if self.meteorite4_coords[0] > 50 and self.move4L == True:
                        self.canvas.move(self.meteorite_4,-(self.xm4),0)
                        self.m4b= self.canvas.bbox(self.meteorite_4)
                        self.move4R = False
                        soundsm4()
                    else:
                        self.move4R=True
                if self.meteorite4_coords[1] < 750 and self.move4D == True:
                    self.canvas.move(self.meteorite_4,0,self.ym4)
                    self.m4b= self.canvas.bbox(self.meteorite_4)
                    soundsm4()
                else:
                    if self.meteorite4_coords[1] > 50 and self.move4U == True:
                        self.canvas.move(self.meteorite_4,0,-(self.ym4))
                        self.m4b= self.canvas.bbox(self.meteorite_4)
                        self.move4D = False
                        soundsm4()
                    else:
                        self.move4D=True
            #Meteorite 5(validates that the flag for existance is on and the position in case a sing swap is needed)
            if self.m5Flag==True:
                self.meteorite5_coords= self.canvas.coords(self.meteorite_5)
                if self.meteorite5_coords[0] < 750 and self.move5R == True:
                    self.canvas.move(self.meteorite_5,self.xm5,0)
                    self.m5b= self.canvas.bbox(self.meteorite_5)
                    soundsm5()
                else:
                    if self.meteorite5_coords[0] > 50 and self.move5L == True:
                        self.canvas.move(self.meteorite_5,-(self.xm5),0)
                        self.m5b= self.canvas.bbox(self.meteorite_5)
                        self.move5R = False
                        soundsm5()
                    else:
                        self.move5R=True
                if self.meteorite5_coords[1] < 750 and self.move5D == True:
                    self.canvas.move(self.meteorite_4,0,self.ym5)
                    self.m5b= self.canvas.bbox(self.meteorite_5)
                    soundsm5()
                else:
                    if self.meteorite5_coords[1] > 50 and self.move5U == True:
                        self.canvas.move(self.meteorite_5,0,-(self.ym5))
                        self.m5b= self.canvas.bbox(self.meteorite_5)
                        self.move5D = False
                        soundsm5()
                    else:
                        self.move5D=True
                    
            
            
            self.canvas.after(70,move_meteorite)
        coord_generator()
        move_meteorite()
        
        #Player ship and projectile movement(validates if there is a collision with the meteorites each time the player moves the ship)
        #Move ship +y
        def up3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[1] > 80:
                x=0
                y=-10
                self.canvas.move(self.ship_3,x,y)
            if self.Life_ship3 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb3[2]<self.m1b[2] and self.m1b[1]<self.sb3[1]<self.m1b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb3[2]<self.m2b[2] and self.m2b[1]<self.sb3[1]<self.m2b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb3[2]<self.m3b[2] and self.m3b[1]<self.sb3[1]<self.m3b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb3[2]<self.m4b[2] and self.m4b[1]<self.sb3[1]<self.m4b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
                if self.m5Flag==True:
                    if self.m5b[0]<self.sb3[2]<self.m5b[2] and self.m5b[1]<self.sb3[1]<self.m5b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m5Flag=False
                        self.canvas.delete(self.meteorite_5)
        #Player ship and projectile movement(validates if there is a collision with the meteorites each time the player moves the ship)        
        #Move ship +x
        def right3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_3,x,y)
            if self.Life_ship3 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision

                if self.m1Flag == True:
                    if self.m1b[0]<self.sb3[2]<self.m1b[2] and self.m1b[1]<self.sb3[1]<self.m1b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb3[2]<self.m2b[2] and self.m2b[1]<self.sb3[1]<self.m2b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb3[2]<self.m3b[2] and self.m3b[1]<self.sb3[1]<self.m3b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb3[2]<self.m4b[2] and self.m4b[1]<self.sb3[1]<self.m4b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
                if self.m5Flag==True:
                    if self.m5b[0]<self.sb3[2]<self.m5b[2] and self.m5b[1]<self.sb3[1]<self.m5b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m5Flag=False
                        self.canvas.delete(self.meteorite_5)
        #Player ship and projectile movement(validates if there is a collision with the meteorites each time the player moves the ship)        
        #Move ship -x
        def left3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_3,x,y)
            if self.Life_ship3 <= 0:
                self.canvas.destroy()
                
            else:
                #Validates if the meteorites still exist and if it does, the collision

                if self.m1Flag == True:
                    if self.m1b[0]<self.sb3[2]<self.m1b[2] and self.m1b[1]<self.sb3[1]<self.m1b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb3[2]<self.m2b[2] and self.m2b[1]<self.sb3[1]<self.m2b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb3[2]<self.m3b[2] and self.m3b[1]<self.sb3[1]<self.m3b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb3[2]<self.m4b[2] and self.m4b[1]<self.sb3[1]<self.m4b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
                if self.m5Flag==True:
                    if self.m5b[0]<self.sb3[2]<self.m5b[2] and self.m5b[1]<self.sb3[1]<self.m5b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m5Flag=False
                        self.canvas.delete(self.meteorite_5)
        #Player ship and projectile movement(validates if there is a collision with the meteorites each time the player moves the ship)       
        #Move ship -y
        def down3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[1] < 720:
                x=0
                y=10
                self.canvas.move(self.ship_3,x,y)
            if self.Life_ship3 <= 0:
                self.canvas.destroy()
                
            else:

                #Validates if the meteorites still exist and if it does, the collision
                if self.m1Flag == True:
                    if self.m1b[0]<self.sb3[2]<self.m1b[2] and self.m1b[1]<self.sb3[1]<self.m1b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m1Flag=False
                        self.canvas.delete(self.meteorite_1)
                if self.m2Flag == True:
                    if self.m2b[0]<self.sb3[2]<self.m2b[2] and self.m2b[1]<self.sb3[1]<self.m2b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m2Flag=False
                        self.canvas.delete(self.meteorite_2)
                if self.m3Flag == True:
                    if self.m3b[0]<self.sb3[2]<self.m3b[2] and self.m3b[1]<self.sb3[1]<self.m3b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m3Flag=False
                        self.canvas.delete(self.meteorite_3)
                if self.m4Flag==True:
                    if self.m4b[0]<self.sb3[2]<self.m4b[2] and self.m4b[1]<self.sb3[1]<self.m4b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m4Flag=False
                        self.canvas.delete(self.meteorite_4)
                if self.m5Flag==True:
                    if self.m5b[0]<self.sb3[2]<self.m5b[2] and self.m5b[1]<self.sb3[1]<self.m5b[3]:
                        self.Life_ship3 -= 1
                        self.Life_ship3L.config(text=str(self.Life_ship3))
                        self.m5Flag=False
                        self.canvas.delete(self.meteorite_5)
        #Key bindings
        self.master.bind("<w>", up3)
        self.master.bind("<d>", right3)
        self.master.bind("<a>", left3)
        self.master.bind("<s>", down3)        
    #Function to destroy each canvas and return to the main menu
    def closeall(self):
            self.canvas.destroy()
            self.Menu()
    #Function to create the LeaderBoard's window
    def Leaderboard(self):
        #Creates the window's canvas
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)

        #Creates a label where each player's info will be stored
        self.ScoresLabel= Label(self.canvas, text = ""  , font=("Arial", 22))
        self.ScoresLabel.place(x=300, y=300)

        #Opens the .txt file of the players, reads each line and places the fist seven players
        self.ScoreBoard = open("ScoreBoard.txt","r")
        self.Score_BoardA = self.ScoreBoard.read()
        self.scores=self.Score_BoardA
        self.ScoresList = self.scores.split("\n")
        #Compares if there are enough players to create each line in the label
        if len(self.ScoresList) == 2:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0])
        elif len(self.ScoresList) == 3:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0]
                                +"\n"+"Second:"+self.ScoresList[1])
        elif len(self.ScoresList) == 4:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0]
                                +"\n"+"Second:"+self.ScoresList[1]
                                +"\n"+"Third:"+self.ScoresList[2])
        elif len(self.ScoresList) == 5:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0]
                                +"\n"+"Second:"+self.ScoresList[1]
                                +"\n"+"Third:"+self.ScoresList[2]
                                +"\n"+"Fourth:"+self.ScoresList[3])
        elif len(self.ScoresList) == 6:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0]
                                +"\n"+"Second:"+self.ScoresList[1]
                                +"\n"+"Third:"+self.ScoresList[2]
                                +"\n"+"Fourth:"+self.ScoresList[3]
                                +"\n"+"Fifth:"+self.ScoresList[4])
        elif len(self.ScoreList)== 7:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0]
                                +"\n"+"Second:"+self.ScoresList[1]
                                +"\n"+"Third:"+self.ScoresList[2]
                                +"\n"+"Fourth:"+self.ScoresList[3]
                                +"\n"+"Fifth:"+self.ScoresList[4]
                                +"\n"+"Sixth:"+self.ScoresList[5])
        else:
            self.ScoresLabel.config(text= "Winners"
                                +"\n"+"First:"+self.ScoresList[0]
                                +"\n"+"Second:"+self.ScoresList[1]
                                +"\n"+"Third:"+self.ScoresList[2]
                                +"\n"+"Fourth:"+self.ScoresList[3]
                                +"\n"+"Fifth:"+self.ScoresList[4]
                                +"\n"+"Sixth:"+self.ScoresList[5]
                                +"\n"+"Seventh:"+self.ScoresList[6])
        self.ScoreBoard.close()

        self.Menu_button= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button.place(x=700,y=740)

        

        


            
#Essential game definitions
root= Tk()
pygame.mixer.init()
#BG is the background's photo
BG = PhotoImage(file="backgroundmenu2.png")
Main= Main_window(root)
root.title("Operation Moon Light")
root.iconbitmap("nave.ico")


root.minsize(800, 800)
root.mainloop
