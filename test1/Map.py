import numpy as np
from random import randint
from Global import *

class Map:
    def __init__(self):
        self.x_rect = int(width / rect_width)
        self.y_rect = int(height / rect_width)
        self.mp = np.zeros([self.x_rect, self.y_rect])

    def initMap(self):
        for i in range(1, self.x_rect - 1):
            for j in range(1, self.y_rect - 1):
                if randint(1, 10) <= 2:
                    self.mp[i][j] = 1
                else:
                    pass
        return self.mp