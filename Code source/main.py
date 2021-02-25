import sys
import pygame
import time
from jeu import Jeu
from player import Player
from map import Map


if __name__ == '__main__':
    clock = pygame.time.Clock()
    jeu = Jeu()
    player = Player()
    map = Map()

    while not False:
        # region affichages
        jeu.fenetre.fill((0,0,0))
        if jeu.inter == "menu principal" or jeu.inter == "credits":
            jeu.affichage()
        if jeu.inter == "jeu":
            jeu.affichage(player, map)
            player.grav(map.collides)
            player.move(map.collides)

        clock.tick(120)
        pygame.display.flip()

        # endregion

        for event in pygame.event.get():
            # region events feseables partout
            if event.type == pygame.KEYDOWN and event.key == 27:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            # endregion

            # Event feseable dans n'importe quel niveau
            if jeu.inter == "jeu":
                if event.type == pygame.KEYDOWN:
                    player.plustouch(event.key)
                if event.type == pygame.KEYUP:
                    player.mointouch(event.key)
                # break

            # events juste dans le menu principal
            if jeu.inter == "menu principal":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jeu.clic_menu_play.collidepoint(event.pos):
                        jeu.inter = "jeu"
                        map.lvl = 1
                        map.listet()
                        map.build(jeu)
                        break
                    elif jeu.clic_menu_credits.collidepoint(event.pos):
                        jeu.inter = "credits"
                        break

            if jeu.inter == "credits":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jeu.inter = "menu principal"
                    break