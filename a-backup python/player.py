import pygame
from options import scale

class Player():
    def __init__(self):
        self.gravity = 0.1
        self.sp = 1
        self.orien = 1
        self.moveloop = 0
        self.hitbox = pygame.Rect(32, 100, 32, 32)
        self.pressed = []
        self.speed_max = 2.5
        self.speedx = 0
        self.speedy = self.gravity
        self.vec = 0.25
        self.jump = False

    def plustouch(self, key):
        self.pressed.append(key)

    def mointouch(self, key):
        self.pressed.remove(key)

    def move(self, collides):

        if self.pressed != []:

            if self.pressed.__contains__(100):
                self.moveloop += 1
                if self.speedx < self.speed_max:
                    self.speedx += self.vec

            if self.pressed.__contains__(113):
                if not self.pressed.__contains__(100):
                    self.moveloop += 1
                if self.speedx > -self.speed_max+1:
                    self.speedx -= self.vec

            if self.pressed.__contains__(32):
                if not self.jump:
                    self.saut()

            # Speed la descente avec un appuis sur "s"
            # if self.pressed.__contains__(115):
            #     self.gravity = 0.25
            # else:
            #     self.gravity = 0.1


        if not self.pressed.__contains__(100) and not self.pressed.__contains__(113) :

            if self.speedx > 1:
                self.speedx -= self.vec
            elif self.speedx < 1:
                self.speedx += self.vec
            if -0.5 <= self.speedx <= 1:
                self.sp = 0
                self.speedx = 0

        if self.mouvx(collides):
            self.hitbox[0] += self.speedx

    # Gestion des variables pour l'annimation
        if self.moveloop >= 15:
            self.moveloop = 0
            self.sp +=1

        if self.speedx > 0:
            self.orien = 1
        elif self.speedx < 0:
            self.orien = 0

        if self.sp >= 7:
            self.sp = 1
    # Check les mouvs latéraux
    def mouvx(self, collides):
        for box in collides:
            if pygame.Rect((self.hitbox[0] + self.speedx), self.hitbox[1], self.hitbox[2], self.hitbox[3]).colliderect(box):
                self.speedx = 0
                return False
        return True

    # Check les collisions et Applique la gravité
    def grav(self, collides):
        for box in collides:
            if pygame.Rect(self.hitbox[0], (self.hitbox[1]+self.speedy), self.hitbox[2], self.hitbox[3]).colliderect(box):
                if self.speedy < 0:
                    self.speedy = 0
                    break
                if self.speedy > 0:
                    while self.hitbox[1] % 16 != 0:
                        self.hitbox[1]+=1
                    self.jump = False

                return
        self.jump = True
        self.speedy += self.gravity
        self.hitbox[1] += self.speedy

    def saut(self):
        self.jump = True
        self.speedy = -3
