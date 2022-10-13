# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Create and open a pygame screen with the given size
width = 640
height = 360
screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("Brysons Castle")

### PUT YOUR GAME CODE HERE

# background
screen.fill((0,0,255))
# grass
pygame.draw.rect(screen,(0,130,0),(0,300,640,60),0)
# sun
pygame.draw.circle(screen,(255,255,0),(40,40),40,0)
# house
pygame.draw.rect(screen,(97,97,97),(80,180,440,120),0)
# windows
pygame.draw.rect(screen,(0,0,0),(440,195,60,60),0)
pygame.draw.circle(screen,(0,0,0),(180,240),40,0)
# doors
pygame.draw.rect(screen,(0,0,0),(360,240,40,60),0)
pygame.draw.rect(screen,(0,0,0),(316,240,40,60),0)
# roof
pygame.draw.polygon(screen,(0,0,0),[(304,180),(416,120),(520,180)],0)
pygame.draw.polygon(screen,(0,0,0),[(80,180),(200,120),(300,180)],0)
# flag
pygame.draw.rect(screen,(0,0,0),(300,60,8,120),0)
pygame.draw.rect(screen,(255,255,255),(300,75,60,60),0)
# Uncomment these lines to have a grid show up on your screen
#from pygame_grid import draw_grid
#draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()