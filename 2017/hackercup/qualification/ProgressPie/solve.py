#!/usr/bin/env python3
from math import *
from sys import stdin

t = int(stdin.readline())

for caseNo in range(1, t+1):
    p, x, y = [int(x) for x in stdin.readline().strip().split()]

    if not p:
        isWhite = True
    else:
        x, y = y / 50 - 1, 1 - x / 50
        r = sqrt(x * x + y * y)
        xyRad = (atan2(y, x) + 2 * pi) % (2 * pi)
        wRad = (1 - p / 100) * 2 * pi

        isWhite = r > 1 or (p != 100 and xyRad < wRad)

    print('Case #{}: {}'.format(caseNo, 'white' if isWhite else 'black'))
