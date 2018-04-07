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
    read = readValues(str)
    return int(read[0]), read[1]

def computeDamage(prog):
    total, crt = 0, 1
    for instr in prog:
        if instr == 'C':
            crt *= 2
        else:
            total += crt

    return total

def solve(D, prog):
    numHacks = 0

    while True:
        if computeDamage(prog) <= D:
            return numHacks

        idx = prog.rfind('CS')
        if idx < 0:
            break

        prog = prog[:idx] + 'SC' + prog[idx+2:]
        numHacks += 1
        
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
