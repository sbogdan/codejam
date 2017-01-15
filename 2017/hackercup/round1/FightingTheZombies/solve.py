#!/usr/bin/env python3

from sys import stdin

def makeBox(x0, y0, x1, y1):
    return min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)

def boxes(x, y, R):
    return [
        makeBox(x, y, x + R, y + R),
        makeBox(x, y, x - R, y + R),
        makeBox(x, y, x + R, y - R),
        makeBox(x, y, x - R, y - R)
    ]

def inBox(x, y, box):
    return x >= box[0] and x <= box[1] and y >= box[2] and y <= box[3]


t = int(stdin.readline())

for caseNo in range(t):
    N, R = tuple(map(int, stdin.readline().split()))
    X, Y = [], []
    for _ in range(N):
        x, y = tuple(map(int, stdin.readline().split()))
        X.append(x)
        Y.append(y)

    ans = 0

    for i in range(N):
        for box in boxes(X[i], Y[i], R):
            boxed = set((j for j in range(N) if inBox(X[j], Y[j], box)))

            ans = max(ans, len(boxed))

            for j in (k for k in range(N) if not k in boxed):
                for box2 in boxes(X[j], Y[j], R):
                    boxed2 = set((l for l in range(N) if inBox(X[l], Y[l], box2)))
                    if not boxed.isdisjoint(boxed2):
                        continue

                    ans = max(ans, len(boxed) + len(boxed2))


    print('Case #{}: {}'.format(caseNo + 1, ans))
