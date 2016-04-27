#!/usr/bin/env python3
import math, collections, itertools
from collections import deque as dq
from sys import stdin


def readValue(valueType):
    return valueType(stdin.readline())


class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    return readValue(str).strip()


def solve(start):
    finish = "+" * len(start)
    queue = dq([start])
    parent = {start: None}

    def swap(pancake):
        return '+' if pancake == '-' else '-'

    def lifts(state):
        l = len(state)

        for i in range(l):
            yield "".join("".join(map(swap, state[:l-i]))[::-1] + state[l-i:])

    #print(list(lifts("-+++-")))
    def numParentsOf(state):
        if state == start:
            print(state)
            return 0
        else:
            ret = 1 + numParentsOf(parent[state])
            print(state)
            return ret

    while True:
        crt = queue.popleft()
        if crt == finish:
            return numParentsOf(crt)

        for lift in lifts(crt):
            if not lift in parent:
                parent[lift] = crt
                queue.append(lift)

def solveLarge(pancakes):
    def swap(pancake):
        return '+' if pancake == '-' else '-'

    def turn(pancakes, at):
        return list(map(swap, pancakes[:at]))[::-1] + pancakes[at:]

    pancakes = list(pancakes)
    happy = ["+"] * len(pancakes)
    howManyTurns = 0

    while not pancakes == happy:
        howManyTurns += 1
        if pancakes[0] == "-":
            at = 1
            while at < len(pancakes) and pancakes[at] == "-":
                at += 1
        else:
            at = len(pancakes)
            while pancakes[at - 1] == "+":
                at -= 1
            while pancakes[at - 1] != "+":
                at -= 1

        pancakes = turn(pancakes, at)

    return howManyTurns

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solveLarge(readInput()))
