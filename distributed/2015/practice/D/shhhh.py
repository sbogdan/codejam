"""Sample input 3, in Python."""
def GetN():
  return 6


def GetLeftNeighbour(i):
  if i == 0:
    return 3
  elif i == 3:
    return 1
  elif i == 1:
    return 4
  elif i == 4:
    return 5
  elif i == 5:
    return 2
  elif i == 2:
    return 0


def GetRightNeighbour(i):
  if i == 0:
    return 2
  elif i == 2:
    return 5
  elif i == 5:
    return 4
  elif i == 4:
    return 1
  elif i == 1:
    return 3
  elif i == 3:
    return 0
