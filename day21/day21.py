from pprint import pprint
from collections import defaultdict

with open("input.txt") as file:
    lines = file.readlines()
    players = [[int(x.split()[1]), int(x.split()[-1])-1, 0] for x in lines]
print(players)

die = 2
winner = -1
turns = 0
while True:
    for (i,p) in enumerate(players):
        turns += 3
        p[1] = (p[1] + die * 3) % 10
        p[2] += p[1] + 1
        if(p[2] >= 1000):
            print(f"Player {p[0]} wins!")
            winner = p[0]
            break
        die += 3
    if winner > 0:
        break
    
print(players)
print(turns)
if winner == 1:
    print(turns * players[1][2])
else:
    print(turns * players[0][2])
test = []
for i in range(1,4):
    for j in range(1,4):
        for h in range(1,4):
            test.append(i+j+h)

d = defaultdict(int)
for t in test:
    d[t] += 1

p1 = [0]*10
p2 = [0]*10
print(p1)
pprint(d)
print(players)
#def game(players, turn, steps):
#    players[turn][1] = (players[turn][1] + steps) % 10
#    players[turn][2] += players[turn][1] + 1
#    if players[turn][2] > 20:
#        return turn
#    else:
#        turn = (turn+1)%2
#        return game(players)