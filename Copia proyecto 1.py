from tkinter import *
import random


#Main class definition
class Main_window:
    def __init__(self, master):
        self.master = master
        
        self.canvas = Canvas(master, width=800, height=1000) 
        self.canvas.pack(fill=BOTH, expand = YES)
        
        #Initial configurations for the menu's canvas
        self.Menu(master)
        
    def Menu(self,master):
        self.canvas = Canvas(master, width=1000, height=800) 
        self.canvas.place(x=0,y=0)
        #Create Background for menu
        self.canvas.create_image(0,0, image = BG, anchor="nw")
        #Welcome message, and user info entries
        self.canvas.create_text(400,80,text= "Welcome to Moon Light", font=("Rocks__G", 42), fill="white")
        self.canvas.create_text(200, 690, text="Enter your nickname:", font= ("Arial", 26),fill="white")

        self.player= Entry(master)
        self.player.window = self.canvas.create_window(200, 720, window=self.player, width= 300)

        self.Level1_button= Button(self.canvas,bg="slate blue", text="Level_1", font=("Rocks__G", 22), fg="White", command=self.Level_1)
        self.Level1_button.place(x=100, y=450)

        self.Level2_button= Button(self.canvas,bg="slate blue", text="Level_2", font=("Rocks__G", 22), fg="White", command=self.Level_2)
        self.Level2_button.place(x=440, y=375)

        self.Level3_button= Button(self.canvas,bg="slate blue", text="Level_3", font=("Rocks__G", 22), fg="White", command=self.Level_3)
        self.Level3_button.place(x= 600, y= 650)
        
        self.Credits_button= Button(self.canvas,bg="slate blue", text="Credits", font=("Rocks__G", 22), fg="White", command=self.Credits)
        self.Credits_button.place(x=350, y=520)
        
    def Credits(self):
        #Important information of the developer
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)

        self.Country= Label(self.canvas, text="Costa Rica", font=("Arial", 22))
        self.Country.place(x=300, y=25)
        
        self.College= Label(self.canvas, text="Tecnológico de Costa Rica", font=("Arial", 22))
        self.College.place(x=200, y=75)
        
        self.Carreer= Label(self.canvas, text="Ingeniería en Computadores", font=("Arial", 22))
        self.Carreer.place(x=200, y=125)
        
        self.Class_info= Label(self.canvas, text="Taller de Programación, 2021, Grupo 04", font=("Arial", 22))
        self.Class_info.place(x=125, y=175)
        
        self.Professor= Label(self.canvas, text="Luis Barboza Artavia", font=("Arial", 22))
        self.Professor.place(x=250, y=225)
        
        self.Version= Label(self.canvas, text="Version:", font=("Arial", 22))
        self.Version.place(x=320, y=325)
        
        self.Author= Label(self.canvas, text="Christopher Hidalgo Delgado", font=("Arial", 22))
        self.Author.place(x=200, y=375)

        self.Menu_buttonC= Button(self.canvas,text="Main Menu", command = Menu)
        self.Menu_buttonC.place(x=350, y=600)
    #Window for level1
    def Level_1(self):
            
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship= PhotoImage(file="Nave2.png")
        self.ship_1= self.canvas.create_image(450,720, image= self.ship)
        self.ship_coords = self.canvas.coords(self.ship_1)

        self.enemy = PhotoImage(file="Enemy1.png")
        self.enemy_1 =self.canvas.create_image(470, 100, image = self.enemy)
        self.enemy_coords =self.canvas.coords(self.enemy_1)
        self.bullet=PhotoImage(file="Bullet1.png")
        self.bullet2=PhotoImage(file="Bullet2.png")
       
        self.enemy_coords =self.canvas.coords(self.enemy_1)

        self.Life_ship1= 50
        self.Life_ship1I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship1I.place(x=650, y=860)
        self.Life_ship = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_ship.place(x=700, y=860)

        self.Life_enemy1=30
        self.Life_enemy1I = Label(self.canvas,text="B:",font=("Arial", 22))
        self.Life_enemy1I.place(x=650, y=900)
        self.Life_enemy = Label(self.canvas,text="30",font=("Arial", 22))
        self.Life_enemy.place(x=700, y=900)

        self.Score=0
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
        
        self.mainM_button= Button(self.canvas,text="Main Menu",command=Menu)
        self.mainM_button.place(x=500,y=900)
        
        self.minute= 0
        self.second= 0
        #Function for the timer
        def Timer():
            if self.minute<=60:
                self.second+=1
                if self.second>=60:
                    self.minute += 1
                    self.second = 0
                if self.minute>= 60:
                    self.minute = 0
            self.canvas.after(1000,Timer)
            self.Second.config(text=self.second)
            self.Minute.config(text=self.minute)
        Timer()
        #Enemy movement and attack
        def enemy_moveL():
            self.enemy_coords =self.canvas.coords(self.enemy_1)
            self.eb= self.canvas.bbox(self.enemy_1)
            if self.enemy_coords[0]< 760:
                x=30
                y=0
                self.canvas.move(self.enemy_1, x,y)
                self.canvas.after(70,enemy_moveL)
            else:
                return enemy_moveR()
            
        def enemy_moveR():
            self.enemy_coords = self.canvas.coords(self.enemy_1)
            self.eb= self.canvas.bbox(self.enemy_1)
            if self.enemy_coords[0]>80:
                x=-30
                y=0
                self.canvas.move(self.enemy_1,x,y)
                self.canvas.after(70,enemy_moveR)
            else:
                return enemy_moveL()
            
        enemy_moveL()
        #Enemy attack function
        def shoot_enemy():
            self.enemy_coords =self.canvas.coords(self.enemy_1)
            return projectile2(self.enemy_coords[0], self.enemy_coords[1])
        
        def projectile2(x,y):
            self.bullet_2= self.canvas.create_image(x-10,y-100, image=self.bullet2)
            return move_projectile2()
        
        def move_projectile2():
            self.bullet2_coords=self.canvas.coords(self.bullet_2)
            self.p2b= self.canvas.bbox(self.bullet_2)
            if self.sb[0]<self.p2b[2]<self.sb[2] and self.sb[1]<self.p2b[1]<self.sb[3]:
                if self.Life_ship1 <= 0:
                    return Lose()
                else:
                    self.Life_ship1 -= 2
                    self.Life_ship.config(text=str(self.Life_ship1))
                    print(self.Life_ship1)
            if self.bullet2_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_2,x,y)
                self.canvas.after(10,move_projectile2)
            else:
                self.canvas.delete(self.bullet_2)
                shoot_enemy()
        self.canvas.after(1000,shoot_enemy)

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
            self.canvas.after(1000,collision)
        #Move ship +x
        def right(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[0] < 720:
                x=50
                y=0
                self.canvas.move(self.ship_1,x,y)
            self.canvas.after(1000,collision)
        #Move ship -x  
        def left(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[0] > 80:
                x=-50
                y=0
                self.canvas.move(self.ship_1,x,y)
            self.canvas.after(1000,collision)
        #Move ship -y   
        def down(event):
            self.ship_coords = self.canvas.coords(self.ship_1)
            self.sb=self.canvas.bbox(self.ship_1)
            if self.ship_coords[1] < 720:
                x=0
                y=10
                self.canvas.move(self.ship_1,x,y)
            self.canvas.after(1000,collision)   
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
            if self.eb[0]<self.pb[2]<self.eb[2] and self.eb[1]<self.pb[1]<self.eb[3]:
                if self.Life_enemy1 <= 0:
                    Win()
                else:
                    self.Score += 1
                    self.ScoreL.config(text="Score:"+str(self.Score))
                    self.Life_enemy1 -= 2
                    self.Life_enemy.config(text=str(self.Life_enemy1))
                    print(self.Life_enemy1)
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
                
        def collision():
            if self.eb[0]<self.sb[2]<self.eb[2] and self.eb[1]<self.sb[1]<self.eb[3]:
                if self.Life_ship1<=0:
                    return Lose()
                else:
                    self.Life_ship1 -= 10
                    self.Life_ship.config(text=str(self.Life_ship1))
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
            
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)
        #Important elements for the window, boss, info, and player.
        self.ship2= PhotoImage(file="Nave2.png")
        self.ship_2= self.canvas.create_image(450,720, image= self.ship2)
        self.ship_coords2 = self.canvas.coords(self.ship_2)

        self.enemy2 = PhotoImage(file="Enemy1.png")
        self.enemy_2 =self.canvas.create_image(470, 100, image = self.enemy2)
        
        self.enemy_coords2 =self.canvas.coords(self.enemy_2)
        
        self.bullet4=PhotoImage(file="Bullet1.png")
        
        self.bullet30=PhotoImage(file="Bullet2.png")
        self.bullet60=PhotoImage(file="Bullet2.png")
        self.bullet90=PhotoImage(file="Bullet2.png")
       
        self.enemy_coords2 =self.canvas.coords(self.enemy_2)

        self.Life_ship2= 50
        self.Life_ship2I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship2I.place(x=650, y=860)
        self.Life_ship3 = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_ship3.place(x=700, y=860)

        self.Life_enemy2=40
        self.Life_enemy2I = Label(self.canvas,text="B:",font=("Arial", 22))
        self.Life_enemy2I.place(x=650, y=900)
        self.Life_enemy3 = Label(self.canvas,text="40",font=("Arial", 22))
        self.Life_enemy3.place(x=700, y=900)

        self.Score2 = 0
        self.ScoreL2 = Label(self.canvas,text="Score: 0",font=("Arial", 22))
        self.ScoreL2.place(x=40, y=900)

        self.Player_name =Label(self.canvas, text=self.player.get(), font=("Arial", 22))
        self.Player_name.place (x=600, y=940)

        self.Second2 = Label(self.canvas,text="",font=("Arial", 22))
        self.Second2.place(x=60, y=940)
        
        self.Minute2 = Label(self.canvas,text="",font=("Arial", 22))
        self.Minute2.place(x=15, y=940)

        self.dots2 = Label(self.canvas,text=":",font=("Arial", 22))
        self.dots2.place(x=40, y=940)
        
        self.mainM_button2= Button(self.canvas,text="Main Menu",command=Menu)
        self.mainM_button2.place(x=500,y=900)
        
        self.minute2= 0
        self.second2= 0
        #Function for the timer
        def Timer2():
            if self.minute2<=60:
                self.second2+=1
                if self.second2>=60:
                    self.minute2 += 1
                    self.second2 = 0
                if self.minute2>= 60:
                    self.minute2 = 0
            self.canvas.after(1000,Timer2)
            self.Second2.config(text=self.second2)
            self.Minute2.config(text=self.minute2)
            
        Timer2()
        #Enemy movement
        def enemy_TP():
            self.random_coord2=random.randint(-700, 700)
            if self.enemy_coords2[0]+self.random_coord2< 760 and self.enemy_coords2[0]+self.random_coord2> 80:
                x=self.random_coord2
                y=0
                self.canvas.move(self.enemy_2, x,y)
                self.canvas.after(2000,enemy_TP)
                self.eb21= self.canvas.bbox(self.enemy_2)
            else:
                return enemy_TP()
        
        enemy_TP()
        #Enemy attack
        def shoot_enemy20():
            self.enemy_coords2 =self.canvas.coords(self.enemy_2)
            return projectile30(self.enemy_coords2[0], self.enemy_coords2[1])
        
        def projectile30(x,y):
            self.bullet_30= self.canvas.create_image(x-10,y-100, image=self.bullet30)
            return move_projectile30()

        def move_projectile30():
            self.bullet30_coords=self.canvas.coords(self.bullet_30)
            self.p30b= self.canvas.bbox(self.bullet_30)
            if self.sb2[0]<self.p30b[2]<self.sb2[2] and self.sb2[1]<self.p30b[1]<self.sb2[3]:
                if self.Life_ship2 <= 0:
                    return Lose2()
                else:
                    self.Life_ship2 -= 3
                    self.Life_ship3.config(text=str(self.Life_ship2))
                    print(self.Life_ship2)
            if self.bullet30_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_30,x,y)
                self.canvas.after(10,move_projectile30)
            else:
                self.canvas.delete(self.bullet_30)
                shoot_enemy20()
        self.canvas.after(1000,shoot_enemy20)

        def shoot_enemy30():
            self.enemy_coords2 =self.canvas.coords(self.enemy_2)
            return projectile60(self.enemy_coords2[0], self.enemy_coords2[1])

        def projectile60(x,y):
            self.bullet_60= self.canvas.create_image(x-10,y-100, image=self.bullet60)
            return move_projectile60()

        def move_projectile60():
            self.bullet60_coords=self.canvas.coords(self.bullet_60)
            self.p60b= self.canvas.bbox(self.bullet_60)
            if self.sb2[0]<self.p60b[2]<self.sb2[2] and self.sb2[1]<self.p60b[1]<self.sb2[3]:
                if self.Life_ship2 <= 0:
                    return Lose2()
                else:
                    self.Life_ship2 -= 3
                    self.Life_ship3.config(text=str(self.Life_ship2))
                    print(self.Life_ship2)
            if self.bullet60_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_60,x,y)
                self.canvas.after(10,move_projectile60)
            else:
                self.canvas.delete(self.bullet_60)
                shoot_enemy30()
        self.canvas.after(1200,shoot_enemy30)

        def shoot_enemy40():
            self.enemy_coords2 =self.canvas.coords(self.enemy_2)
            return projectile90(self.enemy_coords2[0], self.enemy_coords2[1])

        def projectile90(x,y):
            self.bullet_90= self.canvas.create_image(x-10,y-100, image=self.bullet90)
            return move_projectile90()

        def move_projectile90():
            self.bullet90_coords=self.canvas.coords(self.bullet_90)
            self.p90b= self.canvas.bbox(self.bullet_90)
            if self.sb2[0]<self.p90b[2]<self.sb2[2] and self.sb2[1]<self.p90b[1]<self.sb2[3]:
                if self.Life_ship2 <= 0:
                    return Lose2()
                else:
                    self.Life_ship2 -= 3
                    self.Life_ship3.config(text=str(self.Life_ship2))
                    print(self.Life_ship2)
            if self.bullet90_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_90,x,y)
                self.canvas.after(10,move_projectile90)
            else:
                self.canvas.delete(self.bullet_90)
                shoot_enemy40()
        self.canvas.after(1450,shoot_enemy40)

        def Lose2():

            self.canvas = Canvas(self.master,width=800, height=1000)
            self.canvas.place(x=0, y=0)
            
            self.LoserL= Label(self.canvas, text= "You failed the challenge",font=("Arial", 22))
            self.LoserL.place(x=400,y=500)

        
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
        #Projectile function(can shoot on projectile at a time)
        def shoot2(event):
            self.ship_coords2 =self.canvas.coords(self.ship_2)
            return projectile2(self.ship_coords2[0], self.ship_coords2[1])

        def projectile2(x,y):
            self.bullet_4= self.canvas.create_image(x-10,y-100, image=self.bullet4)
            return move_projectile2()

        def move_projectile2():
            self.bullet_coords2=self.canvas.coords(self.bullet_4)
            self.pb2= self.canvas.bbox(self.bullet_4)
            if self.eb21[0]<self.pb2[2]<self.eb21[2] and self.eb21[1]<self.pb2[1]<self.eb21[3]:
                if self.Life_enemy2 <= 0:
                    Win2()
                else:
                    self.Score2 += 1
                    self.ScoreL2.config(text="Score:"+str(self.Score2))
                    self.Life_enemy2 -= 2
                    self.Life_enemy3.config(text=str(self.Life_enemy2))
                    print(self.Life_enemy2)
            if self.bullet_coords2[1]>20:
                x=0
                y=-150
                self.canvas.move(self.bullet_4,x,y)
                self.canvas.after(100,move_projectile2)
            else:
                self.canvas.delete(self.bullet_4)
        def Win2():
            if self.Life_ship2 == 50:
                self.Score += 50
                self.Level_3()
            else:
                self.Level_3()
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

        self.enemy3 = PhotoImage(file="Enemy1.png")
        self.enemy_3 =self.canvas.create_image(470, 100, image = self.enemy3)
        
        self.enemy_coords3 =self.canvas.coords(self.enemy_3)
        
        self.bullet5=PhotoImage(file="Bullet1.png")
        
        self.bullet10=PhotoImage(file="Bullet2.png")
        self.bullet20=PhotoImage(file="Bullet2.png")
        self.bullet30=PhotoImage(file="Bullet2.png")
       
        self.enemy_coords3 =self.canvas.coords(self.enemy_3)

        self.Life_ship4= 50
        self.Life_ship3I = Label(self.canvas,text="P:",font=("Arial", 22))
        self.Life_ship3I.place(x=650, y=860)
        self.Life_ship5 = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_ship5.place(x=700, y=860)

        self.Life_enemy4=50
        self.Life_enemy4I = Label(self.canvas,text="B:",font=("Arial", 22))
        self.Life_enemy4I.place(x=650, y=900)
        self.Life_enemy5 = Label(self.canvas,text="50",font=("Arial", 22))
        self.Life_enemy5.place(x=700, y=900)

        self.Score3 = 0
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
        
        self.mainM_button3= Button(self.canvas,text="Main Menu",command=Menu)
        self.mainM_button3.place(x=500,y=900)
        
        self.minute3= 0
        self.second3= 0
        #Fuction for the timer
        def Timer3():
            if self.minute3<=60:
                self.second3+=1
                if self.second3>=60:
                    self.minute3 += 1
                    self.second3 = 0
                if self.minute3>= 60:
                    self.minute3 = 0
            self.canvas.after(1000,Timer3)
            self.Second3.config(text=self.second3)
            self.Minute3.config(text=self.minute3)
            
        Timer3()
        #Enemy movement
        def enemy_moveL3():
            self.enemy_coords3 =self.canvas.coords(self.enemy_3)
            self.eb3= self.canvas.bbox(self.enemy_3)
            if self.enemy_coords3[0]< 760:
                x=30
                y=0
                self.canvas.move(self.enemy_3, x,y)
                self.canvas.after(70,enemy_moveL3)
            else:
                return enemy_moveR3()
            
        def enemy_moveR3():
            self.enemy_coords3 = self.canvas.coords(self.enemy_3)
            self.eb3= self.canvas.bbox(self.enemy_3)
            if self.enemy_coords3[0]>80:
                x=-30
                y=0
                self.canvas.move(self.enemy_3,x,y)
                self.canvas.after(70,enemy_moveR3)
            else:
                return enemy_moveL3()
            
        enemy_moveL3()
        #Strike return
        def enemy_TP3():
            self.random_coord3=random.randint(-700, 700)
            if self.enemy_coords3[0]+self.random_coord3< 760 and self.enemy_coords3[0]+self.random_coord3> 80:
                x=self.random_coord3
                y=0
                self.canvas.move(self.enemy_3, x,y)
                self.canvas.after(2000,enemy_TP3)
                self.eb31= self.canvas.bbox(self.enemy_3)
            else:
                return enemy_TP3()
        
        enemy_TP3()
        #Enemy attack
        def shoot_enemy10():
            self.enemy_coords3 =self.canvas.coords(self.enemy_3)
            return projectile10(self.enemy_coords3[0], self.enemy_coords3[1])
        
        def projectile10(x,y):
            self.bullet_10= self.canvas.create_image(x-10,y-100, image=self.bullet10)
            return move_projectile10()

        def move_projectile10():
            self.bullet10_coords=self.canvas.coords(self.bullet_10)
            self.p10b= self.canvas.bbox(self.bullet_10)
            if self.sb3[0]<self.p10b[2]<self.sb3[2] and self.sb3[1]<self.p10b[1]<self.sb3[3]:
                if self.Life_ship4 <= 0:
                    Lose3()
                else:
                    self.Life_ship4 -= 3
                    self.Life_ship5.config(text=str(self.Life_ship4))
                    print(self.Life_ship4)
            if self.bullet10_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_10,x,y)
                self.canvas.after(10,move_projectile10)
            else:
                self.canvas.delete(self.bullet_10)
                shoot_enemy10()
        self.canvas.after(1000,shoot_enemy10)

        def shoot_enemy20():
            self.enemy_coords3 =self.canvas.coords(self.enemy_3)
            return projectile20(self.enemy_coords3[0], self.enemy_coords3[1])
        
        def projectile20(x,y):
            self.bullet_20= self.canvas.create_image(x-10,y-100, image=self.bullet20)
            return move_projectile20()

        def move_projectile20():
            self.bullet20_coords=self.canvas.coords(self.bullet_20)
            self.p20b= self.canvas.bbox(self.bullet_20)
            if self.sb3[0]<self.p20b[2]<self.sb3[2] and self.sb3[1]<self.p20b[1]<self.sb3[3]:
                if self.Life_ship4 <= 0:
                    Lose3()
                else:
                    self.Life_ship4 -= 3
                    self.Life_ship5.config(text=str(self.Life_ship4))
                    print(self.Life_ship4)
            if self.bullet20_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_20,x,y)
                self.canvas.after(10,move_projectile20)
            else:
                self.canvas.delete(self.bullet_20)
                shoot_enemy20()
        self.canvas.after(1200,shoot_enemy20)

        def shoot_enemy30():
            self.enemy_coords3 =self.canvas.coords(self.enemy_3)
            return projectile30(self.enemy_coords3[0], self.enemy_coords3[1])
        
        def projectile30(x,y):
            self.bullet_30= self.canvas.create_image(x-10,y-100, image=self.bullet30)
            return move_projectile30()

        def move_projectile30():
            self.bullet30_coords=self.canvas.coords(self.bullet_30)
            self.p30b= self.canvas.bbox(self.bullet_30)
            if self.sb3[0]<self.p30b[2]<self.sb3[2] and self.sb3[1]<self.p30b[1]<self.sb3[3]:
                if self.Life_ship4 <= 0:
                    Lose3()
                else:
                    self.Life_ship4 -= 3
                    self.Life_ship5.config(text=str(self.Life_ship4))
                    print(self.Life_ship4)
            if self.bullet30_coords[1]<780:
                x=0
                y=30
                self.canvas.move(self.bullet_30,x,y)
                self.canvas.after(10,move_projectile30)
            else:
                self.canvas.delete(self.bullet_30)
                shoot_enemy30()
        self.canvas.after(1450,shoot_enemy30)

        def Lose3():

            self.canvas = Canvas(self.master,width=800, height=1000)
            self.canvas.place(x=0, y=0)
            
            self.LoserL= Label(self.canvas, text= self.Player_name.get+"You failed the challenge",font=("Arial", 22))
            self.LoserL.place(x=400,y=500)

        
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
            return projectile5(self.ship_coords3[0], self.ship_coords3[1])

        def projectile5(x,y):
            self.bullet_5= self.canvas.create_image(x-10,y-100, image=self.bullet5)
            return move_projectile5()

        def move_projectile5():
            self.bullet_coords5=self.canvas.coords(self.bullet_5)
            self.pb5= self.canvas.bbox(self.bullet_5)
            if self.eb31[0]<self.pb5[2]<self.eb31[2] and self.eb31[1]<self.pb5[1]<self.eb31[3]:
                if self.Life_enemy4 <= 0:
                    Win3()
                else:
                    self.Score3 += 1
                    self.ScoreL3.config(text="Score:"+str(self.Score3))
                    self.Life_enemy4 -= 2
                    self.Life_enemy5.config(text=str(self.Life_enemy4))
                    print(self.Life_enemy4)
            if self.bullet_coords5[1]>20:
                x=0
                y=-150
                self.canvas.move(self.bullet_5,x,y)
                self.canvas.after(100,move_projectile5)
            else:
                self.canvas.delete(self.bullet_5)
        def Win():
            if self.Life_ship4 == 50:
                self.Score += 50
                self.Winner(self.Score)
            else:
                self.Winner(self.Score)
        #Key bindings
        self.master.bind("<w>", up3)
        self.master.bind("<d>", right3)
        self.master.bind("<a>", left3)
        self.master.bind("<s>", down3)        
        self.master.bind("<KeyRelease-space>", shoot3)

    def Winner(self, Score):

        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)

        self.WinnerL= Label(self.canvas, text= self.Player_name.get+"You passed the challenge",font=("Arial", 22))
        self.WinnerL.place(x=400,y=500)

        self.ScoreL= Label(self.canvas, text= self.Score,font=("Arial", 22))
        self.ScoreL.place(x=400,y=700)
    def Loser_screen3(self):
        
        self.canvas = Canvas(self.master,width=800, height=1000)
        self.canvas.place(x=0, y=0)

        self.LoserL= Label(self.canvas, text= self.Player_name.get+"You failed the challenge",font=("Arial", 22))
        self.LoserL.place(x=400,y=500)

            
#Essential game definitions
root= Tk()
BG = PhotoImage(file="E:/Chris/TEC/Intro y Taller/Space Invaders/backgroundmenu2.png")
Main= Main_window(root)
root.title("Operation Moon Light")
root.iconbitmap("E:/Chris/TEC/Intro y Taller/Space Invaders/nave.ico")


root.minsize(800, 1000)
root.mainloop
