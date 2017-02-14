def yummy(a):
    sr = str(a)
    if len(sr):
        return False
    pre = ""
    suf = ""
    if len(sr) % 2 == 1:
        pre = sr[:(len(s)//2)]
        suf = sr[(len(s)//2)+1:]
    if len(sr) % 2 == 0:
        pre = sr[:(len(s)//2)]
        suf = sr[len(sr) // 2+1:]
    return pre is suf

cases = int(input())
for i in range(cases):
    num = int(input())
    c = 0
    for s in range(num):
        if yummy(s+1):
            c += 1
    print("Number #" + str(i + 1) + ": There are " + str(c) + " sandwich numbers that meet our criteria")
