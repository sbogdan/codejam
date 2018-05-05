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
    N, L = readValues(int)
    words = [readValue(str).strip() for _ in range(N)]

    return N, L, words


def solve(args):
    N, L, words = args
    words.sort()
    #print(N, L, words)

    for ln in range(1, L):
        prefixes = [word[:ln] for word in words]
        crtPrefix = prefixes[0]
        crtPrefixLetters = set([words[0][ln]])
        letters = set(w[ln] for w in words)
        
        for idx in range(N):
            prefix = prefixes[idx]
            if prefix == crtPrefix:
                crtPrefixLetters.add(words[idx][ln])
            else:
                if letters != crtPrefixLetters:
                    break

                crtPrefix = prefix
                crtPrefixLetters = set([words[idx][ln]])

        if letters != crtPrefixLetters:
            return crtPrefix + next(iter(letters-crtPrefixLetters)) + words[0][ln+1:]

    return '-'


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
