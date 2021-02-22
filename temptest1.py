import pygame    
screen = pygame.display.set_mode((700,700))
keep = True
while keep:
        pygame.time.delay(30)
        pygame.draw.circle(screen, (204, 51, 255), (300, 300), 10)
        pygame.draw.circle(screen, (204, 51, 255), (350, 300), 10)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        keep = False
        pygame.display.update()
