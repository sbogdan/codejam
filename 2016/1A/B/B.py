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
    n = readValue(int)
    lines = [readValues(int) for _ in range(2*n-1)]
    return n, lines


def solve(n, lines):
    global crtRow, crtCol, missingRow
    lines = sorted(lines)
    final = [[None] * n for _ in range(n)]

    crtRow = 0
    crtCol = 0
    missingRow = None

    def placeOriz(lineNo):
        global crtRow, crtCol, missingRow
        if crtRow >= n or lineNo >= 2 * n - 1:
            return False

        if crtRow:
            for i in range(n):
                if missingRow != crtRow - 1 and lines[lineNo][i] <= final[crtRow - 1][i]:
                    return False
        for i in range(n):
            if crtCol > i and lines[lineNo][i] != final[crtRow][i]:
                return False
        for i in range(n):
            final[crtRow][i] = lines[lineNo][i]

        for i in range(n):
            prefix = [final[j][i] for j in range(crtRow)]
            found = False
            for li in range(lineNo+1, 2*n-1):
                if prefix == lines[li][:crtRow]:
                    found = True
                    break
            if not found:
                return False

        return True

    def placeVert(lineNo):
        global crtRow, crtCol, missingRow

        if crtCol >= n or lineNo >= 2 * n - 1:
            return False

        if crtCol:
            for i in range(n):
                if lines[lineNo][i] <= final[i][crtCol - 1]:
                    return False
        for i in range(n):
            if crtRow > i and missingRow != i and lines[lineNo][i] != final[i][crtCol]:
                return False

        for i in range(n):
            final[i][crtCol] = lines[lineNo][i]
        return True

    #print(lines)
    def solve(lineNo):
        global crtRow, crtCol, missingRow

        if crtRow == n and crtCol == n:
            return True

        if placeOriz(lineNo):
            crtRow += 1
            #print("oriz: " + str(lines[lineNo]) + ", " + str(lineNo))
            if solve(lineNo + 1):
                return True
            crtRow -= 1

        if placeVert(lineNo):
            crtCol += 1
            #print("vert: " + str(lines[lineNo]) + ", " + str(lineNo))
            if solve(lineNo + 1):
                return True
            crtCol -= 1

        if crtRow != n and missingRow is None:
            missingRow = crtRow
            #print("missing row: " + str(crtRow))
            crtRow += 1
            if solve(lineNo):
                return True
            crtRow -= 1
            missingRow = None

        return False

    solve(0)

    return " ".join([str(x) for x in final[missingRow]])


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
