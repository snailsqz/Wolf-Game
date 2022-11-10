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
        if Game_Start == False:
            start.draw()
            screen.draw.text('Press M to Start',(500,500),fontsize = 60)
            
        else:
            forest.draw()
            screen.draw.text(f'Score : {Score}',(5,10),fontsize = 30)
            screen.draw.text(f'Lives : {lives}', (930,10),fontsize = 30)
            screen.draw.text(f'Time : {time}',(500,10),fontsize = 30)
            wolf.draw()
            arrow.draw()
            arrow2.draw()
            arrow3.draw()
            potion.draw()
            for sheep in sheepar:
                sheep.draw()

            
########################################
           
def sheepspawn():
    global Speed,maxsheep
    for i in range(maxsheep):
        sheepar.append(Actor('sheep1'))
        
    for sheep in sheepar:
        sheep.x = choice([0,32,64,128,256,768,896,1024])
        sheep.y = choice([0,48,96,192,576,672,720])
        
########################################
        
def GameOver():
    if(Game_Over == True):
        music.fadeout(1)
        clock.unschedule(count_time)

#######################################
        
def count_time():
    global time
    time += 1
    if time % 10 == 0:
        potionspawn()

########################################

def potionspawn():
    
    potion.x = randint(410,900)
    potion.y = randint(240,430)

########################################

def arrowhelper():
    arrow3.x = wolf.x
    arrow3.y = wolf.y
    
########################################
    
def on_mouse_down(pos,button):
    global x1,y1,x2,y2,arrowspeed
    if button == mouse.LEFT :
        (x1,y1) = pos
        arrowspeed = 5
    if button == mouse.RIGHT :
        (x2,y2) = pos
        arrowspeed = 5

########################################
        
def update():
    global Score,Game_Over,Speed,bullet,x1,y1,x2,y2,ar,maxsheep,arrowspeed,lives,potionnum,time,Game_Start,arrow3speed

    if Game_Start == False:
       if keyboard.m:
            Game_Start = True
            clock.schedule_interval(count_time,1.0)
            arrowhelper()
            sheepspawn()

    #Wolf walking
    if keyboard.w: 
        wolf.y -= 2
    if keyboard.s:
        wolf.y += 2
    if keyboard.a:
        wolf.x -= 2
    if keyboard.d:
        wolf.x += 2


    for sheep in sheepar:
        if Game_Over != True:
            #check collision
            if(sheep.colliderect(wolf)):
                sheepar.remove(sheep)
                lives -= 1
                sounds.hurt.play()
                if lives == 0:
                    Game_Over = True
                    GameOver()
                
            try:
                if(arrow.colliderect(sheep) or arrow2.colliderect(sheep) or arrow3.colliderect(sheep)):
                    sheepar.remove(sheep)
                    sounds.bow.play()
                    Score += 1
            except:
                 if len(sheepar) == 1:
                    maxsheep += 1
                    sheepspawn()            
                
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
            animate(arrow3, pos=(sheep.pos),duration = arrow3speed,tween='decelerate')
            wolf.angle = wolf.angle_to(arrow3.pos)
            arrow.angle = arrow.angle_to(wolf) - 180
            arrow2.angle = arrow2.angle_to(wolf) - 180
            arrow3.angle = arrow3.angle_to(sheep.pos)


            #Sheep death
            if len(sheepar) == 0:
                maxsheep += 1
                clock.schedule_unique(sheepspawn, 0.5)
                Speed += 0.1


            #Potion things
            if(lives < 3):
                if(wolf.colliderect(potion)):
                    sounds.potion.play()
                    lives += 1
                    potion.x = -300
                    potion.y = -300

    

    #Press Q and E to Return Arrows
    if keyboard.q:
        x1 = wolf.x
        y1 = wolf.y
        arrowspeed = 10
    if keyboard.e:
        x2 = wolf.x
        y2 = wolf.y
        arrowspeed = 10
    
    #Arrow Standby
    if arrow.x < x1:
        arrow.x += arrowspeed
    if arrow.x > x1:
        arrow.x -= arrowspeed
    if arrow.y < y1:
        arrow.y += arrowspeed
    if arrow.y > y1:
        arrow.y -= arrowspeed

    if arrow2.x < x2:
        arrow2.x += arrowspeed
    if arrow2.x > x2:
        arrow2.x -= arrowspeed
    if arrow2.y < y2:
        arrow2.y += arrowspeed
    if arrow2.y > y2:
        arrow2.y -= arrowspeed

      
    #Press R to Restart Game
    if(keyboard.r and Game_Over == True):
        Game_Over = False
        Score = 0
        time = 0
        lives = 3
        Speed = 1
        clock.schedule_interval(count_time,1.0)
        wolf.pos = (WIDTH/2,HEIGHT/2)
        maxsheep = 1
        potion.x = -800
        potion.y = -800
        arrow.x = WIDTH/2 - 20
        arrow.y = HEIGHT/2
        arrow2.x = WIDTH/2 + 20
        arrow2.y = HEIGHT/2
        music.play('music2')
        sheepar.clear()
        sheepspawn()
        arrowhelper()


    #FullScreen
    if keyboard.f:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.g:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))


##Main Program
TITLE = 'Kill em all wolf'
WIDTH = 1280
HEIGHT = 720
Game_Over = False
Game_Start = False
wolf = Actor('wolf2',(WIDTH/2,HEIGHT/2))
arrow = Actor('red2',(WIDTH/2,HEIGHT/2))
arrow2 = Actor('red2',(WIDTH/2,HEIGHT/2))
arrow3 = Actor('red2',(WIDTH/2,HEIGHT/2))
potion = Actor('potion4',(-300,-300))
start = Actor('test1')
forest = Actor('map')

        
x1 = WIDTH/2 - 20
y1 = HEIGHT/2
x2 = WIDTH/2 + 20
y2 = HEIGHT/2

Score = 0
sheepar = []
potionar = []
maxsheep = 1
arrowspeed = 5
arrow3speed = 1
lives = 3
Speed = 1
time = 0
pgzrun.go()
