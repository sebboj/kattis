cases = int(input())
t9 = {
    "a": 2,
    "b": 22,
    "c": 222,
    "d": 3,
    "e": 33,
    "f": 333,
    "g": 4,
    "h": 44,
    "i": 444,
    "j": 5,
    "k": 55,
    "l": 555,
    "m": 6,
    "n": 66,
    "o": 666,
    "p": 7,
    "q": 77,
    "r": 777,
    "s": 7777,
    "t": 8,
    "u": 88,
    "v": 888,
    "w": 9,
    "x": 99,
    "y": 999,
    "z": 9999,
    " ": 0,
}
for i in range(cases):
    word = input().lower()
    code = [None]*len(word)
    for l in range(len(word)):
        code[l] = t9[word[l]]
    press = ""
    for k in range(len(code)-1):
        press += str(code[k])
        if str(code[k])[-1] == str(code[k+1])[0]:
            press += " "
    press += str(code[-1])
    print("Case #%s: %s" % (str((i+1)), press))
