import pygame
BLACK = [0, 0, 0]
WHITE = [0, 0, 0]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]

pygame.init()

TailleEcran = [400, 300]
screen = pygame.display.set_mode(TailleEcran)
pygame.display.set_caption("Super Ball")