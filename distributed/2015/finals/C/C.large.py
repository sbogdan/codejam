#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

import message
from message import PutChar, PutInt, PutLL, Send
from message import Receive as Recv, GetChar, GetInt, GetLL

import necklace

def PutC(nodeId, *args):
    for arg in args:
        PutChar(nodeId, arg)
def PutI(nodeId, *args):
    for arg in args:
        PutInt(nodeId, arg)
def PutL(nodeId, *args):
    for arg in args:
        PutLL(nodeId, arg)

def tupleOrValue(gen):
    tup = tuple(gen)
    return tup[0] if len(tup) == 1 else tup

def GetC(nodeId, howMany=1):
    return tupleOrValue(GetChar(nodeId) for _ in xrange(howMany))
def GetI(nodeId, howMany=1):
    return tupleOrValue(GetInt(nodeId) for _ in xrange(howMany))
def GetL(nodeId, howMany=1):
    return tupleOrValue(GetLL(nodeId) for _ in xrange(howMany))

NumNodes = message.NumberOfNodes()
MyNodeId = message.MyNodeId()

neckL = necklace.GetNecklaceLength()
neckS = neckL * MyNodeId / NumNodes
neckE = neckL * (MyNodeId + 1) / NumNodes

def ge(positions, x):
    ans = -1

    for cntPow in xrange(12, -1, -1):
        cnt = 1 << cntPow
        if ans + cnt < len(positions) and positions[ans + cnt] >= x:
            ans += cnt
    return -1 if ans == -1 else positions[ans]

neckPos = [[] for _ in xrange(10001)]
for neckIdx in xrange(neckS, neckE):
    x = necklace.GetNecklaceElement(neckIdx)
    neckPos[x].append(neckIdx)

neckPos = map(list, map(reversed, neckPos))

mesgL = necklace.GetMessageLength()
mesg = [necklace.GetMessageElement(idx) for idx in xrange(mesgL)]
for mesgS in xrange(mesgL):
    neckIdx = neckS
    ln = 0
    for mesgIdx in xrange(mesgS, mesgL):
        neckIdx = ge(neckPos[mesg[mesgIdx]], neckIdx) + 1
        if not neckIdx:
            break
        ln += 1

    PutI(0, ln) 
Send(0)

if MyNodeId == 0:
    ans = []
    for nodeId in xrange(NumNodes):
        Recv(nodeId)
        ans.append(list((mesgS, mesgLn) for mesgS, mesgLn in enumerate(GetI(nodeId, mesgL))))

    best = 0
    for mesgStart in xrange(mesgL):
        mesgIdx = mesgStart

        for nodeAns in ans:
            for mesgS, mesgLn in nodeAns :
                if mesgIdx == mesgS:
                    mesgIdx += mesgLn
                    break

        best = max(best, mesgIdx - mesgStart)

    print best
