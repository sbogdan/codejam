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
    return readValue(str).strip()


def solve(s):
    ans = ""
    for x in s:
        if not ans:
            ans = x
        elif x >= ans[0]:
            ans = x + ans
        else:
            ans = ans + x
    return ans


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
