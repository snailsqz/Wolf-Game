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
textcolor = (148, 37, 99)
def draw():
    if Game_Over:
        forest.draw()
        screen.draw.text(f'You Survied for {time} seconds',(420,300),color = (34, 44, 60),fontname = "sunshine",fontsize = 50)
        screen.draw.text(f'Your Score : {Score}',(500,350),color = (34, 44, 60),fontname = "sunshine",fontsize = 50)
        screen.draw.text('Press R to Try again',(470,400),color = (34, 44, 60),fontname = "sunshine",fontsize = 50)
    else:
        if Game_Start == False:
            start.draw()
            screen.draw.text('Press M to Start',(500,600),color = 'blue',fontname = "sunshine",fontsize = 60)
            
        else:
            forest.draw()
            for sheep in sheepar:
                sheep.draw()
            for damaged in damage:
                damaged.draw()
            for health in heal:
                health.draw()
            wolf.draw()
            arrow.draw()
            arrow2.draw()
            arrow3.draw()
            potion.draw()
            screen.draw.text(f'Score : {Score}',(20,10),color = textcolor,fontname = "sunshine",fontsize = 50)
            screen.draw.text(f'High Score : {Highscore}',(20,100),color = textcolor,fontname = "sunshine",fontsize = 50)
            screen.draw.text(f'Lives : {lives}', (1100,100),color = textcolor,fontname = "sunshine",fontsize = 50)
            screen.draw.text(f'Time : {time}',(1100,10),color = textcolor,fontname = "sunshine",fontsize = 50)
            screen.draw.text('WASD to Move', (1050,490),color = textcolor,fontname = "sunshine",fontsize = 25)
            screen.draw.text('Q&E to Return Arrows', (1050,530),color = textcolor,fontname = "sunshine",fontsize = 25)
            screen.draw.text('Left Click to move an arrow', (1050,570),color = textcolor,fontname = "sunshine",fontsize = 25)
            screen.draw.text('Right Click to move an arrow', (1050,610),color = textcolor,fontname = "sunshine",fontsize = 25)
            screen.draw.text('F to Full Screen', (1050,650),color = textcolor,fontname = "sunshine",fontsize = 25)
            screen.draw.text('G to Exit Full Screen', (1050,690),color = textcolor,fontname = "sunshine",fontsize = 25)
 
            
########################################
           
def sheepspawn():
    global Speed,maxsheep
    for i in range(maxsheep):
        sheepar.append(Actor('sheep1_2'))
        
    for sheep in sheepar:
        sheep.x = choice([0,32,64,128,256,768,896,900,950,1000,1024])
        sheep.y = choice([0,48,96,192,576,672,690,700,710,720])
        
########################################
        
def GameOver():
    if(Game_Over == True):
        clock.unschedule(count_time)
        music.fadeout(0.2)
        music.set_volume(0.2)
        music.play('gameover')
        

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

def musicdef():
    musicindex = randint(1,9)
    music.set_volume(0.5)
    if musicindex == 1:
        music.play('music2')
    elif musicindex == 2:
        music.play('music3')
    elif musicindex == 3:
        music.play('music4')
    elif musicindex == 4:
        music.play('music5')
    elif musicindex == 5:
        music.play('music6')
    elif musicindex == 6:
        music.play('music7')
    elif musicindex == 7:
        music.play('music8')
    elif musicindex == 8:
        music.play('music9')
    elif musicindex == 9:
        music.play('music10')

########################################
def damaged():
    damage.append(Actor('halfheart2'))
    for damaged in damage:
        damaged.x = wolf.x
        damaged.y = wolf.y - 30
    clock.schedule_unique(cooldown, 0.5)
########################################
def healing():
    heal.append(Actor('heart2'))
    for health in heal:
        health.x = wolf.x
        health.y = wolf.y - 30
    clock.schedule_unique(cooldown, 0.5)
########################################
def cooldown():
    heal.clear()
    damage.clear()
########################################
def update():
    global Score,Game_Over,Speed,bullet,x1,y1,x2,y2,ar,maxsheep
    global arrowspeed,lives,potionnum,time,Game_Start,Highscore
    if Game_Start == False:
       if keyboard.m:
            Game_Start = True
            clock.schedule_interval(count_time,1.0)
            music.fadeout(1)
            musicdef()
            arrowhelper()
            sheepspawn()

    #Wolf walking

    og_x = wolf.x
    og_y = wolf.y
    
    if keyboard.w: 
        wolf.y -= 2
    if keyboard.s:
        wolf.y += 2
    if keyboard.a:
        wolf.x -= 2
    if keyboard.d:
        wolf.x += 2

    if wolf.x < 0 or wolf.x > WIDTH or wolf.y < 0 or wolf.y > HEIGHT:
        wolf.x = og_x
        wolf.y = og_y

    
    for sheep in sheepar:
        if Game_Over != True:
            #check collision
            if(sheep.colliderect(wolf)):
                sheepar.remove(sheep)
                damaged()
                lives -= 1
                sounds.attack2.play()
                if lives == 0:
                    Game_Over = True
                    GameOver()
            sheep.angle = sheep.angle_to(wolf.pos)
                
            try:
                if(arrow.colliderect(sheep) or arrow2.colliderect(sheep) or arrow3.colliderect(sheep)):
                    sheepar.remove(sheep)
                    sounds.attack4.play()
                    Score += 1
            except:
                 if len(sheepar) < 1:
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
            animate(arrow3, pos=(sheep.pos),duration = 1,tween='decelerate')
            wolf.angle = wolf.angle_to(arrow3.pos)
            arrow.angle = arrow.angle_to(wolf) - 180
            arrow2.angle = arrow2.angle_to(wolf) - 180
            arrow3.angle = arrow3.angle_to(sheep.pos)


            #Sheep death
            if len(sheepar) == 0:
                maxsheep += 1
                clock.schedule_unique(sheepspawn, 0.8)
                Speed += 0.1


    
    #Potion things
    if(lives < 3):
        if(wolf.colliderect(potion)):
            sounds.potion.play()
            healing()
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
        if Score > Highscore:
            Highscore = Score
        music.fadeout(1)
        musicdef()
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
        sheepar.clear()
        sheepspawn()
        arrowhelper()


    #FullScreen
    if keyboard.f:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.g:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))


##Main Program
TITLE = 'Hungry!'
WIDTH = 1280
HEIGHT = 720
Game_Over = False
Game_Start = False
wolf = Actor('wolf7',(WIDTH/2,HEIGHT/2))
arrow = Actor('bone3',(WIDTH/2,HEIGHT/2))
arrow2 = Actor('bone4',(WIDTH/2,HEIGHT/2))
arrow3 = Actor('bone5',(WIDTH/2,HEIGHT/2))
potion = Actor('potion4',(-300,-300))
start = Actor('openning')
forest = Actor('map4')
music.play('music1')
        
x1 = WIDTH/2 - 20
y1 = HEIGHT/2
x2 = WIDTH/2 + 20
y2 = HEIGHT/2

music.set_volume(0.5)
Highscore = 0
Score = 0
damage = []
heal = []
sheepar = []
potionar = []
maxsheep = 1
arrowspeed = 5
lives = 3
Speed = 1
time = 0
pgzrun.go()
