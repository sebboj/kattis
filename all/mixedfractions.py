a,b = input().split(" ")
a,b = [int(a), int(b)]
while a != 0 and b != 0:
    print("%s %s / %s" % (str(a//b), str(a%b), str(b)))
    a,b = input().split(" ")
    a,b = [int(a), int(b)]
