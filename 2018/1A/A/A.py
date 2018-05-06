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
    R, C, H, V = readValues(int)
    cookie = [list(map(lambda c: 1 if c == '@' else 0, readValue(str).strip())) for _ in range(R)]
    return R, C, H, V, cookie

def solve(*args):
    R, C, H, V, cookie = args

    NC = sum(sum(c) for c in cookie)
    if NC % ((H+1) * (V+1)):
        return 'IMPOSSIBLE'

    vCuts, sumSoFar = [], 0
    for c in range(C):
        sumSoFar += sum(cookie[r][c] for r in range(R))
        if sumSoFar > NC / (V+1):
            return 'IMPOSSIBLE'
        if sumSoFar == NC / (V+1) and len(vCuts) < V:
            vCuts.append(c)
            sumSoFar = 0
    if len(vCuts) != V or sumSoFar != NC / (V+1):
        return 'IMPOSSIBLE'

    hCuts, sumSoFar = [], 0
    for r in range(R):
        sumSoFar += sum(cookie[r][c] for c in range(C))
        if sumSoFar > NC / (H+1):
            return 'IMPOSSIBLE'
        if sumSoFar == NC / (H+1) and len(hCuts) < H:
            hCuts.append(r)
            sumSoFar = 0
    if len(hCuts) != H or sumSoFar != NC / (H+1):
        return 'IMPOSSIBLE'

    hCut, vCut = 0, 0
    slices = [[0] * (V+1) for _ in range(H+1)]
    for r, c in product(range(R), range(C)):
        if c == 0:
            vCut = 0
            if hCut != H and hCuts[hCut] == r - 1:
                hCut += 1

        slices[hCut][vCut] += cookie[r][c]

        if vCut != V and vCuts[vCut] == c:
            vCut += 1

    return 'POSSIBLE' if len(set(s for ss in slices for s in ss)) == 1 else 'IMPOSSIBLE'

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
