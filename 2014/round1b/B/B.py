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
    return readValues(int)


def solve(A, B, K):
    global ways
    ways = collections.Counter()

    def countWays(blockSize, prefix, A, B):
        global ways
        print('?[{}, {}, {}, {}]?'.format(blockSize, prefix, A, B))

        if blockSize == 0:
            print('[{}, {}, {}, {}]: {}'.format(blockSize, prefix, A, B, int(prefix < K)))
            return prefix < K

        if A == B and 1 << blockSize == A:
            if (blockSize, prefix) in ways:
                return ways[(blockSize, prefix)]

        numWays = 0
        numWays += countWays(blockSize - 1, prefix, blockSize, blockSize)
        numWays += countWays(blockSize - 1, prefix, A - (1 << blockSize), blockSize)
        numWays += countWays(blockSize - 1, prefix, blockSize, B - (1 << blockSize))
        numWays += countWays(blockSize - 1, prefix | (1 << blockSize), A - (1 << blockSize), B - (1 << blockSize))
        ways[(blockSize, prefix)] = numWays
        print('[{}, {}, {}, {}]: {}'.format(blockSize, prefix, A, B, numWays))
        return numWays

    blockSize = 0
    while 1 << blockSize < max(A, B):
        blockSize += 1
    return countWays(blockSize, 0, A, B)


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
