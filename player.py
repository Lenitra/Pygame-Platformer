import pygame
from options import scale

class Player():
    def __init__(self):
        self.gravity = 0.1

        self.hitbox = pygame.Rect(32, 100, 32*scale, 32*scale)
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
                if self.speedx <= self.speed_max:
                    self.speedx += self.vec

            if self.pressed.__contains__(113):
                if self.speedx > -self.speed_max:
                    self.speedx -= self.vec

            if self.pressed.__contains__(32):
                if not self.jump:
                    self.saut()

        if not self.pressed.__contains__(100) and not self.pressed.__contains__(113) :
            if self.speedx > 1:
                self.speedx -= self.vec
            elif self.speedx < 1:
                self.speedx += self.vec
            if -1 <= self.speedx <= 1:
                self.speedx = 0

        if self.mouvx(collides):
            self.hitbox[0] += self.speedx



    def mouvx(self, collides):
        for box in collides:
            if pygame.Rect((self.hitbox[0] + self.speedx)*scale, self.hitbox[1]*scale, 32*scale, 32*scale).colliderect(box):
                self.speedx = 0
                return False
        return True

    def grav(self, collides):
        for box in collides:
            if pygame.Rect(self.hitbox[0]*scale, (self.hitbox[1]+self.speedy)*scale, 32*scale, 32*scale).colliderect(box):
                if self.speedy < 0:
                    self.speedy = 0
                    break
                if self.speedy > 0:
                    while self.hitbox[1] % 16 != 0:
                        self.hitbox[1]+=1
                    self.jump = False

                return

        self.speedy += self.gravity
        self.hitbox[1] += self.speedy

    def saut(self):
        self.jump = True
        self.speedy = -3
