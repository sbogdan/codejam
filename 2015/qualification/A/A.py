#!/usr/bin/env python3
from sys import stdin

class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    return stdin.readline().strip().split()


def solve(*args, **kwargs):
    numAdded = 0
    acc = 0

    for required, numPersons in enumerate(args[0][1]):
        delta = max(0, required - acc)
        numAdded += delta
        acc += int(numPersons) + delta

    return numAdded


if __name__ == '__main__':
    for _ in range(int(stdin.readline())):
        Mouth.answer(solve(readInput()))
