# My First PyGame, Ryan Kelley, 11/30/21, 2:45PM, v0.5

import pygame, sys 
from pygame.locals import * 

# Start PyGame 
pygame.init() 

# Setup the game window.  
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup color values. 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PUKEGREEN = (125, 255, 25)

# Setup fonts. 
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery



