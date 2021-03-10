#!/usr/bin/python3
""" new function"""

def canUnlockAll(boxes):
  """calcule"""
  n=len(boxes)
  L1=[i for i in range(n)]
  for i in range(len(boxes)):
    if (i in boxes[i]):
      boxes[i].remove(i)
  for box in boxes:
    for box1 in box:
      if ( box1 in L1):
        L1.remove(box1)
      else:
        break
  if (L1==[] or L1==[0]):
    return True
  else:
    return False
