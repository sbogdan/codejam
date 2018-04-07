#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin
from collections import deque


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
    states = deque([(prog, 0)])
    seen = set([prog])
    
    while states:
        prog, step = states.popleft()

        damage = computeDamage(prog)
        if damage <= D:
            return step

        start = 0
        while True:
            idx = prog.find('CS', start)
            if idx < 0:
                break
            
            prog_ = prog[0:idx] + 'SC' + prog[idx+2:]
            if not prog_ in seen:
                seen.add(prog_)
                states.append((prog_, step + 1))
            
            start = idx + 1

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
