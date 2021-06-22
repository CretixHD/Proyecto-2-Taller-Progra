from tkinter import *
import random


#Main class definition
class Main_window:
    def __init__(self, master):
        self.master = master
        
        self.canvas = Canvas(master, width=800, height=1000) 
        self.canvas.pack(fill=BOTH, expand = YES)
        
        #Initial configurations for the menu's canvas
        self.Menu()
        
    def Menu(self):
        self.canvas = Canvas(self.master, width=1000, height=800) 
        self.canvas.place(x=0,y=0)
        #Create Background for menu
        #self.canvas.create_image(0,0, image = BG, anchor="nw")
        #Welcome message, and user info entries
        self.canvas.create_text(400,80,text= "Welcome to Moon Light", font=("Rocks__G", 42), fill="white")
        self.canvas.create_text(200, 690, text="Enter your nickname:", font= ("Arial", 26),fill="white")
        
        self.player= Entry(self.master)
        self.player.window = self.canvas.create_window(200, 720, window=self.player, width= 300)

        self.Level1_button= Button(self.canvas,bg="slate blue", text="Level_1", font=("Rocks__G", 22), fg="White", command=self.Level_1)
        self.Level1_button.place(x=100, y=450)

        self.Level2_button= Button(self.canvas,bg="slate blue", text="Level_2", font=("Rocks__G", 22), fg="White", command=self.Level_2)
        self.Level2_button.place(x=440, y=375)

        self.Level3_button= Button(self.canvas,bg="slate blue", text="Level_3", font=("Rocks__G", 22), fg="White", command=self.Level_3)
        self.Level3_button.place(x= 600, y= 650)
        
        self.Credits_button= Button(self.canvas,bg="slate blue", text="Credits", font=("Rocks__G", 22), fg="White", command=self.Credits)
        self.Credits_button.place(x=350, y=520)

        self.Score=0
        self.stopFlag=False
        
    def Credits(self):
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
    def CreditsR(self):
        self.canvasC.delete("all")
    def Level_1(self):
            
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship= PhotoImage(file="Nave2.png")
        self.ship_1= self.canvas.create_image(450,720, image= self.ship)
        self.ship_coords = self.canvas.coords(self.ship_1)

        self.bullet=PhotoImage(file="Bullet1.png")

        

        self.Life_ship1= 50
        self.Life_ship1I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship1I.place(x=650, y=860)
        self.Life_ship = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_ship.place(x=700, y=860)
        
        self.ScoreL=Label(self.canvas,text="Score: 0",font=("Arial", 22))
        self.ScoreL.place(x=40, y=900)

        self.Player_name =Label(self.canvas, text=self.player.get(), font=("Arial", 22))
        self.Player_name.place (x=700, y=940)

        self.Second = Label(self.canvas,text="",font=("Arial", 22))
        self.Second.place(x=60, y=940)
        
        self.Minute = Label(self.canvas,text="",font=("Arial", 22))
        self.Minute.place(x=15, y=940)

        self.dots = Label(self.canvas,text=":",font=("Arial", 22))
        self.dots.place(x=40, y=940)

        self.Menu_button= Button(self.canvas,text="Main Menu", command = self.closeall)
        self.Menu_button.place(x=500,y=900)
        
        #self.mainM_button= Button(self.canvas,text="Main Menu",command=self.Level_2(self.Score))
        #self.mainM_button.place(x=500,y=900)
        
        self.minute= 0
        self.second= 0
        #Function for the timer
        def Timer():
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

        def Lose(self):

            self.canvas = Canvas(self.master,width=800, height=1000)
            self.canvas.place(x=0, y=0)
            
            self.LoserL= Label(self.canvas, text= "You failed the challenge",font=("Arial", 22))
            self.LoserL.place(x=300,y=500)
        
   
        
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
        
        def move_projectile():
            self.bullet_coords=self.canvas.coords(self.bullet_1)
            self.pb= self.canvas.bbox(self.bullet_1)
          
            if self.bullet_coords[1]>20:
                x=0
                y=-150
                self.canvas.move(self.bullet_1,x,y)
                self.canvas.after(100,move_projectile)
            else:
                self.canvas.delete(self.bullet_1)
                
        def Win():
            if self.Life_ship1 == 50:
                self.Score += 50
                self.Level_2()
                    
            else:
                self.Level_2()
                    
        def Lose():
            self.LoserL= Label(self.canvas, text= "You failed the challenge",font=("Arial", 22))
            self.LoserL.place(x=400,y=500)

     
            
        #Key bindings
        self.master.bind("<w>", up)
        self.master.bind("<d>", right)
        self.master.bind("<a>", left)
        self.master.bind("<s>", down)        
        self.master.bind("<KeyRelease-space>", shoot)

    #Window for Level2    
    def Level_2(self):
            
        self.canvasL2 = Canvas(self.master,width=800, height=1000)
        self.canvasL2.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship2= PhotoImage(file="Nave2.png")
        self.ship_2= self.canvasL2.create_image(450,720, image= self.ship2)
        self.ship_coords2 = self.canvasL2.coords(self.ship_2)

        self.bullet2=PhotoImage(file="Bullet1.png")

        self.Life_ship2= 50
        self.Life_ship2I = Label(self.canvasL2,text="P:",font=("Arial", 22))
        self.Life_ship2I.place(x=650, y=860)
        self.Life_ship2 = Label(self.canvasL2,text="50",font=("Arial", 22))
        self.Life_ship2.place(x=700, y=860)
        
        self.ScoreL2=Label(self.canvasL2,text="Score: 0",font=("Arial", 22))
        self.ScoreL2.place(x=40, y=900)

        self.Player_name2 =Label(self.canvasL2, text=self.player.get(), font=("Arial", 22))
        self.Player_name2.place (x=700, y=940)

        self.Second2 = Label(self.canvasL2,text="",font=("Arial", 22))
        self.Second2.place(x=60, y=940)
        
        self.Minute2 = Label(self.canvasL2,text="",font=("Arial", 22))
        self.Minute2.place(x=15, y=940)

        self.dots2 = Label(self.canvasL2,text=":",font=("Arial", 22))
        self.dots2.place(x=40, y=940)

        self.Menu_button2= Button(self.canvasL2,text="Main Menu", command = self.closeall)
        self.Menu_button2.place(x=500,y=900)
        
        self.minute2= 0
        self.second2= 0
        #Function for the timer
        def Timer2():
            if self.minute2<=60:
                self.second2+=1
                self.Score+=1
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
            self.ship_coords2 = self.canvasL2.coords(self.ship_2)
            self.sb2=self.canvasL2.bbox(self.ship_2)
            if self.ship_coords2[1] > 80:
                x=0
                y=-10
                self.canvasL2.move(self.ship_2,x,y)
        #Move ship +x
        def right2(event):
            self.ship_coords2 = self.canvasL2.coords(self.ship_2)
            self.sb2=self.canvasL2.bbox(self.ship_2)
            if self.ship_coords2[0] < 720:
                x=50
                y=0
                self.canvasL2.move(self.ship_2,x,y)
        #Move ship -x  
        def left2(event):
            self.ship_coords2 = self.canvasL2.coords(self.ship_2)
            self.sb2=self.canvasL2.bbox(self.ship_2)
            if self.ship_coords2[0] > 80:
                x=-50
                y=0
                self.canvasL2.move(self.ship_2,x,y)
        #Move ship -y   
        def down2(event):
            self.ship_coords2 = self.canvasL2.coords(self.ship_2)
            self.sb2=self.canvasL2.bbox(self.ship_2)
            if self.ship_coords2[1] < 720:
                x=0
                y=10
                self.canvasL2.move(self.ship_2,x,y)  
        #Projectile function(can shoot one projectile at a time)
        def shoot2(event):
            self.ship_coords2 =self.canvasL2.coords(self.ship_2)
            return projectile2(self.ship_coords2[0], self.ship_coords2[1])
        
        def projectile2(x,y):
            self.bullet_2= self.canvasL2.create_image(x-10,y-100, image=self.bullet2)
            return move_projectile2()
        
        def move_projectile2():
            self.bullet_coords2=self.canvasL2.coords(self.bullet_2)
            self.pb2= self.canvasL2.bbox(self.bullet_2)
          
            if self.bullet_coords2[1]>20:
                x=0
                y=-150
                self.canvasL2.move(self.bullet_2,x,y)
                self.canvasL2.after(100,move_projectile2)
            else:
                self.canvasL2.delete(self.bullet_2)
            
        #Key bindings
        self.master.bind("<w>", up2)
        self.master.bind("<d>", right2)
        self.master.bind("<a>", left2)
        self.master.bind("<s>", down2)        
        self.master.bind("<KeyRelease-space>", shoot2)

    #Window for level3
    def Level_3(self):
            
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

        self.Player_name =Label(self.canvas, text=self.player.get(), font=("Arial", 22))
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
            self.ScoreInfo = str(self.player.get())+":"+ str(self.Score)+"\n"
            self.ScoreBoard = open("ScoreBoard.txt","a")
            self.ScoreBoard.write(self.ScoreInfo)
            self.ScoreBoard.close()
            self.stopFlag=True
            self.canvas.destroy()
            #self.Menu()
            

            
#Essential game definitions
root= Tk()
#BG = PhotoImage(file="backgroundmenu2.png")
Main= Main_window(root)
root.title("Operation Moon Light")
root.iconbitmap("nave.ico")


root.minsize(800, 1000)
root.mainloop
