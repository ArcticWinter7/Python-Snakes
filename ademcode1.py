import pygame
import random
import os
#initialize pygame
pygame.init()
pygame.font.init()
#set up the screen and screen size
screen = pygame.display.set_mode((700,700))
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'python.png')

# pythonimg = pygame.image.load(my_file)

# posx = 350
# posy = 350

# endgame = False
# restart = False

# score = 0

# snakexstart = [350,335,220]
# snakeystart = [350,350,350]

# snakex = snakeystart
# snakey = snakeystart

# applex = random.randint(10, 690)
# appley = random.randint(10, 690)

# appleonscreen = False
# appleeaten = False

# up = False
# down = False
# right = True
# left = False
# game = True

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

def drawapple(x, y, appleonscreencheck):
    global appleonscreen
    global applex
    global appley
    if appleonscreencheck == False:
        applex = random.randint(10, 690)
        appley = random.randint(10, 690)
        appleonscreen = True
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)
    return(applex, appley, appleonscreen)



def eatapple(applex, appley, snakex, snakey, appleonscreencheck, scoreadd, AE, Sped):
    global appleonscreen
    global score
    global appleeaten
    global speed
    xdiff = applex-snakex[0]
    ydiff = appley-snakey[0]
    if xdiff >= -20 and xdiff <= 20:
        print("Matched 1")
        if ydiff >= -20 and ydiff <= 20:
            print("Matched 2")
            score = score+1
            appleonscreen = False
            appleeaten = True
            speed = speed - 1
            return(score , appleonscreen, appleeaten, speed)


def gameovercheck(snakex, snakey, GO):
    global running
    global endgame
    if snakex[0] <= 0 or snakex[0] >= 700 or snakey[0] <= 0 or snakey[0] >= 700:
        running = False
        endgame = True
    for i in range(len(snakex)):
        if snakex[0] == snakex[i] and snakey[0] == snakey[i] and i != 0:
            endgame = True
            running = False 





game = True
restart = True
while game:
    while restart:

        speed = 100
        posx = 350
        posy = 350

        endgame = False

        score = 0

        snakex = [350,345]
        snakey = [350,350]


        applex = -100
        appley = -100

        appleonscreen = False
        appleeaten = False

        up = False
        down = False
        right = True
        left = False

        restart = False
        start = True
    while start:
        screen.fill((255,0,0))
        # screen.blit(pythonimg, (250, 100))
        writetext("Nibbles Game", 250, 350, (0,0,0), 30)
        writetext("Press Space to start", 250, 380, (0,0,0), 30)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    start = False



    while running:
    
        pygame.time.delay(speed)
        # print(speed)
        #go through events and see if close button was click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and right == False:
                    posx = posx - 10
                    up = False
                    down = False
                    right = False
                    left = True
                elif event.key == pygame.K_d and left == False:
                    posx = posx + 10
                    up = False
                    down = False
                    right = True
                    left = False
                elif event.key == pygame.K_w and down == False:
                    posy = posy - 10
                    up = True
                    down = False
                    right = False
                    left = False
                elif event.key == pygame.K_s and up == False:
                    posy = posy + 10
                    up = False
                    down = True
                    right = False
                    left = False
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
    
        screen.fill((92, 230, 131))



        drawsnake(snakex, snakey)


        eatapple(applex, appley, snakex, snakey, appleonscreen, score, appleeaten, speed)


        drawapple(applex, appley, appleonscreen)


        writetext("Score: " + str(score), 0, 0)




        gameovercheck(snakex, snakey, endgame)
    

    
        pygame.display.update()



    while endgame:
        screen.fill((0,255,0))
        writetext("GAME OVER", 250, 350, (0,0,0), 30)
        writetext("Your Score was: " + str(score), 250, 380, (0,0,0), 30)
        writetext("Press ESC to Exit", 253, 415, (0,0,0), 18)
        writetext("Press SPACE to Restart", 253, 435, (0,0,0), 18)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    endgame = False
                    restart = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()