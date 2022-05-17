import pygame
from Global import *
import sys
from pygame.locals import *
import numpy as np
from random import randint
from Draw import *
from Map import *
import Botton as main


def say_hello():
    print("")

def work():
    mp = np.zeros([int(width/rect_width), int(height/rect_width)])
    mp = Map().initMap()
    #print(mp)
    return mp

if __name__ == '__main__':
    #draw().run(mp)
    scr = main.Botton().init((1000, 600), "Life Game")
    la1 = main.Botton().label(30, (120, 30), "freesansbold.ttf", (255, 0, 0),
                     (255, 255, 255), "Life Game")
    la2 = main.Botton().label(20, (500, 580), "freesansbold.ttf", (0, 0, 0),
                              (255, 255, 255), "Designer:  Zhangchen   Tudian")
    la3 = main.Botton().label(7, (400, 20), "freesansbold.ttf", (255, 255, 255),
                              (0, 255, 0), "   ")
    la4 = main.Botton().label(20, (435, 20), "freesansbold.ttf", (0, 0, 0),
                              (255, 255, 255), ":Life")
    la5 = main.Botton().label(7, (700, 20), "freesansbold.ttf", (255, 255, 255),
                              (255, 0, 0), "   ")
    la6 = main.Botton().label(20, (735, 20), "freesansbold.ttf", (0, 0, 0),
                              (255, 255, 255), ":Die")
    bu1 = main.Botton().button(30, (80, 150), "freesansbold.ttf", (255, 255, 255),
                      (55, 55, 55), (255, 255, 255), (155, 155, 155), say_hello(), title="start")

    bu2 = main.Botton().button(30, (80, 270), "freesansbold.ttf", (255, 255, 255),
                      (55, 55, 55), (255, 255, 255), (155, 155, 155), say_hello(), title="pause")

    bu3 = main.Botton().button(30, (80, 390), "freesansbold.ttf", (255, 255, 255),
                      (55, 55, 55), (255, 255, 255), (155, 155, 155), say_hello(), title="reset")

    bu4 = main.Botton().button(30, (80, 510), "freesansbold.ttf", (255, 255, 255),
                      (55, 55, 55), (255, 255, 255), (155, 155, 155), say_hello(), title="random")


    main.Botton().register_cp(la1)
    main.Botton().register_cp(la2)
    main.Botton().register_cp(la3)
    main.Botton().register_cp(la4)
    main.Botton().register_cp(la5)
    main.Botton().register_cp(la6)
    main.Botton().register_cp(bu1)
    main.Botton().register_cp(bu2)
    main.Botton().register_cp(bu3)
    main.Botton().register_cp(bu4)

    main.Botton().run(scr, (0, 0, 0))