#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin


def readValue(valueType):
    return valueType(stdin.readline())


class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    read = readValue(int)
    return read


def solve(n):
    if n == 0:
        return "INSOMNIA"

    seen, crt = set(), 0
    while len(seen) != 10:
        crt += n
        seen |= set(str(crt))
    return crt


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
