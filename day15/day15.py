from queue import PriorityQueue
from collections import defaultdict

with open("input.txt") as file:
    lines = file.readlines()
    field = [[int(x) for x in line if x != "\n"] for line in lines]

start = (0,0)
end = (len(field[0])-1, len(field)-1)
c = (0,0)

q = PriorityQueue()
#d = defaultdict(bool)
#d[start] = True
def calc_dist(point, field):
    #return abs(end[0] - point[0]) + abs(end[1] - point[1]) 
    return field[point[0]][point[1]] + abs(end[0] - point[0]) + abs(end[1] - point[1]) 

def get_path(point):
    res = [point]
    while point != start:
        res.insert(0, prev_map[point])
        point = prev_map[point]
    return res
d = {c : 0}
prev_map = {}
q.put([d[c] + calc_dist((c[0], c[1]+1), field), (c[0], c[1]+1), c])
prev_map[(c[0], c[1]+1)] = start

q.put([d[c] + calc_dist((c[0]+1,c[1]),field),(c[0]+1, c[1]), c])
prev_map[(c[0]+1,c[1])] = start

mx = len(field[0])
my = len(field)
field2 = []
for j in range(0,5):
    for a in range(my):
        field2.append([])
    for i in range(0,5):
        for y in range(my):
            for x in range(mx):
                val = field[y][x] + i + j
                if val > 9:
                    val = 1 + val % 10
                field2[y + j*mx].append(val)
    
mx = len(field2[0])
my = len(field2)
print(mx,my)
end = (mx-1, my-1)
print(field2[end[0]][end[1]])
res = []
i = 0
while not q.empty():
    cur = q.get()
    c = cur[1]
    if c in d.keys():
        continue
    p = cur[2]
    cost = d[p] + field2[c[0]][c[1]]
    if c == end:
        res = [c, cost]
        break
    if c in d.keys() and cost > d[c]:
        continue
    d[c] = cost
    if c[0] + 1 < my and (c[0]+1, c[1]) and (c[0]+1, c[1]) not in d.keys():
        n1 = (c[0]+1,c[1])
        prev_map[n1] = c
        q.put([cost+calc_dist(n1,field2), n1, c])
    if c[1] + 1 < mx and (c[0], c[1]+1) and (c[0], c[1]+1) not in d.keys():
        n2 = (c[0], c[1]+1)
        prev_map[n2] = c
        q.put([cost+calc_dist(n2,field2), n2, c])
    if c[0] - 1 > 0 and (c[0]-1, c[1]) and (c[0]-1, c[1]) not in d.keys():
        n3 = (c[0]-1, c[1])
        prev_map[n3] = c
        q.put([cost+calc_dist(n3, field2), n3, c])
    if c[1] - 1 > 0 and (c[0], c[1]-1) and  (c[0], c[1]-1) not in d.keys():
        n4 = (c[0], c[1]-1)
        prev_map[n4] = c
        q.put([cost+calc_dist(n4,field2), n4, c])
    if q.empty():
        print("queue empty")
        break
    i+=1
print("here")
print(res)
exit(0)
path = get_path(res[0])
for i in range(my):
    for j in range(mx):
        if (j,i) in path:
            print(str(field2[i][j]), end="")
        else:
            print(".", end="")
    print()

print(get_path(res[0]))
