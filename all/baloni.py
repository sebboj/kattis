l = int(input())
ns = input().split(" ")
ns = [int(n) for n in ns]
pop = 0
arrows = 0
popped = [0] * 1000002
for s in ns:
    popped[s] += 1
    if popped[s+1] > 0:
        popped[s+1] -= 1
    else:
        arrows += 1
print(arrows)
