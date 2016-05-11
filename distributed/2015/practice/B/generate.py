#!/usr/bin/python
import random
import sys

N = int(sys.argv[1])
print "def GetN(): return " + str(N)

print "def GetTaste(index):"
for idx in xrange(N):
    print "  {}if index == {}: return {}".format("el" if idx > 0 else "", idx, random.randrange(-1000000, 1000000))
