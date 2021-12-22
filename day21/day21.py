from pprint import pprint
from collections import defaultdict

with open("test.txt") as file:
    lines = file.readlines()
    players = [[int(x.split()[1]), int(x.split()[-1])-1, 0] for x in lines]

die = 2
winner = -1
turns = 0
#while True:
#    for (i,p) in enumerate(players):
#        turns += 3
#        p[1] = (p[1] + die * 3) % 10
#        p[2] += p[1] + 1
#        if(p[2] >= 1000):
#            print(f"Player {p[0]} wins!")
#            winner = p[0]
#            break
#        die += 3
#    if winner > 0:
#        break
#    
#print(players)
#print(turns)
#if winner == 1:
#    print(turns * players[1][2])
#else:
#    print(turns * players[0][2])
test = []
for i in range(1,4):
    for j in range(1,4):
        for h in range(1,4):
            test.append(i+j+h)

d = defaultdict(int)
for t in test:
    d[t] += 1

p1 = [0]*10
p1[players[0][1]] = 1
p2 = [0]*10
p2[players[1][1]] = 1
print(players)
print(p1)
scores1 = [0]*22
scores2 = [0]*22
p2wins = 0
p1wins = 0
pprint(d)
turn = 0
while True:
    player = None
    sb = None
    if turn == 0:
        player = p1
        sb = scores1
    else:
        player = p2
        sb = scores2
    for pos in player:
        pass
    break

states = {}
print("start")
for t in range(2):
    p1 = (t+1)%2
    p2 = t
    for i in range(10):
        for j in range(10):
            for x in range(21):
                for y in range(21):
                    for d in range(3):
                        pos1 = p1*(i+d) % 10
                        pos2 = p2*(j+d) % 10
                        score1 = (pos1+1)*p1
                        score2 = (pos2+1)*p2
                        states[(i,j,x,y,d,t)] = (pos1,pos2,score1,score2,d,(t+1)%2)

curr = (players[0][1], players[1][1], 0, 0, 1, 0)
print(states[curr])
while True:
    nextstates = {}
    for key in d:
        nstate = 0
#def game(players, turn, steps):
#    players[turn][1] = (players[turn][1] + steps) % 10
#    players[turn][2] += players[turn][1] + 1
#    if players[turn][2] > 20:
#        return turn
#    else:
#        turn = (turn+1)%2
#        return game(players)