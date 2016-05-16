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

def GetC(nodeId, howMany=1):
    return tuple(GetChar(nodeId) for _ in xrange(howMany))
def GetI(nodeId, howMany=1):
    return tuple(GetInt(nodeId) for _ in xrange(howMany))
def GetL(nodeId, howMany=1):
    return tuple(GetLL(nodeId) for _ in xrange(howMany))

NumNodes = message.NumberOfNodes()
MyNodeId = message.MyNodeId()

neckL = necklace.GetNecklaceLength()
neck = [necklace.GetNecklaceElement(idx) for idx in xrange(neckL)]
mesgL = necklace.GetMessageLength()
mesg = [necklace.GetMessageElement(idx) for idx in xrange(mesgL)]

if MyNodeId == 0:
    best = 0
    for start, end in ((s, e) for s in xrange(mesgL) for e in xrange(s + 1, mesgL + 1)):
        neckPos = 0
        try:
            for mesgIdx in xrange(start, end):
                neckPos = neck.index(mesg[mesgIdx], neckPos) + 1
            best = max(best, end - start)
        except ValueError:
            pass

    print best
