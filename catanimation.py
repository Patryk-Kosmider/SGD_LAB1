import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
cat2Img = pygame.image.load('cat2.png')
catx = 10
caty = 10
cat2x = 380
cat2y = 280
cat_direction = 'right'
cat2_direction = 'left'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if cat_direction == 'right':
        catx += 5
        if catx == 280:
            cat_direction = 'down'
    elif cat_direction == 'down':
        caty += 5
        if caty == 220:
            cat_direction = 'left'
    elif cat_direction == 'left':
        catx -= 5
        if catx == 10:
            cat_direction = 'up'
    elif cat_direction == 'up':
        caty -= 5
        if caty == 10:
            cat_direction = 'right'

    if cat2_direction == 'right':
        cat2x += 5
        if cat2x == 280:
            cat2_direction = 'down'
    elif cat2_direction == 'down':
        cat2y += 5
        if cat2y == 220:
            cat2_direction = 'left'
    elif cat2_direction == 'left':
        cat2x -= 5
        if cat2x == 10:
            cat2_direction = 'up'
    elif cat2_direction == 'up':
        cat2y -= 5
        if cat2y == 10:
            cat2_direction = 'right'


    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(cat2Img, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)