cases = int(input())
for z in range(cases):
    o = []
    i = int(input())
    for n in range(i):
        k = input()
        if k not in o:
            o.append(k)
    print(len(o))