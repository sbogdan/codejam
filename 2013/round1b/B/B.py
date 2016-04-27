#!/usr/bin/env python3
from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print("Case #{}: {}".format(self.answer_no, answer))
    self.answer_no += 1

NMAX = 3000
cmb = [None] * NMAX
cmb[0] = [1]
for i in range(1, NMAX):
  cmb[i] = [1]+[cmb[i-1][x]+cmb[i-1][x-1] for x in range(1,i)]+[1]

def cnt(num_partitions, num_elements):
  if num_partitions <= 1 or num_elements == 0:
    return 1.
  ret = 0
  for num_groups in range(1, min(num_elements, num_partitions) + 1):
    ret += cmb[num_elements-1][num_groups-1] * cmb[num_partitions][num_groups]
  return ret

def solve():
  base_idx = int((X + Y - 1) * (X + Y) / 2)
  delta = Y + 1 if X else (X + Y) * 2 + 1

  if base_idx + delta > N:
    return 0.
  if base_idx + X + 2 * Y + 1 <= N:
    return 1.
  
  extra = N - base_idx
  total = favorable = 0.

  for left in range(max(0, extra-X-Y), min(X+Y+1, extra+1)):
    right = extra - left
    count = cnt(left+1, right)
    favorable += right >= Y + 1 and count
    total += count
  return float(favorable) / float(total)

if __name__ == "__main__":
  resp = Responder()
  for _ in range(int(stdin.readline())):
    N, X, Y = map(int, stdin.readline().split())
    X = -X if X < 0 else X
    resp.write(solve())
