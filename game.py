import pygame
import random
from decor import *
from fairy import *
from globals import *
from monster import *
from power import *

pygame.init()
pygame.mixer.music.load('ce8e6287c767e45.mp3')
pygame.mixer.music.play(-1)

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, we, JUMP_VEL, jump_vel, e, run
    f = 0
    clock = pygame.time.Clock()
    player = Fairy()
    decor = Decor()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    fo = pygame.font.SysFont('arial', 20)
    k = 0
    if f > 0:
        jump_vel = 10.5
    else:
        jump_vel = 9

    def score():
        global points, game_speed, d, jump_vel, LEVEL
        points += 1
        if points % 1000 == 0:
            game_speed += 3
        if points % 1000 == 0:
            if jump_vel <= 11:
                jump_vel += 0.2

        text = fo.render("Очки: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1100, 40)
        SCREEN.blit(text, textRect)
        lev = fo.render("Уровень: " + str(LEVEL), True, (0, 0, 0))
        levRect = lev.get_rect()
        levRect.center = (1100, 100)
        SCREEN.blit(lev, levRect)
        sp = fo.render("Скорость: " + str(game_speed), True, (0, 0, 0))
        spRect = sp.get_rect()
        spRect.center = (1100, 60)
        SCREEN.blit(sp, spRect)
        j = fo.render("Прыжок: " + str(jump_vel), True, (0, 0, 0))
        jRect = j.get_rect()
        jRect.center = (1100, 80)
        SCREEN.blit(j, jRect)

    def background():
        global x_pos_bg, y_pos_bg, jump_vel
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    global ms

    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 208, 223))
        ui = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(ui)

        if len(we) == 0:
            s = random.randint(0, 4)
            f -= 1
            if s == 0 or s == 4:
                we.append(Monster(MONSTER))
            elif s == 1:
                we.append(Bigmonster(BIGMONSTER))
            elif s == 2:
                we.append(Flymonster(FLYMONSTER))
            elif s == 3:
                we.append(Bonus(BONUS))
                f = 3
        for object in we:
            object.draw(SCREEN)
            object.update()

            # Взяли бонус
            if s == 3 and player.f_rect.colliderect(object.rect):
                if random.randint(0, 3) == 0:
                    if game_speed >= ms + 5:
                        game_speed += random.randint(-5, 5)
                    elif game_speed > ms + 5:
                        game_speed += random.randint(-5, 0)
                    else:
                        game_speed += random.randint(1, 7)
                elif random.randint(0, 3) == 1:
                    points += random.randint(50, 250)
                elif random.randint(0, 3) == 2:
                    f = 3
                elif random.randint(0, 3) == 3:
                    q = 1

            # Дотронулись Монстра
            elif player.f_rect.colliderect(object.rect):
                pygame.time.delay(2000)
                k += 1
                menu(k)
            e = 1

        background()

        decor.draw(SCREEN)
        decor.update()

        score()

        clock.tick(45)
        pygame.display.update()


def menu(de):
    global points, game_speed, z, LEVEL, ms, y, q, we, run
    i = 1
    q = 0
    z = 0
    LEVEL = 1  # начинаем с уровеня 1
    ms = 20
    game_speed = 20  # начальная скорость
    we.clear()  # предметов на поле нет

    while run:
        SCREEN.fill((255, 208, 223))
        font = pygame.font.SysFont('arial', 40)
        if de == 0:
            text = font.render("Нажмите на пробел, чтобы начать игру", True, (0, 0, 0))
        elif de > 0:
            text = font.render("Нажмите на пробел, чтобы возобновить игру", True, (0, 0, 0))
            score = font.render("ОЧКИ: " + str(points), True, (0, 0, 0))
            if points >= 1000:
                if i == 1:
                    LEVEL += 1
                    ms += 2
                    i = 0
            level = font.render("Уровень: " + str(LEVEL), True, (0, 0, 0))
            levelRect = level.get_rect()
            levelRect.center = (800, 100)
            SCREEN.blit(level, levelRect)
            scoreRect = score.get_rect()
            scoreRect.center = (1000, 100)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[z], (70, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()


menu(de=0)
