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
    return readValue(str).strip()


def solve(num):
    while True:
        untidy = 0
        for i in range(1, len(num)):
            if num[i] < num[i-1]:
                untidy = i
                break
        if not untidy:
            return num
        num = str(int(str(int(num[:untidy]) - 1)+'9'*(len(num) - untidy)))


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
