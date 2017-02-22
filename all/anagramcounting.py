import math
import sys

for s in sys.stdin:
    a = {}
    p = list(s.strip())
    for ags in p:
        if ags in a:
            a[ags] += 1
        else:
            a.update({ags: 1})
    r = math.factorial(len(p))
    z = 1
    for pap in a:
        z *= math.factorial(a[pap])
    print(r//z)
