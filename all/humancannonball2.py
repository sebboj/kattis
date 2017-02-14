import math

cases = int(input())
for z in range(cases):
    v0, theta, x1, h1, h2 = input().split()
    v0 = float(v0)
    theta = math.radians(float(theta))
    x1 = float(x1)
    h1 = float(h1)
    h2 = float(h2)
    t = x1 / (v0 * math.cos(theta))
    y = v0 * t * math.sin(theta) - (0.5 * 9.81 * t * t)
    if h1 + 1 <= y <= h2 - 1:
        print("Safe")
    else:
        print("Not Safe")

