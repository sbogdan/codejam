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
    stdin.readline()
    return readValues(int)


def searchSolve(plates):
    seed = (tuple(sorted(plates)), 0)
    visited = set([seed])
    states = collections.deque([seed])
    if max(seed[0]) == 1:
        return 1

    while states:
        #print(states)
        cur = states.popleft()
        assert cur[0].count(0) == 0

        special = nextSpecial(cur)
        if max(special[0]) == 1:
            return special[1] + 1
        addState(special, states, visited)

        wait = nextWait(cur)
        if max(wait[0]) == 1:
            return wait[1] + 1
        addState(wait, states, visited)

    assert False, 'No solution found???'

def nextSpecial(state):
    biggestPlate = state[0][-1]
    assert max(state[0]) == state[0][-1]
    newPlates = tuple([x for x in sorted([biggestPlate//2, (biggestPlate+1)//2] + list(state[0][:-1])) if x > 0])
    return (newPlates, state[1] + 1)

def nextWait(state):
    return (tuple([x-1 for x in state[0] if x > 1]), state[1] + 1)

def addState(newState, states, visited):
    if not newState in visited:
        visited.add(newState)
        states.append(newState)


def solve(*args, **kwargs):
    plates = [0] * 1001
    best = 1001
    for plate in args[0]:
        plates[plate] += 1

    numSpecials = 0
    for pancakes in range(1000, 0, -1):
        if plates[pancakes]:
            best = min(best, pancakes + numSpecials)
            sqrt = max(int(math.sqrt(pancakes)), 2)
            totalLeft = pancakes - sqrt ** 2
            left = totalLeft

            #print(str(pancakes) + ' ' + str(plates[pancakes]) + ' ' + str(numSpecials) + ' ' + str(best))
            numSpecials += sqrt - 1
            #print(str(pancakes) + ' ' + str(sqrt)) 
            for _ in range(sqrt):
                delta = min((totalLeft+1) // sqrt, left)
                left -= delta
                #print(sqrt + delta)
                plates[sqrt + delta] += plates[pancakes]

    return best


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
