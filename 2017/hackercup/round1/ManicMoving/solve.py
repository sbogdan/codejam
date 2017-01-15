#!/usr/bin/env python3

from sys import stdin

t = int(stdin.readline())

for caseNo in range(t):
    n, m, k = tuple(map(int, stdin.readline().split()))
    dist = [[float("inf")] * n for _ in range(n)]

    for _ in range(m):
        i, j, c = tuple(map(int, stdin.readline().split()))

        dist[i - 1][j - 1] = min(dist[i - 1][j - 1], c)
        dist[j - 1][i - 1] = dist[i - 1][j - 1]

    s, d = [0], [0]
    for _ in range(k):
        i, j = tuple(map(int, stdin.readline().split()))

        s.append(i - 1)
        d.append(j - 1)

    for i in range(n):
        dist[i][i] = 0

    for kk in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][kk] + dist[kk][j])

    dp = [0] + [float("inf")] * k

    for i in range(1, k + 1):
        dp[i] = dp[i - 1] + dist[d[i-1]][s[i]] + dist[s[i]][d[i]]
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + dist[d[i-2]][s[i-1]] + dist[s[i-1]][s[i]]
                    + dist[s[i]][d[i-1]] + dist[d[i-1]][d[i]])

    print('Case #{}: {}'.format(caseNo + 1, dp[k] if dp[k] != float("inf") else -1))
