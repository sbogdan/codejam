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
    R, B, C = readValues(int)
    cashiers = [readValues(int) for _ in range(C)]
    return R, B, C, cashiers

def solve(*args):
    R, B, C, cashiers = args

    def test(timeLimit):
        caps = [max(0, min(c[0], (timeLimit - c[2]) // c[1])) for c in cashiers]
        caps.sort(reverse=True)

        return sum(caps[:R]) >= B

    maxT, pow = (1 << 64) - 1, 1 << 63
    timeLimit = 0
    while pow:
        if test(maxT - (timeLimit + pow)):
            timeLimit += pow
        pow >>= 1
    
    return int(maxT - timeLimit)

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
