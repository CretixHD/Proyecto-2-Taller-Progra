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
        self.canvas = Canvas(self.master, width=1000, height=800) 
        self.canvas.place(x=0,y=0)
        #Create Background for menu
        self.canvas.create_image(0,0, image = BG, anchor="nw")
        #Welcome message, and user info entries
        self.canvas.create_text(400,80,text= "Welcome to Moon Light", font=("Rocks__G", 42), fill="white")
        self.canvas.create_text(200, 690, text="Enter your nickname:", font= ("Arial", 26),fill="white")
        
        self.player= Entry(self.master)
        self.player.window = self.canvas.create_window(200, 720, window=self.player, width= 300)

        self.Level1_button= Button(self.canvas,bg="slate blue", text="Level_1", font=("Rocks__G", 22), fg="White", command=self.Level_1)
        self.Level1_button.place(x=100, y=450)
        
        self.Level2_button= Button(self.canvas,bg="slate blue", text="Level_2", font=("Rocks__G", 22), fg="White", command=self.Level_2)
        self.Level2_button.place(x=480, y=275)

        self.Level3_button= Button(self.canvas,bg="slate blue", text="Level_3", font=("Rocks__G", 22), fg="White", command=self.Level_3)
        self.Level3_button.place(x= 500, y= 550)
        
        self.Credits_button= Button(self.canvas,bg="slate blue", text="Credits", font=("Rocks__G", 22), fg="White", command=self.Credits)
        self.Credits_button.place(x=600, y=660)
        
        self.Leaderboard_button= Button(self.canvas,bg="slate blue", text="Ranking", font=("Rocks__G", 22), fg="White", command=self.Leaderboard)
        self.Leaderboard_button.place(x=400, y=460)

        self.Score=0
        self.stopFlag=False
        
    def Credits(self):
        self.name = self.player.get()
        #Important information of the developer
        self.canvasC = Canvas(self.master,width=800, height=1000)
        self.canvasC.place(x=0, y=0)

        self.Country= Label(self.canvasC, text="Costa Rica", font=("Arial", 22))
        self.Country.place(x=300, y=25)
        
        self.College= Label(self.canvasC, text="Tecnológico de Costa Rica", font=("Arial", 22))
        self.College.place(x=200, y=75)
        
        self.Carreer= Label(self.canvasC, text="Ingeniería en Computadores", font=("Arial", 22))
        self.Carreer.place(x=200, y=125)
        
        self.Class_info= Label(self.canvasC, text="Taller de Programación, 2021, Grupo 04", font=("Arial", 22))
        self.Class_info.place(x=125, y=175)
        
        self.Professor= Label(self.canvasC, text="Luis Barboza Artavia", font=("Arial", 22))
        self.Professor.place(x=250, y=225)
        
        self.Version= Label(self.canvasC, text="Version:", font=("Arial", 22))
        self.Version.place(x=320, y=325)
        
        self.Author= Label(self.canvasC, text="Christopher Hidalgo Delgado", font=("Arial", 22))
        self.Author.place(x=200, y=375)

        self.Menu_buttonC= Button(self.canvasC,text="Main Menu", command = self.closeall)
        self.Menu_buttonC.place(x=350, y=600)
        
    #Window for level1
    def Level_1(self):
        self.name = self.player.get()    
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship= PhotoImage(file="Nave2.png")
        self.ship_1= self.canvas.create_image(450,720, image= self.ship)
        self.ship_coords = self.canvas.coords(self.ship_1)

        self.bullet=PhotoImage(file="Bullet1.png")

        self.meteorite=PhotoImage(file="Meteorito1.png")
        self.meteorite_1= self.canvas.create_image(450,220, image= self.meteorite)
        self.mb1= self.canvas.bbox(self.meteorite_1)
        #print("p",self.mb1)
        self.meteorite_2= self.canvas.create_image(250,220, image= self.meteorite)
        self.mb2= self.canvas.bbox(self.meteorite_2)
        self.meteorite_3= self.canvas.create_image(450,120, image= self.meteorite)
        self.mb3= self.canvas.bbox(self.meteorite_3)
        self.meteorite_4= self.canvas.create_image(650,220, image= self.meteorite)
        self.mb4= self.canvas.bbox(self.meteorite_4)
        
        self.Life_ship1= 3
        self.Life_ship1I = Label(self.canvas,text="P:",font=("Arial", 20))
        self.Life_ship1I.place(x=650, y=660)
        self.Life_ship = Label(self.canvas,text="50",font=("Arial", 20))
        self.Life_ship.place(x=700, y=660)
        
        self.ScoreL=Label(self.canvas,text="Score: 0",font=("Arial", 20))
        self.ScoreL.place(x=40, y=700)

        self.Player_name =Label(self.canvas, text=self.name, font=("Arial", 20))
        self.Player_name.place (x=700, y=700)

        self.Second = Label(self.canvas,text="",font=("Arial", 20))
        self.Second.place(x=60, y=740)
        
        self.Minute = Label(self.canvas,text="",font=("Arial", 20))
        self.Minute.place(x=15, y=740)

        self.dots = Label(self.canvas,text=":",font=("Arial", 20))
        self.dots.place(x=40, y=740)

        self.Menu_button= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button.place(x=700,y=740)
        
        #self.mainM_button= Button(self.canvas,text="Main Menu",command=self.Level_2(self.Score))
        #self.mainM_button.place(x=500,y=900)
        
        self.minute= 0
        self.second= 0
        #Function for the timer
        def Timer():
            if self.mb1 == False and self.mb2 == False and self.mb3 == False and self.mb4 == False:
                self.Level_2()
            else:
                if self.minute<=60:
                    self.second+=1
                    self.Score+=1
                    self.ScoreL.config(text="Score:"+str(self.Score))
                    if self.second>=60:
                        self.Level_2()
                self.canvas.after(1000,Timer)
                self.Second.config(text=self.second)
                self.Minute.config(text=self.minute)
        Timer()
        
        self.moveR=True
        self.moveL=True
        self.moveU=True
        self.moveD=True
        def coord_generator():
            
            self.xm1 = random.randint(10,30)
            self.ym1 = random.randint(10,30)
            
        def move_meteorite():
            self.meteorite1_coords= self.canvas.coords(self.meteorite_1)
            if self.meteorite1_coords[0] < 750 and self.moveR == True:
                #self.canvas.move(self.meteorite_1,self.xm1,self.ym1)
                self.canvas.move(self.meteorite_1,self.xm1,0)
            else:
                #coord_generator()
                if self.meteorite1_coords[0] > 50 and self.moveL == True:
                    #self.canvas.move(self.meteorite_1,-(self.xm1),self.ym1)
                    self.canvas.move(self.meteorite_1,-(self.xm1),0)
                    self.moveR = False
                else:
                    self.moveR=True
            if self.meteorite1_coords[1]+10 > 750 and self.moveD == True:
                #coord_generator()
                self.canvas.move(self.meteorite_1,0,-(self.ym1))
                
            else:
                #coord_generator()
                if self.meteorite1_coords[1]+10 < 50 and self.moveU == True:
                    self.canvas.move(self.meteorite_1,0,self.ym1)
                    self.moveU = False
                else:
                    self.canvas.move(self.meteorite_1,0,self.ym1)
                    self.moveD=True
                    
            
            
            self.canvas.after(70,move_meteorite)
        coord_generator()
        move_meteorite()
        
        #Player ship and projectile movement
        #Move ship +y
        def up(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[1] > 80:
                x=0
                y=-10
                self.canvas.move(self.ship_1,x,y)
        #Move ship +x
        def right(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_1,x,y)
        #Move ship -x  
        def left(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_1,x,y)
        #Move ship -y   
        def down(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[1] < 720:
                x=0
                y=10
                self.canvas.move(self.ship_1,x,y)  
        #Projectile function(can shoot one projectile at a time)
        def shoot(event):
            self.ship_coords =self.canvas.coords(self.ship_1)
            return projectile(self.ship_coords[0], self.ship_coords[1])
        
        def projectile(x,y):
            self.bullet_1= self.canvas.create_image(x-10,y-100, image=self.bullet)
            return move_projectile()
        
        self.damagem1=0
        self.damagem2=0
        self.damagem3=0
        self.damagem4=0
        
        def move_projectile():
            self.bullet_coords=self.canvas.coords(self.bullet_1)
            self.bc=True
            self.pb= self.canvas.bbox(self.bullet_1)
            if self.mb1!=False:
                if self.mb1[0]<self.pb[2]<self.mb1[2] and self.mb1[1]<self.pb[1]<self.mb1[3]:
                    self.damagem1 += 1
                    if self.damagem1 >= 3:
                        pygame.mixer.music.load("Pop.mp3")
                        pygame.mixer.music.play()
                        self.canvas.delete(self.bullet_1)
                        self.canvas.delete(self.meteorite_1)
                        self.mb1 = False
                        self.bc = False
                        self.Score += 10
            if self.mb2 != False:
                if self.mb2[0]<self.pb[2]<self.mb2[2] and self.mb2[1]<self.pb[1]<self.mb2[3]:
                    self.damagem2 += 1
                    if self.damagem2 >= 3:
                        pygame.mixer.music.load("Pop.mp3")
                        pygame.mixer.music.play()
                        self.canvas.delete(self.bullet_1)
                        self.canvas.delete(self.meteorite_2)
                        self.mb2 = False
                        self.bc = False
                        self.Score += 10
            if self.mb3 != False:
                if self.mb3[0]<self.pb[2]<self.mb3[2] and self.mb3[1]<self.pb[1]<self.mb3[3]:
                    self.damagem3 += 1
                    if self.damagem3 >= 3:
                        pygame.mixer.music.load("Pop.mp3")
                        pygame.mixer.music.play()
                        self.canvas.delete(self.bullet_1)
                        self.canvas.delete(self.meteorite_3)
                        self.mb3 = False
                        self.bc = False
                        self.Score += 10
            if self.mb4 != False:
                if self.mb4[0]<self.pb[2]<self.mb4[2] and self.mb4[1]<self.pb[1]<self.mb4[3]:
                    self.damagem4 += 1
                    if self.damagem4 >= 3:
                        pygame.mixer.music.load("Pop.mp3")
                        pygame.mixer.music.play()
                        self.canvas.delete(self.bullet_1)
                        self.canvas.delete(self.meteorite_4)
                        self.mb4 = False
                        self.bc = False
                        self.Score += 10
            if self.bc == True:   
                if self.bullet_coords[1]>20:
                    x=0
                    y=-150
                    self.canvas.move(self.bullet_1,x,y)
                    self.canvas.after(100,move_projectile)
                else:
                    self.canvas.delete(self.bullet_1)
                    
        #Key bindings
        self.master.bind("<w>", up)
        self.master.bind("<d>", right)
        self.master.bind("<a>", left)
        self.master.bind("<s>", down)        
        self.master.bind("<KeyRelease-space>", shoot)

    #Window for Level2    
    def Level_2(self):
        self.name = self.player.get()
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship2= PhotoImage(file="Nave2.png")
        self.ship_2= self.canvas.create_image(450,720, image= self.ship2)
        self.ship_coords2 = self.canvas.coords(self.ship_2)

        self.bullet2=PhotoImage(file="Bullet1.png")

        self.Life_ship2= 50
        self.Life_ship2I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship2I.place(x=650, y=860)
        self.Life_ship2 = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_ship2.place(x=700, y=860)
        
        self.ScoreL2=Label(self.canvas,text="Score: 0",font=("Arial", 22))
        self.ScoreL2.place(x=40, y=900)

        self.Player_name2 =Label(self.canvas, text=self.name, font=("Arial", 22))
        self.Player_name2.place (x=700, y=940)

        self.Second2 = Label(self.canvas,text="",font=("Arial", 22))
        self.Second2.place(x=60, y=940)
        
        self.Minute2 = Label(self.canvas,text="",font=("Arial", 22))
        self.Minute2.place(x=15, y=940)

        self.dots2 = Label(self.canvas,text=":",font=("Arial", 22))
        self.dots2.place(x=40, y=940)

        self.Menu_button2= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button2.place(x=500,y=900)
        
        self.minute2= 0
        self.second2= 0
        #Function for the timer
        def Timer2():
            if self.minute2<=60:
                self.second2+=1
                self.Score+=3
                self.ScoreL2.config(text="Score:"+str(self.Score))
                if self.second2>=60:
                    self.Level_3()
            self.canvas.after(1000,Timer2)
            self.Second2.config(text=self.second2)
            self.Minute2.config(text=self.minute2)
        Timer2()     
        #Player ship and projectile movement
        #Move ship +y
        def up2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            if self.ship_coords2[1] > 80:
                x=0
                y=-10
                self.canvas.move(self.ship_2,x,y)
        #Move ship +x
        def right2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            if self.ship_coords2[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_2,x,y)
        #Move ship -x  
        def left2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            if self.ship_coords2[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_2,x,y)
        #Move ship -y   
        def down2(event):
            self.ship_coords2 = self.canvas.coords(self.ship_2)
            self.sb2=self.canvas.bbox(self.ship_2)
            if self.ship_coords2[1] < 720:
                x=0
                y=10
                self.canvas.move(self.ship_2,x,y)  
        #Projectile function(can shoot one projectile at a time)
        def shoot2(event):
            self.ship_coords2 =self.canvas.coords(self.ship_2)
            return projectile2(self.ship_coords2[0], self.ship_coords2[1])
        
        def projectile2(x,y):
            self.bullet_2= self.canvas.create_image(x-10,y-100, image=self.bullet2)
            return move_projectile2()
        
        def move_projectile2():
            self.bullet_coords2=self.canvas.coords(self.bullet_2)
            self.pb2= self.canvas.bbox(self.bullet_2)
          
            if self.bullet_coords2[1]>20:
                x=0
                y=-150
                self.canvas.move(self.bullet_2,x,y)
                self.canvas.after(100,move_projectile2)
            else:
                self.canvas.delete(self.bullet_2)
            
        #Key bindings
        self.master.bind("<w>", up2)
        self.master.bind("<d>", right2)
        self.master.bind("<a>", left2)
        self.master.bind("<s>", down2)        
        self.master.bind("<KeyRelease-space>", shoot2)

    #Window for level3
    def Level_3(self):
        
        self.name = self.player.get()   
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship3= PhotoImage(file="Nave2.png")
        self.ship_3= self.canvas.create_image(450,720, image= self.ship3)
        self.ship_coords3 = self.canvas.coords(self.ship_3)  
        
        self.bullet3=PhotoImage(file="Bullet1.png")

        self.Life_ship4= 50
        self.Life_ship3I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship3I.place(x=650, y=860)
        self.Life_ship5 = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_ship5.place(x=700, y=860)

        #self.Score3 = 0
        self.ScoreL3 = Label(self.canvas,text="Score: 0",font=("Arial", 22))
        self.ScoreL3.place(x=40, y=900)

        self.Player_name =Label(self.canvas, text=self.name, font=("Arial", 22))
        self.Player_name.place (x=600, y=940)

        self.Second3 = Label(self.canvas,text="",font=("Arial", 22))
        self.Second3.place(x=60, y=940)
        
        self.Minute3 = Label(self.canvas,text="",font=("Arial", 22))
        self.Minute3.place(x=15, y=940)

        self.dots3 = Label(self.canvas,text=":",font=("Arial", 22))
        self.dots3.place(x=40, y=940)
        
        self.Menu_button= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button.place(x=500,y=900)
        
        self.minute3= 0
        self.second3= 0

        #Fuction for the timer
        def Timer3():
            if self.minute3<=60:
                self.second3+=1
                self.Score+=1
                self.ScoreL3.config(text="Score:"+str(self.Score))
                if self.second3>=60:
                    self.LeaderBoard()
            self.canvas.after(1000,Timer3)
            self.Second3.config(text=self.second3)
            self.Minute3.config(text=self.minute3)
            
        Timer3()
        
        #Player ship and projectile movement
        #Move ship +y
        def up3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[1] > 80:
                x=0
                y=-10
                self.canvas.move(self.ship_3,x,y)
        #Move ship +x
        def right3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_3,x,y)
        #Move ship -x
        def left3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_3,x,y)
        #Move ship -y
        def down3(event):
            self.ship_coords3 = self.canvas.coords(self.ship_3)
            self.sb3=self.canvas.bbox(self.ship_3)
            if self.ship_coords3[1] < 720:
                x=0
                y=10
                self.canvas.move(self.ship_3,x,y)
        #Projectile function(can shoot on projectile at a time)
        def shoot3(event):
            self.ship_coords3 =self.canvas.coords(self.ship_3)
            return projectile3(self.ship_coords3[0], self.ship_coords3[1])

        def projectile3(x,y):
            self.bullet_5= self.canvas.create_image(x-10,y-100, image=self.bullet3)
            return move_projectile3()

        def move_projectile3():
            self.bullet_coords3=self.canvas.coords(self.bullet3)
            self.pb3= self.canvas.bbox(self.bullet3)
            if self.bullet_coords3[1]>20:
                x=0
                y=-150
                self.canvas.move(self.bullet3,x,y)
                self.canvas.after(100,move_projectile3)
            else:
                self.canvas.delete(self.bullet3)

        #Key bindings
        self.master.bind("<w>", up3)
        self.master.bind("<d>", right3)
        self.master.bind("<a>", left3)
        self.master.bind("<s>", down3)        
        self.master.bind("<KeyRelease-space>", shoot3)
        
    def closeall(self):
            self.ScoreInfo = str(self.name)+":"+ str(self.Score)+"\n"
            self.ScoreBoard = open("ScoreBoard.txt","a")
            self.ScoreBoard.write(self.ScoreInfo)
            self.ScoreBoard.close()
            self.stopFlag=True
            #self.canvas.delete(self.Life_ship2I)
            self.canvas.destroy()
            self.canvas.destroy()
            
            self.Menu()
    def Leaderboard(self):
        self.name = self.player.get()
        #Important information of the developer
        self.canvasC = Canvas(self.master,width=800, height=1000)
        self.canvasC.place(x=0, y=0)

        self.Country= Label(self.canvasC, text="Costa Rica", font=("Arial", 22))
        self.Country.place(x=300, y=25)
        
        self.College= Label(self.canvasC, text="Tecnológico de Costa Rica", font=("Arial", 22))
        self.College.place(x=200, y=75)
        
        self.Carreer= Label(self.canvasC, text="Ingeniería en Computadores", font=("Arial", 22))
        self.Carreer.place(x=200, y=125)
        
        self.Class_info= Label(self.canvasC, text="Taller de Programación, 2021, Grupo 04", font=("Arial", 22))
        self.Class_info.place(x=125, y=175)
        
        self.Professor= Label(self.canvasC, text="Luis Barboza Artavia", font=("Arial", 22))
        self.Professor.place(x=250, y=225)
        
        self.Version= Label(self.canvasC, text="Version:", font=("Arial", 22))
        self.Version.place(x=320, y=325)
        
        self.Author= Label(self.canvasC, text="Christopher Hidalgo Delgado", font=("Arial", 22))
        self.Author.place(x=200, y=375)

        self.Menu_buttonC= Button(self.canvasC,text="Main Menu", command = self.closeall)
        self.Menu_buttonC.place(x=350, y=600)

            
#Essential game definitions
root= Tk()
pygame.mixer.init()
BG = PhotoImage(file="backgroundmenu2.png")
Main= Main_window(root)
root.title("Operation Moon Light")
root.iconbitmap("nave.ico")


root.minsize(800, 800)
root.mainloop
