#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin

def readValue(valueType):
    return valueType(stdin.readline())

def readValues(valueType):
    return list(map(valueType, stdin.readline().split()))

def readInput():
    return readValues(int)

def jamCoins(n):
    coin = [1] + [0] * (n - 2) + [1]
    lastCoin = [1] * n

    while coin != lastCoin:
        yield coin
        if coin[n - 2] == 0:
            coin[n - 2] = 1
        else:
            at = n - 2
            while coin[at] == 1:
                coin[at] = 0
                at -= 1
            coin[at] = 1

    yield lastCoin

def toBase(jamCoin, base):
    based = 0
    for val in jamCoin:
        based = based * base + val
    return based

def firstDivisor(x):
    if x % 2 == 0:
        return 2
    for d in range(3, int(math.sqrt(x)) + 1, 2):
        if x % d == 0:
            return d
        if d > 300000:
            break

def getDivisors(jamCoin):
    divisors = []
    for base in range(2, 11):
        based = toBase(jamCoin, base)
        divisor = firstDivisor(based)

        if divisor is None:
            return []
        else:
            divisors.append(str(divisor))
    return divisors

def solve(nj):
    n, j = nj[0], nj[1]
    for jamCoin in jamCoins(n):
        divisors = getDivisors(jamCoin)
        if len(divisors) == 9:
            print("".join(list(map(str, jamCoin))) + " " + " ".join(divisors))
            j -= 1
            if j == 0:
                break

    
if __name__ == '__main__':
    for _ in range(readValue(int)):
        print("Case #1:")
        solve(readInput())
