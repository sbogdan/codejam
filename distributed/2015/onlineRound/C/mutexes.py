"""Sample input 2, in Python."""
def NumberOfOperations(i):
  if i == 0:
    return 5
  elif i == 1:
    return 2


def GetOperation(i, index):
  if i == 0 and index == 0:
    return 10
  elif i == 0 and index == 1:
    return -10
  elif i == 0 and index == 2:
    return 10
  elif i == 0 and index == 3:
    return 20
  elif i == 0 and index == 4:
    return 30
  elif i == 1 and index == 0:
    return 30
  elif i == 1 and index == 1:
    return 10
