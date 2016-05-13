#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

from message import NumberOfNodes, MyNodeId
from message import PutChar, PutInt, PutLL, Send
from message import Receive as Recv, GetChar, GetInt, GetLL

import shhhh

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

numNodes = NumberOfNodes()
crtNodeId = MyNodeId()
N = shhhh.GetN()

def printAns(lDist, rDist):
    if rDist == lDist:
        print "WHATEVER " + str(min(rDist, lDist))
    elif lDist < rDist:
        print "LEFT " + str(min(rDist, lDist))
    else:
        print "RIGHT " + str(min(rDist, lDist))

if crtNodeId == 0:
    node, lDist = 0, 0
    while node != 1:
        node = shhhh.GetLeftNeighbour(node)
        lDist += 1
    node, rDist = 0, 0
    while node != 1:
        node = shhhh.GetRightNeighbour(node)
        rDist += 1
