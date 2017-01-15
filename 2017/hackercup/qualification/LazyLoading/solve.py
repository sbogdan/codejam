#!/usr/bin/env python3

from sys import stdin

t = int(stdin.readline())
for caseNo in range(t):
    n = int(stdin.readline())
    w = sorted([int(stdin.readline()) for _ in range(n)])
    numTrips = 0

    l, r = 0, n - 1
    while l <= r:
        soFar = top = w[r]
        r -= 1

        while soFar < 50 and l <= r:
            l += 1
            soFar += top

        if soFar >= 50:
            numTrips += 1

    print('Case #{}: {}'.format(caseNo + 1, numTrips))
