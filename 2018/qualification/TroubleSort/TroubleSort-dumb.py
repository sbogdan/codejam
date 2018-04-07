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
    done = False
    while not done:
        done = True
        for i in range(len(v) - 2):
            if v[i] > v[i + 2]:
                done = False
                tmp = v[i]; v[i] = v[i+2]; v[i+2] = tmp
    return v
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return i
    return 'OK'

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
