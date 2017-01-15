#!/usr/bin/env python3

from sys import stdin

t = int(stdin.readline())

for caseNo in range(t):
    n, m = tuple(map(int, stdin.readline().split()))
    dp = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        pies = sorted(list(map(int, stdin.readline().split())))

        cost = 0
        if i == 0:
            for j in range(min(m, n)):
                cost += pies[j]
                dp[0][j] = cost + (j + 1) ** 2
            continue

        for k in range(0, m + 1):
            for j in range(i - 1, n - k):
                dp[i][j + k] = min(dp[i][j + k], dp[i - 1][j] + cost + k ** 2)

            if k < m: cost += pies[k]

    print('Case #{}: {}'.format(caseNo + 1, dp[n - 1][n - 1]))
