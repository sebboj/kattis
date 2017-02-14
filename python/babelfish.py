import sys
pap = {}
msg = input()
while msg is not "":
    spl1t = msg.split(" ")
    pap.update({spl1t[1]:spl1t[0]})
    msg = input()
trnsltd = sys.stdin.readlines()
for line in trnsltd:
    if line[:-1] in pap:
        print(pap[line[:-1]])
    else:
        print("eh")

