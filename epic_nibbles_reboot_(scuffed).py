# importing all libraries
import pygame
import time
import os
import random
from pygame import mixer  # Load the popular external library

# initialising the components
pygame.init()
mixer.init()
pygame.font.init()

# music stuff
mixer.init()
mainmusic = pygame.mixer.Sound("main_music_theme.mp3")
mainmusic.play()

# epilepsy setup
snakewhite = True
snakecolor = (255,255,255)
backgroundcolor = (0,0,0)

# set up screen
screen = pygame.display.set_mode((700,700))

# writes text on screen (for start, score and gameover)
def findsound():
    sound_effect_1 = pygame.mixer.Sound("your_a_gamer.mp3")
    sound_effect_2 = pygame.mixer.Sound("china.mp3")
    sound_effect_3 = pygame.mixer.Sound("wake up.mp3")
    sound_effect_4 = pygame.mixer.Sound("solja_boi.mp3")
    sound_effect_5 = pygame.mixer.Sound("silence_liberal_crab.mp3")
    sound_effect_6 = pygame.mixer.Sound("sanjusansai.mp3")
    sound_effect_7 = pygame.mixer.Sound("poop.mp3")
    sound_effect_8 = pygame.mixer.Sound("_number_six.mp3")
    sound_effect_9 = pygame.mixer.Sound("monke_spin.mp3")
    sound_effect_10 = pygame.mixer.Sound("monke_flip.mp3")
    sound_effect_11 = pygame.mixer.Sound("monke_ad.mp3")
    sound_effect_12 = pygame.mixer.Sound("main_music_theme.mp3")
    sound_effect_13 = pygame.mixer.Sound("ligma.mp3")
    sound_effect_14 = pygame.mixer.Sound("kahoot_snake.mp3")
    sound_effect_15 = pygame.mixer.Sound("grain_cilo.mp3")
    sound_effect_16 = pygame.mixer.Sound("ghost_dance.mp3")
    sound_effect_17 = pygame.mixer.Sound("cursed.mp3")
    sound_effect_18 = pygame.mixer.Sound("_ballin.mp3")
    sound_effect_19 = pygame.mixer.Sound("_bababooey.mp3")
    sound_effect_20 = pygame.mixer.Sound("Amogus.mp3")
    sound_effect_21 = pygame.mixer.Sound("_alert.mp3")
    soundlist = [sound_effect_1,sound_effect_2,sound_effect_3,sound_effect_4,sound_effect_5,sound_effect_6,sound_effect_7,sound_effect_8,sound_effect_9,sound_effect_10,sound_effect_11,sound_effect_12,sound_effect_13,sound_effect_14,sound_effect_15,sound_effect_16,sound_effect_17,sound_effect_18,sound_effect_19,sound_effect_20,sound_effect_21]
    _randsound = random.randint(0,len(soundlist) - 1)
    _soundtoplay = soundlist[_randsound]
    _soundtoplay.play()


def colorswap():
    global snakewhite
    global snakecolor
    global backgroundcolor
    if snakewhite == True:
        snakecolor = (0,0,0)
        backgroundcolor = (255,255,255)
        snakewhite = False
    elif snakewhite == False:
        snakecolor = (255,255,255)
        backgroundcolor = (0,0,0)
        snakewhite = True




def drawinfo(text,x,y,font_size,color=(0,0,0)):
    myfont = pygame.font.SysFont('Ariel', font_size, False, False)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface, (x, y))

# drawing the snake
def drawsnake(snkx,snky):
    for i in range(len(snkx)):
        pygame.draw.circle(screen, (snakecolor), (snkx[i], snky[i]), 10)

# drawing the apple once its been eaten
def drawapple(applex_,appley_,appleonscreen_):
    global appleonscreen
    global applex
    global appley
    if appleonscreen_ == False:
        applex = random.randint(10, 690)
        appley = random.randint(10, 690)
        appleonscreen = True
        pygame.draw.circle(screen, (snakecolor), (applex_, appley_), 10)
    pygame.draw.circle(screen, (snakecolor), (applex_, appley_), 10)
    return(applex, appley, appleonscreen)

# checks if the apple has been eaten
def eatapple(applex, appley, snakex, snakey):
    global appleonscreen
    global score
    global appleeaten
    global speed
    xdiff = applex-snakex[0]
    ydiff = appley-snakey[0]

    if xdiff >= -20 and xdiff <= 20 and ydiff >= -20 and ydiff <= 20:
        # global mainmusic.pause()
        # global sound_effect_.play()
        findsound()
        score = score+1
        appleonscreen = False
        appleeaten = True
        speed = speed - 2 #this accounts for the increase in speed when eating an apple
        return(score , appleonscreen, appleeaten, speed)

# checks if the snake ran outside the borders or into itself
def gameover(snakex, snakey):
    global running
    global endgame
    if snakex[0] <= 0 or snakex[0] >= 700 or snakey[0] <= 0 or snakey[0] >= 700:
        running = False
        endgame = True
    for i in range(len(snakex)):
        if snakex[0] == snakex[i] and snakey[0] == snakey[i] and i != 0:
            endgame = True
            running = False




gamerunning = True
restart = True
while gamerunning:
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
        # Legal disclaimer
        screen.fill((255,0,0))
        drawinfo("DETRIMENTAL EPILEPSY WARNING", 25, 150, 52, (0,0,0))
        drawinfo("The original publisher does not", 220, 185, 20, (0,0,0))
        drawinfo("claim any responsibility for damage", 220, 200, 20, (0,0,0))
        drawinfo("to self, property, or loved ones", 220, 215, 20, (0,0,0))
        drawinfo("as a result of using this program", 220, 230, 20, (0,0,0))
        # instruction
        drawinfo("Press space to start", 120, 380, 60, (0,0,0))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    start = False

    #snake active loop
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
        
        # running all snake/apple checks
        screen.fill((backgroundcolor))
        drawsnake(snakex, snakey)
        eatapple(applex, appley, snakex, snakey)
        drawapple(applex, appley, appleonscreen)
        drawinfo("Score: " + str(score), 0, 0, 24, snakecolor)
        colorswap()
        gameover(snakex, snakey)
        pygame.display.update()

        # def drawinfo(text,x,y,font_size,color=(0,0,0)):

 
    while endgame:
        screen.fill((0,255,0))
        drawinfo("GAME OVER", 250, 350, 60, (0,0,0))
        drawinfo("Your Score was: " + str(score), 250, 400, 20, (0,0,0))
        drawinfo("Press ESC to Exit", 253, 415, 20, (0,0,0))
        drawinfo("Press SPACE to Restart", 253, 435, 20, (0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    endgame = False
                    restart = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()