cases = int(input())
for i in range(cases):
    bookstring = input()[:-2]
    book = bookstring.split(" ")
    c = 0
    for k in range(len(book)-1):
        a = int(book[k])
        b = int(book[k+1])
        if a*2 < b:
            c += b - (a*2)
    print(c)
