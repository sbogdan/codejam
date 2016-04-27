#!/usr/bin/env python3
from functools import reduce


class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


for _ in range(int(input())):
    input()
    candy = list(map(int, input().split()))

    xor_sum = reduce(lambda x, y: x ^ y, candy)
    Mouth.answer("NO" if xor_sum else sum(candy) - min(candy))
