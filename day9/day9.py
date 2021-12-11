
with open("in.txt") as file:
    lines = file.readlines()
    hm = []
    for line in lines:
        hm.append([int(x) for x in line if x != "\n"])

points = []
for i in range(len(hm)):
    for j in range(len(hm[i])):
        if j > 0 and hm[i][j-1] <= hm[i][j]:
            continue
        if j+1 < len(hm[i]) and hm[i][j+1] <= hm[i][j]:
            continue
        if i > 0 and hm[i-1][j] <= hm[i][j]:
            continue
        if i+1 < len(hm) and hm[i+1][j] <= hm[i][j]:
            continue
        points.append((i,j))
res = 0
for p in points:
    res += hm[p[0]][p[1]] + 1

def findbasin(point):
    res = set() 
    unexplored = [point]
    
    while len(unexplored) > 0:
        current = unexplored.pop()
        res.add(current)
        if (current[0] > 0 
                and hm[current[0]-1][current[1]] < 9
                and (current[0]-1, current[1]) not in res 
                and hm[current[0]-1][current[1]] >= hm[current[0]][current[1]]):
            unexplored.append((current[0]-1, current[1]))
        if (current[0]+1 < len(hm)
                and hm[current[0]+1][current[1]] < 9
                and (current[0]+1,current[1]) not in res
                and hm[current[0]+1][current[1]] >= hm[current[0]][current[1]]):
            unexplored.append((current[0]+1, current[1]))
        if (current[1] > 0
                and hm[current[0]][current[1]-1] < 9
                and (current[0], current[1]-1) not in res
                and hm[current[0]][current[1]-1] >= hm[current[0]][current[1]]):
            unexplored.append((current[0],current[1]-1))
        if (current[1]+1 < len(hm[0])
                and hm[current[0]][current[1]+1] < 9
                and (current[0], current[1]+1) not in res
                and hm[current[0]][current[1]+1] >= hm[current[0]][current[1]]):
            unexplored.append((current[0], current[1]+1))
    return res
res2 = 1
resl = []
ptest = []
for p in points:
    bf = findbasin(p)
#    if len(bf) < 80:
#        continue
#    a = list(bf)
#    a.sort()
#    print(a) 
#    for i in range(50, 65):#len(hm)):
#        for j in range(20,33): #len(hm[i])):
#            if (i,j) in bf:
#                print("#",end="")
#            else:
#                print(".", end="")
#        print()
#    print()
#    for i in range(50, 65):#len(hm)):
#        for j in range(20,33): #len(hm[i])):
#            print(str(hm[i][j]), end="")
#        print()
#    print()
    resl.append(len(bf))
resl.sort(reverse=True)
print(resl)
res2 = resl[0] * resl[1] * resl[2]
print(res2)
    
