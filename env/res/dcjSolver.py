#!/usr/bin/python
from collections import defaultdict as dd, deque as dq, OrderedDict as od
from itertools import ifilter, islice, imap, izip
from itertools import combinations as combos, combinations_with_replacement as replCombos, product, permutations as perms
from random import choice, randint, random, randrange, shuffle

from message import NumberOfNodes, MyNodeId
from message import PutChar as PutC, PutInt as PutI, PutLL as PutL, Send
from message import Receive as Recv, GetChar as GetC, GetInt as GetI, GetLL as GetL

import 

numNodes = NumberOfNodes()
crtNodeId = MyNodeId()
