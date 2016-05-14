import random
random.seed(39)
def NumberOfFiles(): return 1000000
def MaxDistance(): return 10000
_Identifiers=sorted([random.randint(0, 10000) for _ in xrange(1000000)])
def Identifier(idx): return _Identifiers[idx]
