import pygame
import sys

fenetre = pygame.display.set_mode((128, 128), pygame.FULLSCREEN)

while not False:
    pygame.display.flip()
    fenetre.fill((0,255,200))
    img_player = pygame.transform.scale(pygame.image.load("assets/player.png"), (128, 128))
    fenetre.blit(img_player, (0,0))
    for event in pygame.event.get():
        # region events feseables partout
        if event.type == pygame.KEYDOWN and event.key == 27:
            sys.exit()
