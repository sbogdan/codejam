#!/usr/bin/env python

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

def solve(n, s, p, totals):
  count = 0

  for total in totals:
    best = total / 3 + (total % 3 <> 0)
    if best == p - 1 and s and total > 1 and total % 3 <> 1:
      s -= 1
      best += 1

    count += best >= p

  return count

if __name__ == "__main__":
  resp = Responder()
  
  for line in stdin.readlines()[1:]:
    params = map(int, line.strip().split())
    n, s, p = params[:3]
    t = params[3:]

    resp.write(solve(n, s, p, t))
