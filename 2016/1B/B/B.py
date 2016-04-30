#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin


def readValue(valueType):
    return valueType(stdin.readline())


def readValues(valueType):
    return list(map(valueType, stdin.readline().strip().split()))


class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    return readValues(str)

def turn(x, combo):
    for c in combo:
        x = x.replace("?", str(c), 1)
    return x

def solveBrute(score0, score1):
    num0 = score0.count("?")
    num1 = score1.count("?")
    minDiff = None
    sol = None

    for combo0 in itertools.product(range(10), repeat=num0):
        for combo1 in itertools.product(range(10), repeat=num1):
            x0 = turn(score0, combo0)
            x1 = turn(score1, combo1)
           
            diff = abs(int(x0) - int(x1))
            if sol is None:
                minDiff = diff
                sol = x0, x1
            elif diff < minDiff:
                minDiff = diff
                sol = x0, x1

    return str(sol[0]) + " " + str(sol[1])

def solve(score0, score1):
    overlap = True
    diff = 0
    for d0, d1 in zip(score0, score1):
        if d0 != "?" and d1 != "?":
            overlap = False
            diff = ord(d0) - ord(d1)
            break

    if score0[0] == "?" and score1[0] == "?" and not overlap:
        score0 = score0[1:]
        score1 = score1[1:]
        if diff > 0:
            if abs(diff) > 5:
                r0, r1 = "0", "1"
            else:
                r0, r1 = "0", "0"
        else:
            if abs(diff) > 5:
                r0, r1 = "1", "0"
            else:
                r0, r1 = "0", "0"
    else:
        r0, r1 = "", ""
    for d0, d1 in zip(score0, score1):
        if d0 != "?" and d1 != "?":
            r0 += d0
            r1 += d1
            continue

        if r0 == r1:
            if d0 == "?" and d1 == "?":
                r0 += "0"
                r1 += "0"
            elif d0 == "?":
                r0 += d1
            elif d1 == "?":
                r1 += d0
        elif r0 > r1:
            if d0 == "?" and d1 == "?":
                r0 += "0"
                r1 += "9"
            elif d0 == "?":
                r0 += "0"
            elif d1 == "?":
                r1 += "9"
        elif r1 > r0:
            if d0 == "?" and d1 == "?":
                r0 += "9"
                r1 += "0"
            elif d0 == "?":
                r0 += "9"
            elif d1 == "?":
                r1 += "0"
        
        if d0 != "?":
            r0 += d0
        if d1 != "?":
            r1 += d1

    return r0 + " " + r1

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
