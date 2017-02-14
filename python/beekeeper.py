#umm why is it not accepting??

def vowels(w):
    v = {
        "aa":1,
        "ee":1,
        "ii":1,
        "oo":1,
        "uu":1,
        "yy":1
    }
    score = 0
    if len(w) <= 2:
        if w in v:
            score += 1
    else:
        for lol in range(len(w)-1):
            if w[lol:lol+2] in v:
                score += 1
    return score

words = int(input())
while words != 0:
    z = []
    for o in range(words):
        z.append(input())
    m4x = vowels(z[0])
    best = z[0]
    for word in z:
        i = vowels(word)
        if i > m4x:
            m4x = i
            best = word
    print(best)
    words = int(input())

