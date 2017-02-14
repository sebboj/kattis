#idek

absthr = int(input())
inn = list(input())
queue = []
for o in inn:
    queue.append(o == "M")
diff = 0
club = 0
while len(queue) > 0:
    curr = 1 + -2 * queue[0]
    nd = 1 + -2 ** (queue[0] + 1)
    if len(queue) == 1 or abs(curr + diff) < abs(nd + diff):
        queue.remove(queue[0])
        diff += curr
    else:
        queue.remove(queue[0]+1)
        diff += nd
    if abs(diff) > absthr:
        break
    else:
        club += 1
print(club)
