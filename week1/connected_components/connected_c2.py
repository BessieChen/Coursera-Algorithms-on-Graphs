#Uses python3
import sys
input = sys.stdin.read()
v,e = map(int, input.split())
graph = [[] for i in range(v)]
for i in range(e):
    x,y = map(int, input.split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
visited = [False]*v
cc = {}
c = 0
def dfs():
    global graph
    global visited
    global cc
    global c
    for i in range(v):
        if not visited[i] :
            explore(i)
            c += 1
def explore(i):
    global graph
    global visited
    global c
    global cc
    visited[i] = True
    cc[i] = c
    for x in graph[i]:
        if not visited[x]:
            explore(x)
dfs()
print(c)