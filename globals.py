import pygame
import os

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
q = 0
z = 0  # персонаж 0..2
game_speed = 20  # скорость игры
we = []  # отображаемые монстры и бонусы
powers = []  # выстрелы фей
ms = 20
LEVEL = 1  # уровень
d = 0
run = True  # игра запущена

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BG = pygame.image.load(os.path.join("ot", "Track1.png"))

BONUS = [pygame.image.load(os.path.join("Bon", "musa_fairy_dust_.png")),
         pygame.image.load(os.path.join("Bon", "pylca-stelly.png"))]

MONSTER = [pygame.image.load(os.path.join("Monster", "monster.png")),
           pygame.image.load(os.path.join("Monster", "monster2.png")),
           pygame.image.load(os.path.join("Monster", "monster3.png"))]

BIGMONSTER = [pygame.image.load(os.path.join("Monster", "bigmonster.png")),
              pygame.image.load(os.path.join("Monster", "bigmonster2.png")),
              pygame.image.load(os.path.join("Monster", "bigmonster3.png"))]

FLYMONSTER = [pygame.image.load(os.path.join("fmonster", "flymonster.png")),
              pygame.image.load(os.path.join("fmonster", "flymonstrer2.png"))]
