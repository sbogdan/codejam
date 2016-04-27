#!/usr/bin/env python

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

def get_max(portion):
  return 0 if not portion else max(portion)

def column(lawn, col):
  return [row[col] for row in lawn]

def mowable(lawn):
  for row in xrange(len(lawn)):
    for col in xrange(len(lawn[0])):
      if (lawn[row][col] < get_max(lawn[row][0:col]) or lawn[row][col] < get_max(lawn[row][col:])) and\
          (lawn[row][col] < get_max(column(lawn, col)[0:row]) or lawn[row][col] < get_max(column(lawn, col)[row:])):
        return False
  return True

resp = Responder()

for _ in xrange(int(stdin.readline())):
  n, m = map(int, stdin.readline().split())
  lawn = [stdin.readline().strip().split() for _ in xrange(n)]
  resp.write('YES' if mowable(lawn) else 'NO')

