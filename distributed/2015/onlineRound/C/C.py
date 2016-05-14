#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

import message
from message import PutChar, PutInt, PutLL, Send
from message import Receive as Recv, GetChar, GetInt, GetLL

import mutexes

def PutC(nodeId, *args):
    for arg in args:
        PutChar(nodeId, arg)
def PutI(nodeId, *args):
    for arg in args:
        PutInt(nodeId, arg)
def PutL(nodeId, *args):
    for arg in args:
        PutLL(nodeId, arg)

def GetC(nodeId, howMany=1):
    return tuple(GetChar(nodeId) for _ in xrange(howMany))
def GetI(nodeId, howMany=1):
    return tuple(GetInt(nodeId) for _ in xrange(howMany))
def GetL(nodeId, howMany=1):
    return tuple(GetLL(nodeId) for _ in xrange(howMany))

NumNodes = message.NumberOfNodes()
MyNodeId = message.MyNodeId()

n1 = mutexes.NumberOfOperations(0)
m1 = [mutexes.GetOperation(0, i) for i in xrange(n1)]
n2 = mutexes.NumberOfOperations(1)
m2 = [mutexes.GetOperation(1, i) for i in xrange(n2)]

if MyNodeId == 0:
    best = None
    for m11 in xrange(n1 - 1):
        for m12 in xrange(m11, n1):
            if not m1[m11] > 0 or not m1[m12] > 0:
                continue
            if not m2.count(m1[m11]) or not m2.count(m1[m12]):
                continue
            m21 = m2.index(m1[m12])

            if not m1[m11] in m2[m21 + 1:]:
                continue
            m22 = m2.index(m1[m11], m21 + 1)

            ans = m12 + m22 + 2
            if best is None or ans < best:
                best = ans

    if best is not None:
        print best
    else:
        print "OK"
