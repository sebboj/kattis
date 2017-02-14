hands, dom = input().split(" ")
hands = int(hands)
tot = 0
for z in range(hands * 4):
    s = input()
    card = s[0]
    suit = s[1]
    if card == "A":
        tot += 11
    elif card == "K":
        tot += 4
    elif card == "Q":
        tot += 3
    elif card == "T":
        tot += 10
    elif card == "J" and dom == suit:
        tot += 20
    elif card == "J" and dom != suit:
        tot += 2
    elif card == "9" and dom == suit:
        tot += 14
print(tot)



