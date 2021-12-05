from collections import defaultdict

with open("input.txt") as file:
    lines = file.readlines()
    d = defaultdict(int)
    for line in lines:
        coords = line.split(" -> ")
        start = coords[0].split(',')
        to = coords[1].split(',')
        start = (int(start[0]), int(start[1]))
        to = (int(to[0]), int(to[1]))
        if start[0] == to[0]:
            dist = abs(start[1] - to[1]) + 1
            for i in range(dist):
                if start[1] > to[1]:
                    d[(start[0], to[1] + i)] += 1
                else:
                    d[(start[0], start[1] + i)] += 1
        elif start[1] == to[1]:
            dist = abs(int(start[0]) - to[0]) + 1
            for i in range(dist):
                if start[0] > to[0]:
                    d[(to[0] + i, to[1])] += 1
                else:
                    d[(start[0] + i, to[1])] += 1
        else:
            print(start, to)

            dist = abs(start[0] - to[0]) + 1
            if start[0] > to[0]:
                points = (to, start)
            else:
                points = (start, to)
            print(points)
            if points[0][1] > points[1][1]:
                offset = -1
            else:
                offset = 1
            for i in range(dist):
                d[(points[0][0]+i,points[0][1] + i*offset)] += 1
    c = 0
    for key in d.keys():
        if d[key] > 1:
            c += 1
    print(c)
    #for i in range(10):
    #    for j in range(10):
    #        if (j,i) in d.keys():
    #            print(d[(j,i)], end="")
    #        else:
    #            print(".", end="")
    #    print()
