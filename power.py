import pygame
import os
from globals import *

POWER = [pygame.image.load(os.path.join("Powerballs", "musaball.png")),
         pygame.image.load(os.path.join("Powerballs", "stellaball.png")),
         pygame.image.load(os.path.join("Powerballs", "bloonball.png"))]

class Power:
    def __init__(self):
        self.x = 100
        self.y = 50
        self.image = POWER[z]
        self.width = self.image.get_width()

    def update(self):
        self.x += game_speed * 3

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
