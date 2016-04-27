#!/usr/bin/env python

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

def solve(A, B):
  count = 0
  for x in range(A, B+1):
    mirror = str(x) * 2
    x_len = len(mirror) / 2

    for i in range(x_len):
      pair = int(mirror[1+i:1+i+x_len])
      if pair == x:
        break

      count += pair > x and pair <= B

  return count

if __name__ == "__main__":
  resp = Responder()
  for line in stdin.readlines()[1:]:
    resp.write(solve(*map(int, line.split())))

