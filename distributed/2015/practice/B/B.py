#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

from message import NumberOfNodes, MyNodeId
from message import PutChar as PutC, PutInt as PutI, PutLL as PutL, Send
from message import Receive as Recv, GetChar as GetC, GetInt as GetI, GetLL as GetL

import sandwich

numNodes = NumberOfNodes()
crtNodeId = MyNodeId()
N = sandwich.GetN()

if crtNodeId == 0:
    bLeft = [0] * N
    bRight = [0] * N

    s = 0
    for i in xrange(N):
        s += sandwich.GetTaste(i)
        bLeft[i] = max(bLeft[i - 1], s) if i > 0 else max(s, 0)

    s = 0
    for i in xrange(N - 1, -1, -1):
        s += sandwich.GetTaste(i)
        bRight[i] = max(bRight[i + 1], s) if i < N - 1 else max(s, 0)

    best = 0
    for i in xrange(N - 1):
        best = max(best, bLeft[i] + bRight[i + 1])

    print best
