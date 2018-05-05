#!/usr/bin/env python3
import collections, itertools, math
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict
from itertools import count, cycle, repeat, groupby, tee, zip_longest
from itertools import product, permutations, combinations, combinations_with_replacement
from sys import stderr, stdin, stdout


def readValue(valueType):
    return valueType(stdin.readline())

def readValues(valueType):
    return list(map(valueType, stdin.readline().split()))

def flushPrintln(line, fout=stdout):
    println(line, fout)
    fout.flush()

def flushPrintlns(lines, fout=stdout):
    for line in lines:
        println(line, fout)
    fout.flush()

def println(line, fout=stdout):
    if isinstance(line, str):
        print(line, file=fout)
    elif isinstance(line, collections.Iterable):
        print(' '.join(map(str, line)), file=fout)
    else:
        print(line, file=fout)

class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1

def readInput():
    return readValue(int)

def solve(args):
    N = args
    counts = [1] * N
    available = set(range(N))

    def prob(i):
        return counts[i] / sum(counts)

    for _ in range(N):
        prefs = readValues(int)
        if prefs == [-1]:
            return False
        prefs = prefs[1:]

        for p in prefs:
            counts[p] += 1

        prefs = [p for p in prefs if p in available]
        if not prefs:
            flushPrintln(-1)
        else:
            choice = min(prefs, key=prob)
            flushPrintln(choice)
            available.remove(choice)

    return True

if __name__ == '__main__':
    for _ in range(readValue(int)):
        ok = solve(readInput())
        if not ok:
            break
