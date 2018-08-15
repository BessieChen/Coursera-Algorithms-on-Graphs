#Uses python2
v = int(raw_input())
graph = []
edges = []
def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
for i in range(v):
    x,y = map(int,raw_input().split(" "))
    for g in graph:
        edges.append([distance((x,y),g),(x,y),g])
        edges.append([distance((x,y),g),g,(x,y)])
    graph.append((x,y))

def kruskal(graph,edges):
    result = []
    find = {}
    for i in range(len(graph)):
        find[graph[i]] = i
    edges = sorted(edges)
    for e in edges:
        if find[e[1]] != find[e[2]]:
            temp = find[e[2]]
            result.append(e[0])
            for x in find:
                if find[x] == temp:
                    find[x] = find[e[1]]
    return sum(result)

print kruskal(graph,edges)