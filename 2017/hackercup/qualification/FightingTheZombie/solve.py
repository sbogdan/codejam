#!/usr/bin/env python3

from sys import stdin
import re

def toSpell(serialized):
    first = serialized.split('d')
    second = re.split('([-+])', first[1])

    return int(first[0]), int(second[0]), 0 if len(second) == 1 else (-1 if second[1] == '-' else 1) * int(second[2])

def prob(spell, h):
   x, y, z = spell
   res = [0] + [1] * y + [0] * (x - 1) * y

   for _ in range(x - 1):
       newRes = [0] + [0] * x * y
       for i in range(1, y + 1):
           for j in range(x * y - i + 1):
               if res[j] > 0:
                   newRes[j + i] += res[j]

       res = newRes

   validCount = sum(res[i] for i in range(x * y + 1) if i + z >= h)

   return validCount / y ** x

t = int(stdin.readline())

for caseNo in range(t):
    h, n = [int(x) for x in stdin.readline().split()]
    spells = [toSpell(split) for split in stdin.readline().split()]

    bestP = max(prob(spell, h) for spell in spells)

    print('Case #{}: {:1.6f}'.format(caseNo + 1, bestP))
