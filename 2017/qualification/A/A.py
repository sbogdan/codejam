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
    pancakes, k = readValue(str).split()
    return pancakes, int(k)


def solve(pancakes, k):
    numSteps = 0
    while True:
        f = pancakes.find('-')
        if f == -1:
            return numSteps
        if len(pancakes) - f < k:
            return 'IMPOSSIBLE'

        numSteps += 1
        pancakes = ''.join(p if i < f or i >= f + k else '+' if p == '-' else '-' for i, p in enumerate(pancakes))


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
