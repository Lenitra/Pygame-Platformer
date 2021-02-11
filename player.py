class Player():
    def __init__(self):
        self.pos = [0, 0]
        self.orientation = 1
        self.pressed = []


    def plustouch(self, key):
        self.pressed.append(key)

    def mointouch(self, key):
        self.pressed.remove(key)

    def move(self):
        if self.pressed != []:
            if self.pressed[0] == 100:
                self.pos[0] += 5
            if self.pressed[0] == 113:
                self.pos[0] -= 5
