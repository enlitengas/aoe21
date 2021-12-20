from collections import defaultdict

with open("input.txt") as file:
    lines = file.readlines()

state = lines[0]
rules = lines[2:]

#print(state)

#print(rules)
my_rules = {}
for rule in rules:
    k = rule[0:2]
    v = rule[6:7]
    my_rules[k] = (k[0]+v, v+k[1])

d = defaultdict(int)
nd = defaultdict(int)
step = 0
for i in range(len(state)-2):
    d[state[i:(i+2)]] += 1

while step < 40:
    nd = defaultdict(int)
    for key in d.keys():
        nd[my_rules[key][0]] += d[key]
        nd[my_rules[key][1]] += d[key]
    
    #for key in nd.keys:
        
    d = nd
    step += 1
print(d)


char_count = defaultdict(int)
dups = defaultdict(int)

for key in d.keys():
    #s += d[key]
    if key[0] == key[1]:
        dups[key[0]] = d[key]
        #w += d[key]
        #char_count[key[0]] -= d[key]
        continue
    else:
        char_count[key[0]] += d[key]
        char_count[key[1]] += d[key]
mx = 0
mn = 3210302130210321030210321030213012030210
for key in char_count.keys():
    char_count[key] = dups[key] + ((char_count[key]+1)//2)
    mx = max(char_count[key], mx)
    mn = min(char_count[key], mn)

print(char_count)
print(mx)
print(mn)
print(mx-mn)