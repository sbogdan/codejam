#!/usr/bin/env python
from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

# ================
# PREPROC
# ================
# I have preprocessed the palindromes via gen_pal()
# Ofcourse I didn't get to the finish line
# Too late&lazy to find gen pattern
# ================

def check_pal(x):
  x = str(x)
  for i in range(len(x)/2):
    if x[i] <> x[len(x)-i-1]:
      return False
  return True

next_digit = {'0':'1', '1':'2', '2':'0'}

def inc_pal(pal):
  if all([digit == '2' for digit in pal]):
    return None
  
  l = r = (len(pal)-1)/2
  if len(pal) % 2 == 0:
    r += 1
  while pal[l] == '2':
    pal[l] = '0'
    pal[r] = '0'
    l -= 1
    r += 1
  pal[l] = pal[r] = next_digit[pal[l]]
  return pal

def gen_pal():
  yield 1
  yield 4
  yield 9
  
  num_digits = 2
  while True:
    root = ['1'] + ['0'] * (num_digits - 2) + ['1']
    
    while True:
      sqr = int(''.join(root))
      if sqr > 10 ** 100:
        return

      pal = sqr ** 2
      if check_pal(pal):
        yield pal

      # increment root
      if not inc_pal(root):
        break

    num_digits += 1

# ================
# MAIN
# ================

def count(a, b):
  return 

resp = Responder()

palis = [int(line) for line in open('palis.txt', 'r')]

for _ in xrange(int(stdin.readline())):
  a, b = map(int, stdin.readline().split())

  count = 0
  for pal in palis:
    if pal > b:
      break
    if pal >= a:
      count += 1
  resp.write(count)
