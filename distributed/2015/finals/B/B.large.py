#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

import message
from message import PutChar, PutInt, PutLL, Send
from message import Receive as Recv, GetChar, GetInt, GetLL

import kolakoski

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

from array import array

def decode(x):
    return array('B', [x & 0xFF, (x & 0xFF00) >> 8, (x & 0x0F0000) >> 16])

c3 = chr(3)
c7 = chr(7)
c1 = chr(1)

def expand(arr, last):
    xed = 0
    l, arrL = 0, 0
    while arrL < 20:
        crt = (ord(arr[arrL >> 3]) >> (arrL & 7)) & c1
        for _ in xrange(last):
            xed |= 

    return xed
    
NumNodes = message.NumberOfNodes()
MyNodeId = message.MyNodeId()

N = kolakoski.GetIndex()

lookup = [expand(decode(idx)) for idx in xrange(1 << 20)]
