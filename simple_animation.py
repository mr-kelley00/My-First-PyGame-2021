# Simple Animation with PyGame, Ryan Kelley, 12/08/21, 10:18AM, v0.1

import pygame, sys, time 
from pygame.locals import * 

# Setup PyGame
pygame.init()

# Setup the Window 
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400 
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
