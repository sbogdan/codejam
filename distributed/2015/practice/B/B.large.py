#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

from message import NumberOfNodes, MyNodeId
from message import PutChar, PutInt, PutLL, Send
from message import Receive as Recv, GetChar, GetInt, GetLL

import sandwich

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
N = sandwich.GetN()

start = N * crtNodeId / numNodes
end = N * (crtNodeId + 1) / numNodes

total, bestWithin, bestL, bestR = 0, 0, 0, 0
for val in (-sandwich.GetTaste(idx) for idx in xrange(start, end)):
    total += val
    bestL = max(bestL, total)
    bestR = max(bestR + val, 0)
    bestWithin = max(bestWithin, bestR)

if crtNodeId:
    PutL(0, total, bestWithin, bestL, bestR)
    Send(0)
else:
    best, dp = bestWithin, bestR

    for nodeId in xrange(1, numNodes):
        Recv(nodeId)
        part, bestWithin, bestL, bestR = GetL(nodeId, 4)

        total += part
        best = max(best, bestWithin, dp + bestL)
        dp = max(dp + part, bestR)
    print -total + best
