def even(a):
    return a % 2 == 0


def odd(b):
    return b % 2 == 1


def toIntArr(c):
    o = [0]*len(c)
    for x in range(len(o)):
        o[x] = int(c[x])
    return o

cases = int(input())
for i in range(cases):
    nums = int(input())
    coins = input().split(" ")
    coins = toIntArr(coins)
    more = 0
    more1 = 0
    for u in range(len(coins)):
        if even(u+coins[u]):
            more += 1
        if odd(u+coins[u]):
            more1 += 1
    if more < more1:
        print("Row #" + str(i + 1) + ": Jerry needs to add a minimum of " + str(more) + " coins")
    else:
        print("Row #" + str(i + 1) + ": Jerry needs to add a minimum of " + str(more1) + " coins")


