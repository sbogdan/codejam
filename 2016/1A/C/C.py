#!/usr/bin/env python3
import math, collections, itertools
from itertools import permutations as perms
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
    return readValue(int), readValues(int)


def solve(n, bff):
    bff = [x - 1 for x in bff]

    for howMany in range(n, 0, -1):
        for perm in perms(range(n), howMany):
            valid = True
            perm = perm + (perm[0],)
            for i in range(howMany):
                if not bff[perm[i]] == perm[i+1] and not bff[perm[i]] == perm[i-1]:
                    valid = False
                    break
            if valid:
                return howMany


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
