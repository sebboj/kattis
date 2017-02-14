import decimal

a = input()
l3n = len(a)
w = 0
l = 0
u = 0
s = 0
for i in range(l3n):
    c = ord(a[i])
    if c == 95:
        w += 1
    elif 97 <= c <= 122:
        l += 1
    elif 65 <= c <= 90:
        u += 1
    else:
        s += 1
print(round(decimal.Decimal(w/l3n), 16))
print(round(decimal.Decimal(l/l3n), 16))
print(round(decimal.Decimal(u/l3n), 16))
print(round(decimal.Decimal(s/l3n), 16))

