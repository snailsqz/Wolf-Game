import pgzrun
from random import randint,choice
import pygame
'''
Press WASD to move
Press Left click and Right click to move an arrow
Press Q and E to Return an arrow
Press F to Fullscreen
Press G to Exit Fullscreen
Press R to Retry

'''
def draw():
    if Game_Over:
        screen.fill('black')
        screen.draw.text(f'Your Score : {Score}',(245,300),fontsize = 50)
        screen.draw.text('Press R to Try again',(245,350),fontsize = 50)
    else:
        screen.fill((0,171,102))
        screen.draw.text(f'Score : {Score}',(5,10),fontsize = 30)
        wolf.draw()
        arrow.draw()
        arrow2.draw()
        arrow3.draw()
        for sheep in ar:
            sheep.draw()
            
def sheepspawn():
    global Speed,maxsheep,Game_Over

    for i in range(maxsheep):
        ar.append(Actor('sheep1'))
        
    for sheep in ar:
        sheep.x = choice([0,256,768,1024])
        sheep.y = choice([0,192,576,768])
        Speed = randint(2,5)

def arrowhelper():
    global Speed2
    arrow3.x = randint(-200,1000)
    arrow3.y = randint(-100,800)
    Speed2 = randint(1,4)
    
def on_mouse_down(pos,button):
    global x1,y1,x2,y2
    if button == mouse.LEFT : (x1,y1) = pos
    if button == mouse.RIGHT : (x2,y2) = pos

 
def update():
    global Score,Game_Over,Speed,bullet,Speed2,x1,y1,x2,y2,ar,maxsheep
              
    #Wolf walking
    if keyboard.w: 
        wolf.y -= 2
    if keyboard.s:
        wolf.y += 2
    if keyboard.a:
        wolf.x -= 2
    if keyboard.d:
        wolf.x += 2

    for sheep in ar:
        if Game_Over != True:
            #check collision
            if(sheep.colliderect(wolf)):
                Game_Over = True
            if(arrow.colliderect(sheep) or arrow2.colliderect(sheep) or arrow3.colliderect(sheep)):
                ar.remove(sheep)
                Score += 1
                Speed2 += 0.01

                
            #Sheep Chasing
            if sheep.x < wolf.x:
                sheep.x += Speed
            if sheep.x > wolf.x:
                sheep.x -= Speed
            if sheep.y < wolf.y:
                sheep.y += Speed
            if sheep.y > wolf.y:
                sheep.y -= Speed

            #animation
            if arrow3.x < sheep.x:
                arrow3.x += Speed2
            if arrow3.x > sheep.x:
                arrow3.x -= Speed2
            if arrow3.y < sheep.y:
                arrow3.y += Speed2
            if arrow3.y > sheep.y:
                arrow3.y -= Speed2
            wolf.angle = wolf.angle_to(sheep.pos)
            arrow.angle = arrow.angle_to(wolf) - 180
            arrow2.angle = arrow2.angle_to(wolf) - 180
            arrow3.angle = arrow3.angle_to(sheep.pos)

            #Game Over

            if len(ar) == 0:
                maxsheep += 1
                sheepspawn()
                
        if(Game_Over == True):
            sheep.x = 0
            sheep.y = 0
            arrow.x = 1600
            arrow.y = 1600
            arrow2.x = 1600
            arrow2.y = 1600 
            arrow3.x = 1600
            arrow3.y = 1600
            maxsheep = 1


    #Press Q and E to Return
    if keyboard.q:
        x1 = wolf.x
        y1 = wolf.y
    if keyboard.e:
        x2 = wolf.x
        y2 = wolf.y
    
    #Arrow Standby
    if arrow.x < x1:
        arrow.x += 5
    if arrow.x > x1:
        arrow.x -= 5
    if arrow.y < y1:
        arrow.y += 5
    if arrow.y > y1:
        arrow.y -= 5

    if arrow2.x < x2:
        arrow2.x += 5
    if arrow2.x > x2:
        arrow2.x -= 5
    if arrow2.y < y2:
        arrow2.y += 5
    if arrow2.y > y2:
        arrow2.y -= 5

      
    #Press R to Restart Game
    if(keyboard.r and Game_Over == True):
        Game_Over = False
        Score = 0
        wolf.pos = (WIDTH/2,HEIGHT/2)
        sheep.x = 0
        sheep.y = 0
        arrow.x = WIDTH/2 - 20
        arrow.y = HEIGHT/2
        arrow2.x = WIDTH/2 + 20
        arrow2.y = HEIGHT/2
        ar.clear()
        sheepspawn()
        arrowhelper()


    #FullScreen
    if keyboard.f:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.g:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

    



##Main Program
TITLE = 'Kill em all wolf'
WIDTH = 1024
HEIGHT = 768
Score = 0
Game_Over = False
wolf = Actor('wolf2',(WIDTH/2,HEIGHT/2))
arrow = Actor('red2',(WIDTH/2,HEIGHT/2))
arrow2 = Actor('red2',(WIDTH/2,HEIGHT/2))
arrow3 = Actor('red2',(WIDTH/2,HEIGHT/2))
x1 = WIDTH/2 - 20
y1 = HEIGHT/2
x2 = WIDTH/2 + 20
y2 = HEIGHT/2
ar = []
maxsheep = 1
arrowhelper()
sheepspawn()
pgzrun.go()