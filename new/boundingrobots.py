dim = input().split(" ")
while int(dim[0]) != 0 and int(dim[1]) != 0:
    r = int(dim[0]) - 1
    c = int(dim[1]) - 1
    x = 0
    y = 0
    ax = 0
    ay = 0
    walls = int(input())
    for w in range(walls):
        wal = input().split(" ")
        j = int(wal[1])
        if wal[0] == "u":
            y += j
            ay += j
        if wal[0] == "d":
            y -= j
            ay -= j
        if wal[0] == "l":
            x -= j
            ax -= j
        if wal[0] == "r":
            x += j
            ax += j
        if ay < 0:
            ay = 0
        if ax < 0:
            ax = 0
        if ay > c:
            ay = c
        if ax > r:
            ax = r
    print("Robot thinks %s %s\nActually at %s %s\n\n" % (str(x), str(y), str(ax), str(ay)))
    dim = input().split(" ")
    
