import os
import pygame
import random
from globals import *


DECOR = [pygame.image.load(os.path.join(
            "ot", "1614551742_53-p-kartinka-noti-na-belom-fone-64.png")),
         pygame.image.load(os.path.join("ot", "maxresdefault.png")),
         pygame.image.load(os.path.join("ot", "ueh.png"))]


class Decor:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = DECOR[z]
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
