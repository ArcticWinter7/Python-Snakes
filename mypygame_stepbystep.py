import pygame
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
running = True
posx = 350
posy = 350
while running:
    #go through events and see if close button was click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posx = posx - 10
            elif event.key == pygame.K_RIGHT:
                posx = posx + 10
            elif event.key == pygame.K_UP:
                posy = posy - 10
            elif event.key == pygame.K_DOWN:
                posy = posy + 10
    
    screen.fill((92, 230, 131))
    #draw a purple circle
    circle1 = pygame.draw.circle(screen, (204, 51, 255), (posx, posy), 20)
    
    #draw a red line
    pygame.draw.line(screen, (255, 153, 51), (30, 400), (670, 500), 5)
    #add some text
    writetext('My Awesome Game', 0, 0)
    writetext('The is the second line', 0, 100, (255,0,0))
    writetext('And the third line', 0, 200, (0,0,255), 48)
    #update the game screen with latest

    pygame.display.update()
pygame.quit()