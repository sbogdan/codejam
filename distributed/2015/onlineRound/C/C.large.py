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

idToIdx = dict()
for m in m2:
    if m > 0 and not m in idToIdx:
        idToIdx[m] = len(idToIdx)

m2Pos = [[] for i in xrange(len(idToIdx))]
for pos, m in enumerate(m2):
    if m > 0:
        m2Pos[idToIdx[m]].append(pos)

s = (n1 - 1) * MyNodeId / NumNodes
e = (n1 - 1) * (MyNodeId + 1) / NumNodes

best = -1
for i11 in xrange(s, e):
    if m1[i11] < 0:
        continue
    mv11 = m1[i11]
    if not mv11 in idToIdx:
        continue
    mv22 = idToIdx[mv11]
    if not m2Pos[mv22]:
        continue

    for i12 in xrange(i11 + 1, n1):
        if m1[i11] == m1[i12] or m1[i12] < 0:
            continue
        mv12 = m1[i12]
        if not mv12 in idToIdx:
            continue
        mv21 = idToIdx[mv12]
        if not m2Pos[mv21]:
            continue
        i21 = m2Pos[mv21][0]
        i22 = -1
        for pos in m2Pos[mv22]:
            if pos > i21:
                i22 = pos
                break
        if i22 == -1:
            continue

        if best == -1 or i12 + i22 + 2 < best:
            best = i12 + i22 + 2
    
PutL(0, best)
Send(0)

if MyNodeId == 0:
    best = -1
    for nodeId in xrange(NumNodes):
        Recv(nodeId)
        ans, = GetL(nodeId)
        if ans != -1 and (best == -1 or ans < best):
            best = ans

    print "OK" if best == -1 else best
