#!/usr/bin/env python

from sys import stdin, stderr
from collections import Counter, defaultdict as dd

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

def contains(a, b):
    '''True, if Counter "a" contains Counter "b"'''
    for key in a:
        if a[key] < b[key]:
            return False
    for key in b:
        if not key in a:
            return False
    return True

def solve(start, required, contained):
    global hand, opened, order
    key2chests = dd(list)
    for i, key in enumerate(required):
        key2chests[key].append(i)
    
    opened = set()
    order = []
    hand = Counter()
    # eq_chests[i][j] == True, if chest i include the keys in chest j
    eq_chests = [[False] * len(contained) for _ in range(len(contained))]
    for i,conti in enumerate(contained):
        for j,contj in enumerate(contained):
            if conti == contj:
                eq_chests[i][j] = contains(conti, contj)
    
    for key in start:
        hand[key] += 1
    
    def rec():
        global hand, opened, order
        print order
        
        if len(opened) == len(required):
            return True
        for key in hand:
            tried_chests = set()
            for chest in key2chests[key]:
                no_use_trying = False
                for tried_chest in tried_chests:
                    if eq_chests[tried_chest][chest]:
                        no_use_trying = True
                if no_use_trying:
                    continue # ironic
                        
                if not chest in opened:
                    order.append(chest + 1)
                    opened.add(chest)
                    hand[key] -= 1
                    hand += contained[chest]
                        
                    if rec():
                        return True

                    tried_chests.add(chest)
                    hand -= contained[chest]
                    hand[key] += 1
                    opened.remove(chest)
                    order.pop()
        return False

    if rec():
        return order
            

if __name__ == "__main__":
    resp = Responder()
    
    for _ in xrange(int(stdin.readline())):
        k, n = map(int, stdin.readline().strip().split())
        start_keys = map(int, stdin.readline().split())

        stderr.write('start keys: {}\n'.format(start_keys))
        required_key = [None] * n
        contained_keys = [None] * n
        for i in xrange(n):
            ints = map(int, stdin.readline().strip().split())
            required_key[i] = ints[0]
            contained_keys[i] = Counter()
            for key in ints[2:]:
                contained_keys[i][key] += 1

        stderr.write('required keys: {}\n'.format(required_key))
        if solve(start_keys, required_key, contained_keys):
            resp.write(' '.join(map(str, order)))
        else:
            resp.write('IMPOSSIBLE')
        
            
