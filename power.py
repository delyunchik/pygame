import pygame
import os
from globals import *

POWER = [pygame.image.load(os.path.join("Powerballs", "musaball.png")),
         pygame.image.load(os.path.join("Powerballs", "stellaball.png")),
         pygame.image.load(os.path.join("Powerballs", "bloonball.png"))]


class Power:
    def __init__(self, y, z):
        self.image = POWER[z]
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = y

    def update(self):
        self.rect.x += game_speed * 3
        if self.rect.x > SCREEN_WIDTH:
            powers.remove(self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
