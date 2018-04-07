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
    stdin.readline()
    return readValues(int)


def solve(v):
    v0 = sorted(v[0::2])
    v1 = sorted(v[1::2])
    vv = [v0[i//2] if i % 2 == 0 else v1[i//2] for i in range(len(v))]
    for i in range(len(v) - 1):
        if vv[i] > vv[i+1]:
            return i

    return 'OK'

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
