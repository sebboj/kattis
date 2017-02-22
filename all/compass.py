s = int(input())
e = int(input())
a = 0
b = 0
if e >= s:
  a = e - s
  b = 0 - s - (360 - e)
else:
  a = (360 - s) + e
  b = -(s - e)
if abs(a) <= abs(b):
  print(a)
else:
  print(b)