#!/usr/bin/python
"""Python solution to the "Sum all integers on the input" problem.

This is a sample solution to the "Sum all integers" problem. Each node sums the
elements that belong to it (that is, the ones with position equal to MyNodeId()
modulo NumberOfNodes()).

To showcase the communication a bit better, instead of sending all the results
to a "master" node, each node sends its result to the next one, accumulating the
result from the previous node. The last node prints the final result.
"""

import message
import sum_all


accumulated_sum = 0
my_id = message.MyNodeId()
pos = my_id
while pos < sum_all.GetN():
  accumulated_sum += sum_all.GetNumber(pos)
  pos += message.NumberOfNodes()
if my_id > 0:
  message.Receive(my_id - 1)
  accumulated_sum += message.GetLL(my_id - 1)
if my_id < message.NumberOfNodes() - 1:
  message.PutLL(my_id + 1, accumulated_sum)
  message.Send(my_id + 1)
else:
  print accumulated_sum
