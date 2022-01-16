import pygame
import os
from globals import *

BOOM = pygame.image.load(os.path.join("ot", "boom-t-170x148.png"))


class Boom:
    def __init__(self, x, y):
        self.image = BOOM
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = 10  # сколько отображать на экране

    def update(self):
        self.rect.x -= game_speed
        self.time -= 1
        if self.time == 0 or \
           self.rect.x + self.rect.width < 0:
            we.remove(self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
