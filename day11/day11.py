
map = []
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        map.append([int(x) for x in line if x != "\n"])

step = 0
flashes = 0
for row in map:
    print(row)
az = False
while not az:
    first = True
    while True:
        found = False
        if first:
            for row in map:
                for (i,cell) in enumerate(row):
                    row[i] += 1
        for (i,row) in enumerate(map):
            for (j,cell) in enumerate(row):
                if cell >= 10:
                    xstart = max(j-1,0)
                    xend = min(j+2, len(row))
                    ystart = max(i-1,0)
                    yend = min(i+2, len(map))
                    found = True
                    flashes += 1
                    map[i][j] = 0
                    for y in range(ystart, yend):
                        for x in range(xstart, xend):
                            if map[y][x] != 0:
                                map[y][x] += 1
        first = False
        if not found:
            break
    step += 1
    az = True
    for row in map:
        if any(row):
            az = False
            break
print(step)
print(flashes)
