import numpy as np
from Global import *

class logic:
    def live_num(self,mp,x, y):  # 为了避免出现ground[-1][-1]的情况，我们需要从1开始
        self.neighbour = [mp[x][y - 1], mp[x][y + 1], mp[x - 1][y], mp[x + 1][y]
            , mp[x - 1][y - 1], mp[x + 1][y - 1], mp[x - 1][y + 1], mp[x + 1][y + 1]]
        return sum(self.neighbour)

    def solve(self,mp,x,y):
        tmp_mp = np.zeros([width, height])
        tmp_mp = mp
        for i in range(1, x - 1):
            for j in range(1, y - 1):
                if mp[i][j] == 1:
                    if self.live_num(mp,i, j) != 2 and self.live_num(mp,i, j) != 3:
                        tmp_mp[i][j] = 0
                    else:
                        pass
                else:
                    if self.live_num(mp,i, j) == 3:
                        tmp_mp[i][j] = 1
                    else:
                        pass
        mp=tmp_mp
        return mp
