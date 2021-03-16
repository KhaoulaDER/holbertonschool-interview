#!/usr/bin/python3
""" new function"""
def canUnlockAll(boxes):
  """calcule"""
  l = len(boxes) - 1
  List = []
  for k in boxes[0]:
      if k not in List and k <= l:
          List.append(k)
  for j in range(l + 1):
      if j in List:
          for i in boxes[j]:
              if i not in List and i <= l:
                  List.append(i)
  if (len(List) == l) or (l == 0 and len(List) == 1)):
      return True
  else:
      return False
