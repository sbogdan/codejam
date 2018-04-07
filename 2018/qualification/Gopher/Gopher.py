#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin, stderr, stdout


def readValue(valueType):
    return valueType(stdin.readline())

def readValues(valueType):
    return list(map(valueType, stdin.readline().split()))

def go(x, y):
    print("{} {}".format(x, y))
    stdout.flush()

    return readValues(int)

def solve():
    A = readValue(int)
    p = [[1] * 10 for _ in range(10)]
    bounds = [1, 6 if A == 20 else 60, 1, 5 if A == 20 else 50]

    def numP(x, y):
        return p[x-1][y-1] + p[x-1][y] + p[x-1][y+1] \
            + p[x][y-1] + p[x][y] + p[x][y+1] \
            + p[x+1][y-1] + p[x+1][y] + p[x+1][y+1]

    def best():
        best = None, 0
        for x in range(bounds[0] + 1, bounds[1] - 1):
            for y in range(bounds[2] + 1, bounds[3] - 1):
                num = numP(x, y)
                if best[0] is None or num > best[1]:
                    best = (x, y), num
        return best[0]

    while True:
        x, y = go(*best())
        if (x, y) == (-1, -1) or (x, y) == (0, 0):
            return

        p[x][y] = 0


if __name__ == '__main__':
    for _ in range(readValue(int)):
        solve()
