with open("input.txt") as file:
    data = file.read().split(",")
    data = [int(x) for x in data]
data.sort()
med = data[len(data)//2]
res = 0
for d in data:
    res += abs(d - med)
print(res)


#Part 2
res2 = 0
avg = round(sum(data) / len(data))
avg -= 1
print(avg)
for d in data:
    l = abs(d - avg)
    res2 += (l * (l+1))/2
print(res2)
