#!/usr/bin/python
import random
import sys

def constantFunction(name, constant):
    print "def {}(): return {}".format(name, constant)

def indexFunction(name, upperLimit, generatorFn):
    print "def {}(idx):".format(name)
    for idx in xrange(upperLimit):
        print "  {}if idx == {}: return {}".format("el" if idx else "", idx, generatorFn())

def randomGenerator():
    if random.randint(0, 3) > 0:
        return 2
    else:
        return random.randint(0, 10)

N = int(sys.argv[1])

constantFunction("GetN", N)
indexFunction("GetVote", N, randomGenerator)
