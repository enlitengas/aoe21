from pprint import pprint

with open("test.txt") as file:
    lines = file.readlines()
    lines = [x.replace("\n","").split("-") for x in lines]


graph = {}
for line in lines:
    if line[0] not in graph.keys():
        graph[line[0]] = []
    graph[line[0]].append(line[1])

    if line[1] not in graph.keys():
        graph[line[1]] = []
    graph[line[1]].append(line[0])

nono = set()

paths = []

def dfs(start,end,path=[], double_dipped=False): 
    path=path+[start] 
    if start==end:
        paths.append(path)
        return

    for node in graph[start]:
        if node == "start":
            continue
        if not node.islower():
            dfs(node,end,path,double_dipped)
        elif node not in path:
            dfs(node,end,path, double_dipped)
        elif not double_dipped:
            dfs(node, end, path, True)

dfs("start","end")
#pprint(paths)

print(len(paths))