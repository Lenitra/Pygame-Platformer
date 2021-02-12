import pygame

class Jeu:
    def __init__(self):
        pygame.display.set_caption('PixelArtGame')
        self.screen_x = 512
        self.screen_y = 288
        self.fenetre = pygame.display.set_mode((self.screen_x, self.screen_y), pygame.FULLSCREEN)
        self.inter = "menu principal"
        self.img_main_menu = pygame.image.load("assets/main_menu.png")
        self.img_player = pygame.transform.scale(pygame.image.load("assets/player.png"), (32, 32))

        self.clic_menu_play = pygame.Rect(100, 100, 700, 100)
        self.img_play_button = pygame.transform.scale(pygame.image.load("assets/play-button.png"), (self.clic_menu_play.size))

    # méthode bouclée
    def affichage(self, *args):
        if self.inter == "menu principal":
            self.fenetre.blit(self.img_play_button, self.clic_menu_play.topleft)





        if self.inter == ("jeu"):
            self.fenetre.fill((0, 0, 0))
            self.fenetre.blit(args[1].img, (0, 0))
            self.fenetre.blit(self.img_player, (args[0].pos[0], args[0].pos[1]))
