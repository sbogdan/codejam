#!/usr/bin/env python3

from sys import stdin

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print("Case #{}: {}".format(self.answer_no, answer))
    self.answer_no += 1

def solve_quadratic(a, b, c):
  d = b*b - 4*a*c
  if d < 0:
    return None
  elif d == 0:
    return -b / a / 2
  d **= 0.5
  return (-d-b) / a / 2, (+d-b) / a / 2

def pos_root(sol, gr=0):
  print(sol)
  assert sol is not None
  if type(sol) == tuple:
    sol = sol[0] if sol[0] > gr else sol[1]
  assert sol > gr
  return sol

def my_speed(t, a, v=0):
  return v*t + a*t**2/2

def other_speed(t0, d0, t1, d1):
  return (d1 - d0) / (t1 -t0)

if __name__ == "__main__":
  resp = Responder()
  for _ in range(int(stdin.readline())):
    D, N, *_ = map(float, stdin.readline().split())
    N, pos = int(N), []
    for _ in range(N):
      pos.append(list(map(float, stdin.readline().split())))
    A = list(map(float, stdin.readline().split()))
    
    while len(pos) >= 2 and pos[-2][1] >= D:
      pos.pop()
    if len(pos) >= 2 and pos[-1][1] > D:
      other_s = other_speed(pos[-2][0], pos[-2][1], pos[-1][0], pos[-1][1])
      pos[-1] = pos[-2][0] + (D - pos[-2][1]) / other_s, D
    
    print('-' * 60)
    print(D, pos, A)
    for a in A:
      print('a = ', a)
      if len(pos) == 1:
        print((D * 2 / a) ** 0.5)
        continue

      my_t = (pos[0][1] * 2 / a) ** 0.5
      my_s = a * my_t

      for i in range(1, len(pos)):
        print('{}: {}, t: {}, s: {}'.format(i-1, pos[i-1][1], my_t, my_s))
        other_s = other_speed(pos[i-1][0], pos[i-1][1], pos[i][0], pos[i][1])
        A = a / 2
        B = my_s - other_s - a * my_t
        C = a / 2 * my_t ** 2 + other_s * pos[i-1][0] - my_s * my_t
        
        t = pos_root(solve_quadratic(A, B, C), my_t)
        print('meet at:', t)

        if t >= pos[i][0]:
          tt = pos_root(solve_quadratic(a/2, my_s, pos[i-1][1] - pos[i][1]))
          my_s += tt * a
          my_t += tt
        else:
          my_t = pos[i][0]
          my_s = other_s
      print('{}: {}, t: {}, s: {}'.format(len(pos)-1, pos[-1][1], my_t, my_s))
      print('Response:', my_t)
