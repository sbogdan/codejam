#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

from message import NumberOfNodes, MyNodeId
from message import PutChar, PutInt, PutLL, Send
from message import Receive as Recv, GetChar, GetInt, GetLL

import majority

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

numNodes = NumberOfNodes() - 1
crtNodeId = MyNodeId()

N = majority.GetN()
start = N * crtNodeId / numNodes
end = N * (crtNodeId + 1) / numNodes

if crtNodeId != numNodes:
    votes = dd(int)
    maxVoted = 0
    for idx in xrange(start, end):
        voted = majority.GetVote(idx)
        votes[voted] += 1
        if maxVoted is None or votes[voted] > votes[maxVoted]:
            maxVoted = voted

    totalVotes = 0
# query nodes
    for nodeId in xrange(numNodes):
        PutC(nodeId, "Q")
        PutL(nodeId, maxVoted)
        Send(nodeId)

    votesForMaxVoted = 0
# respond to incoming queries / responses
    for nodeId in xrange(numNodes * 2):
        nodeId = Recv(-1)
        msgType = GetC(nodeId)[0]
        val = GetL(nodeId)[0]

        if msgType == "Q":
            PutC(nodeId, "R")
            PutL(nodeId, votes[val])
            Send(nodeId)
        elif msgType == "R":
            votesForMaxVoted += val

    PutL(numNodes, maxVoted if votesForMaxVoted * 2 > N else -1)
    Send(numNodes)
else:
    winnerFound = False
    for _ in xrange(numNodes):
        nodeId = Recv(-1)
        winner = GetL(nodeId)[0]

        if winner > 0 and not winnerFound:
            print winner
            winnerFound = True

    if not winnerFound:
        print "NO WINNER"
