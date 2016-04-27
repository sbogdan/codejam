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
        if answer is None:
            answer = 'NOT POSSIBLE'
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    global N, L, devs, outs, outss
    N, L = readValues(int)
    outs = list(map(list, readValues(str)))
    devs = readValues(str)
    outss = [''.join(out) for out in outs]


def doSwitch(outs, swNo):
    for out in outs:
        out[swNo] = '0' if out[swNo] == '1' else '1'


def getSwitchedOuts(cfg):
    global devs, outs
    newOuts = [[c for c in out] for out in outs]
    for swNo in cfg:
        doSwitch(newOuts, swNo)
    newOuts = [''.join(out) for out in newOuts]
    newOuts.sort()
    return newOuts

def isValid(cfg):
    global devs, outss
    newDevs = collections.Counter()
    for dev in devs:
        newDevs[''.join(c for i,c in enumerate(dev) if i in cfg)] += 1
    newOuts = collections.Counter()
    for out in outss:
        newOuts[''.join('0' if c == '1' else '1' for i,c in enumerate(out) if i in cfg)] += 1
    return newOuts == newDevs


def solve():
    global N, L, devs, outs, outss
    d = collections.deque()
    viz = set()
    devs.sort()
    outss.sort()
    if devs == outss:
        return 0
    for x in range(L):
        new = frozenset([x])
        if isValid(new):
            d.append(new)
            viz.add(new)

    while d:
        crt = d.popleft()
        newOuts = getSwitchedOuts(crt)
        #print(newOuts)
        if newOuts == devs:
            return len(crt)

        for x in range(L):
            if not x in crt:
                new = frozenset(crt | frozenset([x]))
                if not new in viz and isValid(new):
                    viz.add(new)
                    d.append(new)

    return None

if __name__ == '__main__':
    for _ in range(readValue(int)):
        readInput()
        Mouth.answer(solve())
