#!/usr/bin/env python3

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print("Case #{}: {}".format(self.answer_no, answer))
    self.answer_no += 1

def solve():
  

if __name__ == "__main__":
  resp = Responder()
  for _ in range(stdin.readline()):
    R, N, M, K = map(int, stdin.readline().split())
    for _ in range(R):
      p = list(map(int, stdin.readline().split()))
      resp.write(solve())
