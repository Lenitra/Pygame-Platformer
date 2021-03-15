import pygame
from options import *

class Jeu:
    def __init__(self):
        pygame.display.set_caption('PixelArtGame')
        pygame.display.set_caption('PixelArtGame')
        self.screen_x = 768
        self.screen_y = 432
        self.fenetre = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.inter = "menu principal"
        self.img_main_menu = pygame.image.load("assets/main_menu.png")
        self.img_player0 = pygame.transform.scale(pygame.image.load("assets/player/player0.png"), (32*scale, 32*scale))
        self.img_player1 = pygame.transform.scale(pygame.image.load("assets/player/player1.png"), (32, 32))
        self.img_player2 = pygame.transform.scale(pygame.image.load("assets/player/player2.png"), (32, 32))
        self.img_player3 = pygame.transform.scale(pygame.image.load("assets/player/player3.png"), (32, 32))
        self.img_player4 = pygame.transform.scale(pygame.image.load("assets/player/player4.png"), (32, 32))
        self.img_player5 = pygame.transform.scale(pygame.image.load("assets/player/player5.png"), (32, 32))
        self.img_player6 = pygame.transform.scale(pygame.image.load("assets/player/player6.png"), (32, 32))
        self.img_player10 = pygame.transform.scale(pygame.image.load("assets/player/player10.png"), (32, 32))
        self.img_player11 = pygame.transform.scale(pygame.image.load("assets/player/player11.png"), (32, 32))
        self.img_player12 = pygame.transform.scale(pygame.image.load("assets/player/player12.png"), (32, 32))
        self.img_player13 = pygame.transform.scale(pygame.image.load("assets/player/player13.png"), (32, 32))
        self.img_player14 = pygame.transform.scale(pygame.image.load("assets/player/player14.png"), (32, 32))
        self.img_player15 = pygame.transform.scale(pygame.image.load("assets/player/player15.png"), (32, 32))
        self.img_player16 = pygame.transform.scale(pygame.image.load("assets/player/player16.png"), (32, 32))
        self.img_back = pygame.transform.scale(pygame.image.load("assets/back.jpg"), (self.screen_x, self.screen_y))

        self.clic_menu_play = pygame.Rect(0, 0, 100, 50)
        self.img_play_button = pygame.transform.scale(pygame.image.load("assets/play-button.png"), (self.clic_menu_play.size[0],self.clic_menu_play.size[1]))
        self.clic_menu_credits = pygame.Rect(200, 200, 100, 50)
        self.img_credit_button = pygame.transform.scale(pygame.image.load("assets/play-button.png"), (self.clic_menu_play.size[0],self.clic_menu_play.size[1]))

    # méthode bouclée
    def affichage(self, *args):
        if self.inter == "menu principal":
            self.fenetre.blit(self.img_play_button, self.clic_menu_play.topleft)
            self.fenetre.blit(self.img_credit_button, self.clic_menu_credits.topleft)


        if self.inter == ("jeu"):
            self.fenetre.fill((0, 0, 0))

            self.fenetre.blit(args[1].img, (0, 0))
            if args[0].orien == 1:
                self.fenetre.blit(eval(f"self.img_player{str(args[0].sp)}"), (args[0].hitbox[0], args[0].hitbox[1]))
            elif args[0].orien == 0:
                self.fenetre.blit(eval(f"self.img_player{str(args[0].sp+10)}"), (args[0].hitbox[0], args[0].hitbox[1]))


        if self.inter == ("credits"):
            self.fenetre.fill((0, 0, 0))
            img = pygame.image.load("assets/crédits.png")
            self.fenetre.blit(pygame.transform.scale(img, (img.get_size()[0], img.get_size()[1])), (0, 0))
