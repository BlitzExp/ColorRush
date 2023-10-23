#Libraries
import pygame
import os
from random import randint
from math import sqrt


#Important variables
WIDTH,HEIGHT= 1000,800
WIN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Rush")
FPS=60

WHITE= (255,255,255)
BLACK= (0,0,0)

#Buttons Class
class Collisionablesprites:
    def __init__(self,x,y,dir,name,esx,esy):
        #Position
        self.x = x
        self.y = y
        self.esx=esx
        self.esy=esy
        #Image
        self.path=pygame.image.load(os.path.join(dir,name))
        #Hitboxs
        self.hitbox = (self.x,self.y,self.esx,self.esy)
    def show(self):
        WIN.blit(self.path,(self.x,self.y))
    def drawhitbox(self):
        pygame.draw.rect(WIN,(255,0,0),self.hitbox,1)

class Texto:
    def __init__(self,x,y,dir,name):
        self.x=x
        self.y=y
        self.path=pygame.image.load(os.path.join(dir,name))
    def show(self,x,y):
        self.x=x
        self.y=y
        WIN.blit(self.path,(self.x,self.y))
       


#Class objects which are sprites
Playbutton = Collisionablesprites(467.5,350,'assets',"Play.png",75,50)
Instructions = Collisionablesprites(400,425,'assets',"HOWTOPLAY.png",200,50)
Leaderboard = Collisionablesprites(400,500,'assets',"LEADERBOARD.png",200,50)
Exit = Collisionablesprites(467.5,575,'assets',"Exit.png",75,50)
Game = pygame.image.load(os.path.join('assets',"COLOR_RUSH.png"))
Gametam = pygame.transform.scale(Game,(700,450))
bolaazuldeco = Collisionablesprites(150,675,'assets',"Bola_azul.png",0,0)
bolaverdedeco = Collisionablesprites(300,675,'assets',"Bola_verde.png",0,0)
bolaamarilladeco = Collisionablesprites(450,675,'assets',"Bola_amarrilla.png",0,0)
bolamoradadeco = Collisionablesprites(600,675,'assets',"Bola_morada.png",0,0)
bolamarrondeco = Collisionablesprites(750,675,'assets',"Bola_maron.png",0,0)
back=Collisionablesprites(462.5,720,'assets',"Back.png",75,50)
#Sprites for the random pattern
random=pygame.image.load(os.path.join('Assets',"antesppatron.png"))
randomazul=pygame.image.load(os.path.join('Assets',"patronazul.png"))
randommarron=pygame.image.load(os.path.join('Assets',"patronmarron.png"))
randomamarillo=pygame.image.load(os.path.join('Assets',"patronamarrillo.png"))
randommorado=pygame.image.load(os.path.join('Assets',"patronmorrado.png"))
randomverde=pygame.image.load(os.path.join('Assets',"patronverde.png"))

instrucciones=pygame.image.load(os.path.join('Assets',"instrucciones.png"))

Lose=pygame.image.load(os.path.join('assets','Lose.png'))
youLose = pygame.transform.scale(Lose,(600,500))
points=pygame.image.load(os.path.join('assets','Points.png'))

class bola:
    def __init__(self,x,y,vel,dir,name):
        self.x=x
        self.y=y
        self.vel=vel
        self.path=pygame.image.load(os.path.join(dir,name))
    def show(self,vel):
        WIN.blit(self.path,(self.x,self.y+vel))


def sprites(escena,patron,ticks,rep,orden,velocidad,puntajes,user):
    puntaje2=str(puntajes)
    listaPuntaje=list(puntaje2)
    if escena==1:
        WIN.fill(BLACK)
        Playbutton.show()
        Instructions.show()
        Leaderboard.show()
        Exit.show()
        bolaazuldeco.show()
        bolaverdedeco.show()
        bolaamarilladeco.show()
        bolamoradadeco.show()
        bolamarrondeco.show()
        WIN.blit(Gametam,(150,0))
    elif escena==2: #Pattern scene 
        WIN.fill(BLACK)
        if rep>=1: #Rep number of elements in the pattern
            if ticks<=10:
              WIN.blit(random,(0,0))  
            elif ticks <=90: #Changes the image for the pattern every second
                if patron[len(patron)-rep] == 'azul':
                    WIN.blit(randomazul,(0,0))
                elif patron[len(patron)-rep] == 'morado':
                    WIN.blit(randommorado,(0,0))
                elif patron[len(patron)-rep] == 'verde':
                    WIN.blit(randomverde,(0,0))
                elif patron[len(patron)-rep] == 'marron':
                    WIN.blit(randommarron,(0,0))
                else:
                    WIN.blit(randomamarillo,(0,0))
            if ticks>=90:
                ticks=ticks-90
                rep=rep-1
        elif rep==0:
            ticks=0
            escena=3
    elif escena==3:
        equis=0
        WIN.fill(BLACK)
        WIN.blit(points,(0,30))
       
        for i in listaPuntaje:
            equis+=20
            numero = Texto(0,0,'assets/numeros',i+'.png')
            numero.show(equis,100)
        for i in range(0,5):
            a = orden[i][1]
            b = orden[i][2]
            c = orden[i][3]
            match a:
                case 'amarillo':
                    amarillo=bola(b,c,velocidad,'assets',"Bola_amarrilla.png")
                case 'verde':
                    verde=bola(b,c,velocidad,'assets',"Bola_verde.png")
                case 'azul':
                    azul=bola(b,c,velocidad,'assets',"Bola_azul.png")
                case 'marron':
                    marron=bola(b,c,velocidad,'assets',"Bola_maron.png")
                case 'morado':
                    morado=bola(b,c,velocidad,'assets',"Bola_morada.png")
        amarillo.show(velocidad)
        verde.show(velocidad)
        azul.show(velocidad)
        marron.show(velocidad)
        morado.show(velocidad)
    elif escena==4: #Leaderboard
        WIN.fill(BLACK)
        back.show()
        equis=400
        for i in 'Leaderboard':
            letra = Texto(0,0,'assets/letras',i.upper()+'.png')
            letra.show(equis,100)
            equis+=20
        l=open('Leaderboard.txt','r')
        top=l.readlines()
        #Names
        ye=150
        equis=420
        for element in top:
            separados=element.split()
            ye+=50
            for i in separados[2]:
                letra = Texto(0,0,'assets/letras',i+'.png')
                letra.show(equis,ye)
                equis+=20
            equis=420
        #Scores
        ye=150
        equis=520
        for element in top:
            separados=element.split()
            ye+=50
            for i in separados[0]:
                letra = Texto(0,0,'assets/numeros',i+'.png')
                letra.show(equis,ye)
                equis+=20
            equis=520        
    elif escena==5: #Instructions
        WIN.fill(BLACK)
        WIN.blit(instrucciones,(0,-50))
        back.show()
    elif escena==6: #Lose
        WIN.fill(BLACK)
        WIN.blit(youLose,(200,35))
        WIN.blit(points,(380,420))
        equis=510
        for i in listaPuntaje:
            equis+=20
            numero = Texto(0,0,'assets/numeros',i+'.png')
            numero.show(equis,417)
        equis=400
        for i in 'Your name]':
            if i!=" ":
                letra = Texto(0,0,'assets/letras',i.upper()+'.png')
                letra.show(equis,480)
                equis+=20
            else:
                equis+=20
        equis=460
        for i in user:
            letra = Texto(0,0,'assets/letras',i.upper()+'.png')
            letra.show(equis,550)
            equis+=20
        pygame.draw.rect(WIN,WHITE,(405,540,180,70),3)
    pygame.display.update()
    return (ticks,escena,rep)

def hitbox():
    Playbutton.drawhitbox()
    Instructions.drawhitbox()
    Leaderboard.drawhitbox()
    Exit.drawhitbox()

def pattern(patron):
    colores={1:"azul",2:"verde",3:"amarillo",4:"morado",5:"marron"}
    chi=randint(1,5)
    patron.append(colores[chi])
    return patron

def ordenbolas(patron):
    colores={1:"azul",2:"verde",3:"amarillo",4:"morado",5:"marron"}
    orden=[]
    datos=[]
    y=0
    posx=150
    while len(orden)!=5:
        chi=randint(1,5)
        y=0
        for x in orden:
            if colores[chi]==x:
                y=1
        if y==0:
            orden.append(colores[chi])
    for i in range(0,5):
        j=0
        pat=[]
        for x in patron:
            if x==orden[i]:
                pat.append(j)
            j=j+1
        dato=[i,orden[i],posx,0,pat]
        posx=posx+150
        datos.append(dato)
    return datos

def update_leaderboard(user,puntaje):
    l=open('Leaderboard.txt','r')
    leaders=l.readlines()
    M=[]
    for a in leaders:
        N=a.split(" ")
        b=N[2]
        N[2]=N[2].replace("\n","")
        N[0]=int(N[0])    
        M.append(N)
    if puntaje<M[len(M)-1][0] and len(M)==10:
        return 0
    l.close()
    M.append([puntaje,"by",user])
    for i in range (0,len(M)):
        maximo=M[i][0]
        for j in range (i+1,len(M)):
            if (maximo<M[j][0]):
                maximo=M[j][0]
                posic=j
        if maximo!=M[i][0]:
            n=M[i]
            b=M[posic]
            M[i]=b
            M[posic]=n
    if len(M)>10:
        M.pop()
    l=open("Leaderboard.txt",'w')
    for i in M:
        textos=str(i[0])+" "+i[1]+" "+i[2]
        if i!=M[len(M)-1]:
            textos+='\n'
        l.write(textos)
    l.close()


def main():
    puntajes=0
    escena=1
    patron=[]
    Reloj= pygame.time.Clock() #Pygame's clock
    run = True
    nivel = 1
    start=True
    ticks=0
    rep=0
    orden=[]
    velocidad=0
    ordenamiento=0
    patron_correcto=True
    user=''
    keypress=0
    while run:
        ticks+=1 #Every 60 ticks a second has passed
        Reloj.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        x,y=pygame.mouse.get_pos()
        b1,b2,b3=pygame.mouse.get_pressed()
        if b1==True:
            if escena == 1:
                puntajes=0
                patron=[]
                run = True
                nivel = 1
                start=True
                ticks=0
                rep=0
                orden=[]
                velocidad=0
                ordenamiento=0
                patron_correcto=True
                user=''
                keypress=0
                if x>=Playbutton.x and x<=Playbutton.x + Playbutton.esx and y>Playbutton.y and y<= Playbutton.y + Playbutton.esy:
                    escena=2
                    ticks=0
                    patron=pattern(patron)
                    
                    rep=len(patron)
                elif x>=Exit.x and x<=Exit.x + Exit.esx and y>Exit.y and y<= Exit.y + Exit.esy:
                    run = False
                elif x>=Instructions.x and x<=Instructions.x + Instructions.esx and y>Instructions.y and y<= Instructions.y + Instructions.esy:
                    escena=5
                elif x>=Leaderboard.x and x<=Leaderboard.x + Leaderboard.esx and y>Leaderboard.y and y<= Leaderboard.y + Leaderboard.esy:
                    escena=4
            elif escena==3:
                
                if x>=orden[0][2] and x<=orden[0][2] + 90 and y>(orden[0][3])+velocidad and y<=(orden[0][3])+velocidad + 90 and ticks>20:
                    ticks=0
                    var1=orden[0][4]
                    if len(var1)!=0:
                        for i in var1:
                            if i == ordenamiento:
                                ordenamiento+=1
                                patron_correcto=True
                                puntajes+=200
                                break
                            patron_correcto=False
                           
                    else: 
                        patron_correcto=False
                    if patron_correcto==False:
                        escena=6
                        #pygame.quit()   
                elif x>=orden[1][2] and x<=orden[1][2] +90 and y>(orden[1][3])+velocidad and y<=(orden[1][3])+velocidad + 90 and ticks>20:
                    ticks=0
                    var1=orden[1][4]
                    if len(var1)!=0:
                        for i in var1:
                            if i == ordenamiento:
                                ordenamiento+=1
                                patron_correcto=True
                                puntajes+=200
                                break
                            patron_correcto=False
                           
                    else: 
                        patron_correcto=False
                    if patron_correcto==False:
                        escena=6
                        #pygame.quit()    
                elif x>=orden[2][2] and x<=orden[2][2] +90 and y>(orden[2][3])+velocidad and y<=(orden[2][3])+velocidad + 90 and ticks>20:
                    ticks=0
                    var1=orden[2][4]
                    if len(var1)!=0:
                        for i in var1:
                            if i == ordenamiento:
                                ordenamiento+=1
                                patron_correcto=True
                                puntajes+=200
                                break
                            patron_correcto=False
                    else: 
                        patron_correcto=False
                    if patron_correcto==False:
                        escena=6
                        #pygame.quit()   
                elif x>=orden[3][2] and x<=orden[3][2] +90 and y>(orden[3][3])+velocidad and y<=(orden[3][3])+velocidad + 90 and ticks>20:
                    ticks=0
                    var1=orden[3][4]
                    if len(var1)!=0:
                        for i in var1:
                            if i == ordenamiento:
                                ordenamiento+=1
                                patron_correcto=True
                                puntajes+=200
                                break
                            else:
                                patron_correcto=False
                    else: 
                        patron_correcto=False
                    if patron_correcto==False:
                        escena=6
                        #pygame.quit()   
                elif x>=orden[4][2] and x<=orden[4][2] +90 and y>(orden[4][3])+velocidad and y<=(orden[4][3])+velocidad + 90 and ticks>20:
                    ticks=0
                    var1=orden[4][4]
                    if len(var1)!=0:
                        for i in var1:
                            if i == ordenamiento:
                                ordenamiento+=1
                                patron_correcto=True
                                puntajes+=200
                                break
                            patron_correcto=False
                    else: 
                        patron_correcto=False
                    if patron_correcto==False:
                        escena=6
                        #pygame.quit()  
            elif escena==4:
                if x>=back.x and x<=back.x + back.esx and y>back.y and y<= back.y + back.esy:
                    WIN.fill(BLACK)
                    escena=1

            elif escena==5:
                if x>=back.x and x<=back.x + back.esx and y>back.y and y<= back.y + back.esy:
                    WIN.fill(BLACK)
                    escena=1 
        if escena==3:
            if start==True:
                ordenamiento=0
                velocidad=0
                orden=ordenbolas(patron)
                start=False
                velocidad = .001 * sqrt(nivel)
            velocidad+=1 * sqrt(nivel)
            if ordenamiento==len(patron):
                nivel+=1
                escena=2
                ticks=0
                patron=pattern(patron)
                rep=len(patron)
                start=True
            if orden[4][3]+velocidad >=810 :
                user=''
                escena=6
                patron_correcto=False


        if escena == 6:
            if event.type == pygame.KEYDOWN and ticks>20 and user!="":
                if event.key == pygame.K_BACKSPACE:
                    user=user[:-1]
                    ticks = 0
                if event.key == pygame.K_RETURN:
                    update_leaderboard(user,puntajes)
                    escena = 1
                    ticks=0
            elif ticks>20 and len(user)<3:
                keypress=pygame.key.get_pressed()
                if keypress[pygame.K_a]:
                    user+='A'
                    
                    ticks=0
                elif keypress[pygame.K_b]:
                    user+='B'
                    ticks=0
                elif keypress[pygame.K_c]:
                    user+='C'
                    ticks=0
                elif keypress[pygame.K_d]:
                    user+='D'
                    ticks=0    
                elif keypress[pygame.K_e]:
                    user+='E'
                    ticks=0
                elif keypress[pygame.K_f]:
                    user+='F'
                    ticks=0
                elif keypress[pygame.K_g]:
                    user+='G'
                    ticks=0
                elif keypress[pygame.K_h]:
                    user+='H'
                    ticks=0
                elif keypress[pygame.K_i]:
                    user+='I'
                    ticks=0
                elif keypress[pygame.K_j]:
                    user+='J'
                    ticks=0
                elif keypress[pygame.K_k]:
                    user+='K'
                    ticks=0
                elif keypress[pygame.K_l]:
                    user+='L'
                    ticks=0
                elif keypress[pygame.K_m]:
                    user+='M'
                    ticks=0
                elif keypress[pygame.K_n]:
                    user+='N'
                    ticks=0
                elif keypress[pygame.K_o]:
                    user+='O'
                    ticks=0
                elif keypress[pygame.K_p]:
                    user+='P'
                    ticks=0
                elif keypress[pygame.K_q]:
                    user+='Q'
                    ticks=0
                elif keypress[pygame.K_r]:
                    user+='R'
                    ticks=0
                elif keypress[pygame.K_s]:
                    user+='S'
                    ticks=0
                elif keypress[pygame.K_t]:
                    user+='T'
                    ticks=0
                elif keypress[pygame.K_u]:
                    user+='U'
                    ticks=0
                elif keypress[pygame.K_v]:
                    user+='V'
                    ticks=0
                elif keypress[pygame.K_w]:
                    user+='W'
                    ticks=0
                elif keypress[pygame.K_x]:
                    user+='X'
                    ticks=0
                elif keypress[pygame.K_y]:
                    user+='Y'
                    ticks=0
                elif keypress[pygame.K_z]:
                    user+='Z'
                    ticks=0


        ticks,escena,rep=sprites(escena,patron,ticks,rep,orden,velocidad,puntajes,user)  
        
    pygame.quit()

main()