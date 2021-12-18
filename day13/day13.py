with open("input.txt") as file:
    lines = file.readlines()
    folds = [x for x in lines if x.startswith("fold")]
    coords = [x for x in lines if x not in folds and x != "\n"]
    coords = [[int(x[0:x.index(",")]), int(x[x.index(",")+1:len(x)-1])] for x in coords]
    folds = [(x[x.index("=")-1:x.index("=")], x[x.index("=")+1:x.index("\n")]) for x in folds]
    folds = [(a,int(b)) for (a,b) in folds]

def print_map(points, maxx, maxy):
    for y in range(maxy):
        for x in range(maxx):
            if [x,y] in points:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

maxx = 0
maxy = 0
for (x,y) in coords:
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y


for fold in folds:
    (axis, val) = fold
    for i in range(len(coords)):
        if axis == 'x' and coords[i][0] > val:
            coords[i][0] = val - (coords[i][0] - val)
        elif axis == 'y' and coords[i][1] > val:
            coords[i][1] = val - (coords[i][1] - val)
    if axis == 'x':
        maxx = (maxx // 2) + 1
    else:
        maxy = (maxy // 2) + 1
rmi = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        if coords[i][0] == coords[j][0] and coords[i][1] == coords[j][1]:
            if i not in rmi:
                rmi.append(i)
rmi.sort(reverse=True)
for i in rmi:
    coords.pop(i)
coords.sort()
print(coords)
print(len(coords))
print_map(coords, maxx, maxy)
