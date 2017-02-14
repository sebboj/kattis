n, l = input().split(" ")
n, l = int(n), int(l)
s = 0
t = 0
for z in range(n):
    d, r, g = input().split(" ")
    d, r, g = int(d), int(r), int(g)
    t += d - s
    s = d
    o = t%(r+g)
    if o < r:
        t += r - o
t += l - s
print(t)
