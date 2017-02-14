cases = int(input())
for z in range(cases):
    num = int(input())
    out = ""
    b = False
    for o in range(4):
        for i in range(4):
            for n in range(4):
                if o == 0:
                    out += "4 * 4"
                elif o == 1:
                    out += "4 // 4"
                elif o == 2:
                    out += "4 + 4"
                else:
                    out += "4 - 4"
                if i == 0:
                    out += " * 4"
                elif i == 1:
                    out += " // 4"
                elif i == 2:
                    out += " + 4"
                else:
                    out += " - 4"
                if n == 0:
                    out += " * 4"
                elif n == 1:
                    out += " // 4"
                elif n == 2:
                    out += " + 4"
                else:
                    out += " - 4"
                if eval(out) == num and not b:
                    while "//" in out:
                        out = out[:out.find("//")] + "/" + out[out.find("//")+2:]
                    print(out + " = " + str(num))
                    b = True
                out = ""
    if not b:
        print("no solution")

