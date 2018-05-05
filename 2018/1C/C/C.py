#!/usr/bin/env python3
import math, collections, itertools
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
    N = readValue(int)
    return N, readValues(int)


def solve(*args):
    N, W = args

    best = 1
    bestW = [None] * N
    bestW[0] = W[0]

    for i, w in enumerate(W):
        for k in reversed(range(1, min(i + 1, best + 1))):
            if bestW[k-1] is not None and w * 6 >= bestW[k-1]:
                if bestW[k] is None or bestW[k] > bestW[k-1] + w:
                    bestW[k] = bestW[k-1] + w
                    best = max(best, k + 1)
        bestW[0] = min(bestW[0], w)

    return best

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
