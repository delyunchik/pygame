import pygame
import os
from globals import *

RUNNING = [pygame.image.load(os.path.join("fiary", "musa_harmonix_by_fenixfairy_d8wcs91-fullview.png")),
           pygame.image.load(os.path.join("fiary", "34d95c2dc9b57f3a1182c1366821a00d.jpg")),
           pygame.image.load(os.path.join("fiary", "bloom-flora-musa-aisha-tecna-animation.png"))]

JUMPING = [pygame.image.load(os.path.join("fiary", "be2c321caf6b181f7326926dad281efc.png")),
           pygame.image.load(os.path.join("fiary", "2c087835dcfd7dfbee68d0506287cec1.png")),
           pygame.image.load(os.path.join("fiary", "bloom_sirenix_by_miaenchantedfairy_d9cpkkd-pre.png"))]

DUCKING = [pygame.image.load(os.path.join("fiary", "musa.png")),
           pygame.image.load(os.path.join("fiary", "stella_sirenix_render_by_bloomsama_d8rrdoq-pre.png")),
           pygame.image.load(os.path.join("fiary", "bloom.png"))]

class Fairy:
    X_POS = 30
    Y_POS = 205
    Y_POS_DUCK = 270
    JUMP_VEL = 9

    def __init__(self, z):
        self.z = z
        
        self.duck_img = DUCKING[z]
        self.run_img = RUNNING[z]
        self.jump_img = JUMPING[z]
        self.fly = DUCKING[z]

        self.f_duck = False
        self.f_run = True
        self.f_jump = False
        self.fly = False

        self.step_index = 0
        self.f_vel = self.JUMP_VEL
        self.image = self.run_img
        self.f_rect = self.image.get_rect()
        self.f_rect.x = self.X_POS
        self.f_rect.y = self.Y_POS

    def update(self, userInput):
        global q
        if q == 1:
            if self.fly:
                self.f
        if self.f_duck:
            self.duck()
        if self.f_run:
            self.run()
        if self.f_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0
        if q == 1 and (userInput[pygame.K_UP] or userInput[pygame.K_w]):
            h = 1
            d = 0
            self.f_duck = False
            self.f_run = False
            self.f_jump = False
            self.fly = True
        elif q == 1 and (userInput[pygame.K_DOWN] or userInput[pygame.K_s]):
            h = 0
            d = 1
            self.f_duck = False
            self.f_run = False
            self.f_jump = False
            self.fly = True
        if (userInput[pygame.K_UP] or userInput[pygame.K_w]) and not self.f_jump and q == 0:
            self.f_duck = False
            self.f_run = False
            self.f_jump = True
        elif (userInput[pygame.K_DOWN] or userInput[pygame.K_s]) and not self.f_jump and q == 0:
            self.f_duck = True
            self.f_run = False
            self.f_jump = False
        elif not (self.f_jump or userInput[pygame.K_DOWN] or userInput[pygame.K_w]) and q == 0:
            self.f_duck = False
            self.f_run = True
            self.f_jump = False
        if userInput[pygame.K_a]:
            self.z += 1
            if self.z > 2:
                self.z = 0
            self.duck_img = DUCKING[self.z]
            self.run_img = RUNNING[self.z]
            self.jump_img = JUMPING[self.z]

    def duck(self):
        self.image = self.duck_img
        self.f_rect = self.image.get_rect()
        self.f_rect.x = self.X_POS
        self.f_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img
        self.f_rect = self.image.get_rect()
        self.f_rect.x = self.X_POS
        self.f_rect.y = self.Y_POS
        self.step_index += 1

    def f(self, h, d):
        if h == 1:
            if self.X_POS <= 590:
                self.f_rect.x = self.X_POS + 10
        elif d == 0:
            if self.X_POS >= 10:
                self.f_rect.x = self.X_POS - 10

    def jump(self):
        self.image = self.jump_img
        if self.f_jump:
            self.f_rect.y -= self.f_vel * 4
            self.f_vel -= 0.8
        if self.f_vel < - self.JUMP_VEL:
            self.f_jump = False
            self.f_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.f_rect.x, self.f_rect.y))
