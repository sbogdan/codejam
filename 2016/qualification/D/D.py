#!/usr/bin/env python3
import math, collections, itertools
from itertools import combinations as combos
from sys import stdin


def readValue(valueType):
    return valueType(stdin.readline())

def readValues(valueType):
    return list(map(valueType, stdin.readline().split()))

class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1

def readInput():
    return readValues(int)

def genFractals(k):
    fractal = "L" * (k - 1) + "G"
    lastFractal = "G" * k

    while fractal != lastFractal:
        yield fractal
        if fractal[-1] == "L":
            fractal = fractal[:-1] + "G"
        else:
            lastL = fractal.rindex("L")
            fractal = fractal[:lastL] + "G" + "L" * (k - lastL - 1)

def expand(fractal, kernel):
    return "".join(kernel if f == "L" else "G" * len(kernel) for f in fractal)

def solvable(fractals, s):
    for combo in combos(range(len(fractals[0])), s):
        isSolution = True
        for f in fractals:
            if all(f[c] == "L" for c in combo):
                isSolution = False
                break

        if isSolution:
            return combo

def solve(k, c, s):
    fractals = list(genFractals(k))
    fractals = [(f, f) for f in fractals] 
    
    for _ in range(c - 1):
        fractals = [(expand(f[0], f[1]), f[1]) for f in fractals]

    fractals = [f[0] for f in fractals]

    for s in range(1, k+1):
        sol = solvable(fractals, s)
        if sol:
            print(sol)
            return s

def chooseBest(expands):
    def encode(tile):
        return tuple(i for i, x in enumerate(expands) if x[tile] == "L")

    dq = collections.deque()
    backlink = {}

    def findTiles(state):
        if state is None:
            return []
        tiles = findTiles(backlink[state][0])
        tiles.append(backlink[state][1])
        return tiles

    for i in range(len(expands[0])):
        e = encode(i)
        if not e:
            return [i]
        dq.append(e)
        # (parent state, tile)
        backlink[e] = (None, i)

    while True:
        crt = dq.popleft()
        #print("popped: " + str(crt))
        last = backlink[crt][1]

        crtSet = set(crt)
        for i in range(last + 1, len(expands[0])):
            intersect = tuple(sorted(set(encode(i)) & crtSet))

            if not intersect in backlink:
                backlink[intersect] = (crt, i)
                if not intersect:
                    #print("returned: " + str(findTiles(intersect)))
                    return findTiles(intersect)
                dq.append(intersect)

def solveLarge(k, c, s):
    fractals = list(genFractals(k))
    expands = list(fractals)
    tiles = list(range(k))
    c -= 1
    while c > 0:
        #print("initial:")
        #for x in expands:
           #print(x)
        expands = [expand(x, fractals[idx]) for idx, x in enumerate(expands)] 
        #print("expanded:")
        #for x in expands:
           #print(x)
        tiles = [t * k + i for t in tiles for i in range(k)]
        c -= 1

        #print("c: {}".format(c))
        bestIdx = chooseBest(expands)
        expands = [''.join(expand[idx] for idx in bestIdx) for expand in expands]
        tiles = [tiles[idx] for idx in bestIdx]
        #print(tiles)

    if len(tiles) <= s:
        return " ".join(str(t + 1) for t in tiles)
    else:
        return "IMPOSSIBLE"

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solveLarge(*readInput()))
