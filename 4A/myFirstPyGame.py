# My First PyGame, Ryan Kelley, 12/01/21 2:02pm, v0.6

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
PUKEGREEN = (17, 115, 63)

# Setup font. 
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect() 
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill in the background. 
windowSurface.fill(PUKEGREEN)

# Draw a polygon on the screen. 
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291,106), (236,277), (56,277), (0, 106)))

# Draw lines on the screen. 
pygame.draw.line(windowSurface, RED, (60,60), (120,60), 4)
pygame.draw.line(windowSurface, WHITE, (75,60), (60,75), 2)
pygame.draw.line(windowSurface, BLUE, (0,150), (150,0), 1)

# Draw a circle. 
pygame.draw.circle(windowSurface, BLACK, (300, 50), 20, 0)

# Draw an ellipse. 
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw the text rectangle. 
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLUE 
del pixArray

# Draw the text onto the surface. 
windowSurface.blit(text, textRect)

# Update Pygame Display 
pygame.display.update()

# Run game loop. 
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()