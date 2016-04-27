#!/usr/bin/env python3
from sys import stdin


def read_int(f=stdin):
    return int(f.readline())


def read_ints(f=stdin):
    return list(map(int, f.readline().split()))


class Mouth(object):
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def solve(buttons):
    code = {'O': 0, 'B': 1}
    # pos, delta 
    state = [[1, 0], [1, 0]]
    time = 0
    for color, pos in buttons:
        robot = code[color]
        other = robot ^ 1

        delta = max(
            abs(pos - state[robot][0]) + 1 - state[robot][1],
            1)
        state[robot] = [pos, 0]
        state[other][1] += delta
        time += delta

    return time


t = read_int()
for _ in range(t):
    buttons = stdin.readline().strip().split()
    buttons = [(buttons[idx], int(buttons[idx + 1])) 
               for idx in range(1, len(buttons), 2)]
    ans = solve(buttons)
    Mouth.answer(ans)
