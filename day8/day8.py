with open("input.txt") as file:
    lines = file.readlines()
    data = [x.split('|') for x in lines]
    data = [[a,b.replace("\n","")] for [a,b] in data]

res = 0
for t in data:
    l = t[1].split()
    for word in l:
        if len(word) == 2:
            res += 1
        elif len(word) == 4:
            res += 1
        elif len(word) == 3:
            res += 1
        elif len(word) == 7:
            res += 1
print(res)
