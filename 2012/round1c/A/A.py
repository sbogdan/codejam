#!/usr/bin/env python3

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print("Case #{}: {}".format(self.answer_no, answer))
    self.answer_no += 1

def solve(G):
  def dfs_root(x):
    st, v = [x], set([x])
    while st:
      crt = st.pop()
      for dad in G[crt]:
        if dad in v:
          return True
        st.append(dad)
        v.add(dad)

  for n in range(len(G)):
    if dfs_root(n):
      return 'Yes'
  return 'No'

def dec(x):
  return int(x) - 1

if __name__ == "__main__":
  resp = Responder()
  for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    G = [None] * N

    for idx in range(N):
      _, *dads = map(dec, stdin.readline().split())
      G[idx] = dads

    resp.write(solve(G))
