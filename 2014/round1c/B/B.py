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
    readValue(str)
    return readValues(str)


def validTrain(lvl, printSol=False):
    global cars, st
    letters = set()
    crtLetter = None
    for lvlIdx in range(0, lvl + 1):
        for letter in cars[st[lvlIdx]]:
            if letter != crtLetter:
                if letter in letters:
                    return False
                letters.add(letter)
                crtLetter = letter
    return True


def rec(lvl):
    global cars, numSol, st, used

    if lvl == len(cars):
        validTrain(lvl - 1, True)
        numSol += 1
        return
    for carIdx in range(len(cars)):
        if not carIdx in used:
            st[lvl] = carIdx
            if lvl == 0 or validTrain(lvl):
                used.add(carIdx)
                rec(lvl + 1)
                used.remove(carIdx)


def solve(*args, **kwargs):
    global cars, numSol, st, used
    cars = args[0]
    numSol = 0
    st = [None] * len(cars)
    used = set()
    rec(0)
    return numSol


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
