import pygame,sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_cation('Hello world!')
while True:
    for event in pygame.event.get():
        if enent.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()