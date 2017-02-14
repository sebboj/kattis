p = int(input())
sum = 0
for po in range(p):
    n = input()
    pow = int(n[-1])
    num = int(n[:-1])
    sum += num ** pow
print(sum)