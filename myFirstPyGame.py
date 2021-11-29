# My First PyGame, Ryan Kelley, 11/29/21 2:28pm, v0.3

import pygame, sys
from pygame.locals import * 

# Start PyGame
pygame.init()

# Setup our window. l
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

