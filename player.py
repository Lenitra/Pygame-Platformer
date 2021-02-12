class Player():
    def __init__(self):
        self.pos = [32, 240]
        self.orientation = 1
        self.pressed = []
        self.speed = 3


    def plustouch(self, key):
        self.pressed.append(key)

    def mointouch(self, key):
        self.pressed.remove(key)

    def move(self):
        if self.pressed != []:
            if self.pressed[0] == 100:
                if self.pos[0] + 5 < 480:
                    self.pos[0] += self.speed
            if self.pressed[0] == 113:
                if self.pos[0] - 5 > 0:
                    self.pos[0] -= self.speed
