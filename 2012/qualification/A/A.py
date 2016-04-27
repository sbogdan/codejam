#!/usr/bin/env python

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

trans = {
    ' ': ' ', 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's',
    'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd',
    'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b',
    'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n',
    't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
    'y': 'a', 'z': 'q'}

if __name__ == "__main__":
  resp = Responder()

  for line in stdin.readlines()[1:]:
    resp.write(''.join(map(trans.get, line.strip())))
