#!/usr/bin/env python

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

if __name__ == "__main__":
  resp = Responder()
