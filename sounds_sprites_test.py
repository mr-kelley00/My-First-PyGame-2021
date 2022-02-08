# PyGame Sounds and Sprites Practice, Ryan Kelley, February 08, 2022, 2:14PM, v0.0

import pygame, sys, random
from pygame.locals import * 

# Setup PyGame 
pygame.init() 
mainClock = pygame.time.Clock() 

# Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400 
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds 2022') # Changed 


# Setup colors. 
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
WHITE = (255, 255, 255) # Only need white since we will use image files now. 

# Setup the food data structures. 
foodCounter = 0 
NEWFOOD = 40
FOODSIZE = 20

# Setup the player data structures.  NEW 
player = pygame.Rect(300, 100, 40, 40) # Changed from (300, 100, 50, 50)
playerImage = pygame.image.load('img/player.png') # NEW 
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40)) # NEW

foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Movement Variables 
moveLeft = False
moveRight = False
moveUp = False
moveDown = False 

MOVESPEED = 6

# Set up the music. All new. 
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# Run the game loop. 
while True: 
    # Check for events. 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN: 
            # Change the keyboard variables. 
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True 
            if event.key == K_RIGHT or event.key == K_d: 
                moveLeft = False
                moveRight = True 
            if event.key == K_UP or event.key == K_w: 
                moveDown = False
                moveUp = True 
            if event.key == K_DOWN or event.key == K_s: 
                moveUp = False
                moveDown = True
        if event.type == KEYUP: 
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Check to see if the player has stopped moving. 
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d: 
                moveRight = False
            if event.key == K_UP or event.key == K_w: 
                moveUp = False
            if event.key == K_DOWN or event.key == K_s: 
                moveDown = False
            if event.key == K_x: # Use x to teleport the player.  
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            # Turn off the music. 
            if event.key == K_m: 
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)

        if event.type == MOUSEBUTTONUP: 
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))         

    foodCounter += 1
    if foodCounter >= NEWFOOD: 
        # Add new food. 
        foodCounter = 0 
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE)) 

    # Draw white background on Window Surface. 
    windowSurface.fill(WHITE)

    # Move the player. 
    if moveDown and player.bottom < WINDOWHEIGHT: 
        player.top += MOVESPEED
    if moveUp and player.top > 0: 
        player.top -= MOVESPEED
    if moveLeft and player.left > 0: 
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    
    # Draw the player on the surface. 
    pygame.draw.rect(windowSurface, BLACK, player)

    # Check for player colliding with food(s). 
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # Draw the food. 
    for i in range(len(foods)): 
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw the window to the screen. 
    pygame.display.update() 
    mainClock.tick(40)    




    







        


       


        



