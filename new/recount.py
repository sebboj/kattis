pap = {}
name = input()
while name != "***":
  if name not in pap:
    pap.update({name: 1})
  else:
    pap.update({name: (pap[name] + 1)})
  name = input()
most = 0
winner = ""
for key in pap:
  if pap[key] > most:
    most = pap[key]
    winner = key
sm = 0
for k in pap:
  if pap[k] == most:
    sm += 1
if sm > 1:
  print("Runoff!")
else:
  print(winner)



