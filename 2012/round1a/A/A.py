#!/usr/bin/env python3

# flops are pretty tricky on division
from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print("Case #{}: {:.6F}".format(self.answer_no, answer))
    self.answer_no += 1

def expected():
  global A, B, P
  B -= A
  best = min(A + B + 2, 2 * A + B + 1)
  p = 1

  for a in range(0, A):
    p *= P[a]
    d = A - a - 1
    best = min(best, p * (2*d+B+1) + (1 - p) * (2*d+2*B+A+2))

  return float(best)


if __name__ == "__main__":
  resp = Responder()
  for _ in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    P = list(map(float, stdin.readline().split()))
    resp.write(expected())
