#!/usr/bin/env python
import sys

class Responder:
  def __init__(self):
    self.answer_no = 1
  def write(self, answer):
    print "Case #{}: {}".format(self.answer_no, answer) 
    self.answer_no += 1

def winner(line):
  if line.replace('T','X') == 'X' * 4:
    return 'X won'
  elif line.replace('T','O') == 'O' * 4:
    return 'O won'

def state(board):
  for i in range(4):
    win = winner(board[i*4:i*4+4]) or winner(board[i:12+i+1:4]) or\
      winner(board[0:16:5]) or winner(board[12:0:-3])
    if win: return win
  if board.find('.') <> -1:
    return 'Game has not completed'
  return 'Draw'

resp = Responder()
n = int(sys.stdin.readline())
boards = sys.stdin.readlines()

for i in xrange(n):
  board = ''.join(map(str.strip, boards[i*5:i*5+4]))
  resp.write(state(board))
