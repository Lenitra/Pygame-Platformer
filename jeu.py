import pygame

class Jeu:
    def __init__(self):
        pygame.display.set_caption('PixelArtGame')
        self.screen_x = 1280
        self.screen_y = 720
        self.fenetre = pygame.display.set_mode((1280, 720))
        self.inter = "menu principal"
        self.img_main_menu = pygame.image.load("assets/main_menu.png")
        self.img_player = pygame.transform.scale(pygame.image.load("assets/player.png"), (100, 100))

        self.clic_menu_play = pygame.Rect(100, 100, 700, 100)
        self.img_play_button = pygame.transform.scale(pygame.image.load("assets/play-button.png"), (self.clic_menu_play.size))

    # méthode bouclée
    def affichage(self, *args):
        if self.inter == "menu principal":
            self.fenetre.blit(self.img_play_button, self.clic_menu_play.topleft)





        if self.inter == ("jeu1"):
            self.fenetre.fill((0,0,0))
            self.fenetre.blit(self.img_player, (int(self.screen_x*(args[0].pos[0]/self.screen_x)), int(self.screen_y*(args[0].pos[1]/self.screen_y))))