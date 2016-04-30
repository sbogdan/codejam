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


numbers = [
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
]

_fr = [0] * 26

def recurse(last):
    global fr
    if sum(_fr) == 0:
        return ''
    for idx in range(last, len(numbers)):
        for letter in numbers[idx]:
            _fr[code(letter)] -= 1
        if all(x >= 0 for x in _fr):
            further = recurse(last)
            if further is not None:
                return str(idx) + further
        for letter in numbers[idx]:
            _fr[code(letter)] += 1
    return None

def code(let):
    return ord(let) - ord('A')

def solve(coded):
    global _fr
    _fr = [0] * 26
    for letter in coded:
        _fr[code(letter)] += 1

    return recurse(0)

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
