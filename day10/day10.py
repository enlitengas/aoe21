from collections import deque

op = "([{<"
cl = ")]}>"

with open("input.txt") as file:
    lines = file.readlines()

def checkmatch(o, c):
    return (o == "(" and c == ")") or (o == "[" and c == "]") or (o == "{" and c == "}") or (o == "<" and c == ">")
lines = [x.replace("\n", "") for x in lines]
score = 0
scores = []
for line in lines:
    score2 = 0
    stack = deque()
    corrupt = False
    for c in line:
        if c in op:
            stack.append(c)
        elif c in cl:
            if not checkmatch(stack.pop(), c):
                if c == ")":
                    score += 3
                elif c == "]":
                    score += 57
                elif c == "}":
                    score += 1197
                elif c == ">":
                    score += 25137
                corrupt = True
                break
        else:
            print("ERROR: invalid char")
    if not corrupt:
        for i in range(len(stack)):
            score2 *= 5
            c = stack.pop()
            score2 += op.index(c) + 1
        scores.append(score2)

print(score)
scores.sort()
print(scores[len(scores)//2])

            
