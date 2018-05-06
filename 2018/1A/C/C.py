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
    read = _
    return read

def solve(*args):
    _

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
