sebby = print
path = []
kitten = int(input())
path.append(kitten)
tree = []
branch = input()
while branch != "-1":
    tree.append(branch)
    branch = input()
atbottom = False
curr = str(kitten)
d = 0
while not atbottom:
    d = 1
    for b in tree:
        if curr in b[b.find(" ")+1:].split(" "):
            path.append(int(b[:b.find(" ")]))
            curr = b[:b.find(" ")]
            d = 0
    if d == 1:
        atbottom = not atbottom
thepath = ""
for s in range(len(path)):
    thepath += str(path[s]) + " "
sebby(thepath[:-1])

