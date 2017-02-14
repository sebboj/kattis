a = input()
i = 0
while i < len(a)-1:
    if a[i] == a[i+1]:
        a = a[:i] + a[i+1:]
    else:
        i += 1
print(a)
