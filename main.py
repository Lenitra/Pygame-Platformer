import sys
import pygame
from jeu import Jeu
from player import Player

if __name__ == '__main__':
    clock = pygame.time.Clock()
    jeu = Jeu()
    player = Player()
    while not False:
        # region affichages

        if jeu.inter == "menu principal":
            jeu.affichage()
        if jeu.inter.__contains__("jeu"):
            jeu.affichage(player)

        clock.tick(60)
        player.move()
        pygame.display.flip()

        # endregion

        for event in pygame.event.get():
            # region events feseables partout
            if event.type == pygame.QUIT:
                sys.exit()
            # endregion

            # Event feseable dans n'importe quel niveau
            if jeu.inter == ("jeu1"):
                if event.type == pygame.KEYDOWN:
                    player.plustouch(event.key)
                if event.type == pygame.KEYUP:
                    player.mointouch(event.key)

            # events juste dans le menu principal
            if jeu.inter == "menu principal":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jeu.clic_menu_play.collidepoint(event.pos):
                        jeu.inter = "jeu1"

