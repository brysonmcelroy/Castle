# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Create and open a pygame screen with the given size
width = 500
height = 350
screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE



# Flip the changes to the screen to the computer display
pygame.display.flip()