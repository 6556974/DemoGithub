import pygame
from Global import *
from Map import *
import sys
from pygame.locals import*
import numpy as np
from random import randint
from Logic import *

class draw:
    def init(self):
        pygame.init()
        size = width, height
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("LifeGame")
        return screen

    def get_rect(self,row, column):  # 计算应该在哪里画方格，以右上角为点。
        x1 = rect_width * row
        y1 = rect_width * column
        return (x1, y1, rect_width, rect_width)

    def draw_live(self,screen, x, y):
        pygame.draw.rect(screen, LifeColor, self.get_rect(x, y), 0)

    def draw_live_all(self,screen,mp):
        for i in range(1, 80 - 1):  # 所有细胞的生存状态发展
            for j in range(1, 50 - 1):
                if mp[i][j] == 1:
                    self.draw_live(screen, i, j)
                else:
                    pass

    def run(self,mp):
        while True:
            mp=logic().solve(mp,80,50)
            screen=self.init()
            screen.fill(BGColor)
            self.draw_live_all(screen,mp)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.flip()
            pygame.time.delay(100)