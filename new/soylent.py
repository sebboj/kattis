cases = int(input())
for z in range(cases):
    cal = int(input())
    if cal%400 != 0:
        print(str(cal//400 + 1))
    else:
        print(str(cal//400))
