#Uses python3
import sys
input = sys.stdin.read()
v,e = map(int,input.split())
graph = [[] for i in range(v)]
cc = {}
c = 0
visited = [False]*v
for i in range(e):
    p,q = map(int,input.split())
    graph[p-1].append(q-1)
    graph[q-1].append(p-1)

x,y = map(int,input.split())
def DFS():
    global cc
    global c
    global graph
    global visited
    for i in range(v):
        if not visited[i]:
            explore(i)
            c += 1

def explore(i):
    global visited
    global cc
    global c
    visited[i] = True
    cc[i] = c
    for j in graph[i]:
        if not visited[j]:
            explore(j)

DFS()
print(int(cc[x-1] == cc[y-1]))