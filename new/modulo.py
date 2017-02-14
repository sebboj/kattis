a = []
b = 0
for z in range(10):
    a.append(int(input()) % 42)
used = []
for o in range(10):
    c = a[o]
    if c not in used:
        b += 1
    used.append(c)
print(b)
