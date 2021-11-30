# My First PyGame, Ryan Kelley, 11/30/21, 1:14PM, v0.3

import pygame, sys 
from pygame.locals import * 

# Initialize PyGame 
pygame.init()

# Setup the Window to draw on. 
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('My First PyGame')

# Setup color values. 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PUKEBROWN = (150, 150, 25)
