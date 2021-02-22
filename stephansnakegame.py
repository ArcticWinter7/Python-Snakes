import pygame
import random
#initialize pygame
pygame.init()
pygame.font.init()
#set up the screen and screen size
screen = pygame.display.set_mode((700,700))


#write some text
def writetext(text, x, y, color=(0,0,0), fontsize=24):
    # you have to call this at the start, 
    myfont = pygame.font.SysFont('Arial', fontsize, False, False)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface, (x, y))
#initialize the main game loop

def drawsnake(snkx, snky):
    for i in range(len(snkx)):
        pygame.draw.circle(screen, (204, 51, 255), (snkx[i], snky[i]), 10)

def spawnapple(applestatus,randxx,randyy):
    global appleactive
    global randx
    global randy
    if applestatus == False:
        randx = random.randint(10, 690)
        randy = random.randint(10, 690)
        print(randx, randy)
        pygame.draw.circle(screen, (24, 25, 25), (randx, randy), 10)
        print("apple spawned")
        appleactive = True
    else:
        pygame.draw.circle(screen, (24, 25, 25), (randx, randy), 10)
        print("apple spawned")
        appleactive = True


def eatapple(snakexx, snakeyy, applexx, appleyy, appleactivee):
    global appleactive
    diameter = 10
    if appleactivee == True:
        if snakexx - diameter < applexx + diameter and snakexx + diameter > applexx - diameter and snakeyy - diameter < appleyy + diameter and snakeyy + diameter > appleyy - diameter:
            appleactive = False













start = True
while start:
    screen.fill((255,0,0))
    writetext("Press Space to start", 300, 350, (0,0,0), 30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True
                start = False


posx = 350
posy = 350

snakex = [350,340,330]
snakey = [350,350,350]

screenwidth, screenheight = pygame.display.get_surface().get_size()
randx = 200
randy = 200

up = False
down = False
right = True
left = False

appleactive = False
while running:
    pygame.time.delay(30)
    #go through events and see if close button was click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                posx = posx - 10
                up = False
                down = False
                right = False
                left = True
            elif event.key == pygame.K_d:
                posx = posx + 10
                up = False
                down = False
                right = True
                left = False
            elif event.key == pygame.K_w:
                posy = posy - 10
                up = True
                down = False
                right = False
                left = False
            elif event.key == pygame.K_s:
                posy = posy + 10
                up = False
                down = True
                right = False
                left = False
            elif event.key == pygame.K_l:
                appleactive = True
                print("l pressed")
    if up == True:
        if appleeaten == True:
            i=0
            while i < 2:
                snakey.insert(0, snakey[0]-15)
                snakex.insert(0, snakex[0])
                appleeaten = False
                i = i+1
        else:
            snakey.insert(0, snakey[0]-15)
            snakey.pop()
            snakex.insert(0, snakex[0])
            snakex.pop()
    elif down == True:
        if appleeaten == True:
            i=0
            while i < 2:
                snakey.insert(0, snakey[0]+15)
                snakex.insert(0, snakex[0])
                appleeaten = False
                i = i+1
        else:
            snakey.insert(0, snakey[0]+15)
            snakey.pop()
            snakex.insert(0, snakex[0])
            snakex.pop()
    elif left == True:
        if appleeaten == True:
            i=0
            while i < 2:
                snakex.insert(0, snakex[0]-15)
                snakey.insert(0, snakey[0])
                appleeaten = False
                i = i+1
        else:
            snakex.insert(0, snakex[0]-15)
            snakex.pop()
            snakey.insert(0, snakey[0])
            snakey.pop()
    elif right == True:
        if appleeaten == True:
            i=0
            while i < 2:
                snakex.insert(0, snakex[0]+15)
                snakey.insert(0, snakey[0])
                appleeaten = False
                i = i+1
        else:
            snakex.insert(0, snakex[0]+15)
            snakex.pop()
            snakey.insert(0, snakey[0])
            snakey.pop()
    
    # border detection
    screenwidth, screenheight = pygame.display.get_surface().get_size()
    if snakex[0] > screenwidth or snakex[0] < 0:
        running = False
    if snakey[0] > screenheight or snakey[0] < 0:
        running = False

    #apple spawning


    screen.fill((92, 230, 131))
    eatapple(snakex[0],snakey[0],randx,randy, appleactive)
    spawnapple(appleactive,randx,randy)

    #draw a purple circle
    #circle1 = pygame.draw.circle(screen, (204, 51, 255), (posx, posy), 20)
    drawsnake(snakex, snakey)
    #update the game screen with latest
    pygame.display.update()
pygame.quit()