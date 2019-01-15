import pygame


WIDTH = 640
HEIGHT = 400
FPS = 60
TITLE = "Platformer"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0 ,255 ,0)
BACKGROUND_COLOR = (64, 177, 247)

pygame.init()
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption(TITLE)

running = True
while running:
    allEvents = pygame.event.get()
    for event in allEvents:
        if event.tupe == pygame.QUIT:
            running = False
            if event.tupe == pygame.KEYDOWN:
               

    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()

pygame quit()
