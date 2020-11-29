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


clock = pygame.time.Clock()

balle_y = 50
balle_x = 50

balle_change_x = 3
balle_change_y = 3

balle_rayon = 5
Termine = False


while not Termine:
    event = pygame.event.get(pygame.USEREVENT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termine = True

    balle_x += balle_change_x
    balle_y += balle_change_y


    if balle_y > TailleEcran[1] or balle_y < 0:
        balle_change_y = balle_change_y * -1
    if balle_x > TailleEcran[0] or balle_x < 0:
        balle_change_x = balle_change_x * -1


