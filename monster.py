import random
from globals import *

class qwe:

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x + self.rect.width < 0 or \
           self.rect.x > SCREEN_WIDTH:
            we.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Bonus(qwe):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(60, 100)


class Monster(qwe):
    def __init__(self, image):
        a = random.randint(0, 2)
        self.type = a
        super().__init__(image, self.type)
        if a == 0 or a == 1:
            self.rect.y = 315
        else:
            self.rect.y = 280


class Bigmonster(qwe):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        if self.type == 0:
            self.rect.y = 240
        if self.type == 1:
            self.rect.y = 300
        if self.type == 2:
            self.rect.y = 245


class Flymonster(qwe):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 70
        self.index = 0
