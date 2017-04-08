#!/usr/bin/python
import random
import sys

print "import random"
print "random.seed(" + str(random.randint(0, 100)) + ")"

def constantFunction(name, constant):
    print "def {}(): return {}".format(name, constant)

def indexFunction(name, n, lower, upper):
    print "_{}s=[random.randint({}, {}) for _ in xrange({})]".format(name, lower, upper, n)
    print "def {}(idx): return _{}s[idx]".format(name, name)

N = int(sys.argv[1])

constantFunction("GetIndex", N)
indexFunction("GetMultiplier", N, 1, 50)
