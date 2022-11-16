import pgzrun

def draw():
    screen.fill('white')
    wolf.draw()
    
def update():
    og_x = wolf.x
    og_y = wolf.y
    if keyboard.w: 
        wolf.y -= 5
    if keyboard.s:
        wolf.y += 5
    if keyboard.a:
        wolf.x -= 5
    if keyboard.d:
        wolf.x += 5

    if wolf.x < 0 or wolf.x > WIDTH or wolf.y < 0 or wolf.y > HEIGHT:
        wolf.x = og_x
        wolf.y = og_y


TITLE = 'TEST'
WIDTH = 800
HEIGHT = 600
wolf = Actor('wolf2',(WIDTH/2,HEIGHT/2))
pgzrun.go()
