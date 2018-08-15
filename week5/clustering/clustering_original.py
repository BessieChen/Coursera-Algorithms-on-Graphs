#Uses python2
v = int(raw_input())
def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
graph = []
edges = []
for i in range(v):
    curr = tuple(map(int,raw_input().split(" ")))
    for x in graph:
        edges.append([distance(x,curr),x,curr])
        edges.append([distance(x,curr),curr,x])
    graph.append(curr)

k = int(raw_input())

def full(find,k):
    temp = list(set([find[x] for x in find]))
    return len(temp) == k


def kruskal(graph,edges,k):
    find = {}
    result = []
    for i in range(v):
        find[graph[i]] = i
    edges = sorted(edges)
    for e in range(len(edges)):
        if full(find,k):
            raw = edges[e:]
            for z in raw:
                if find[z[1]] != find[z[2]]:
                    return z[0]
        x = edges[e]
        if find[x[1]]!=find[x[2]]:
            result.append(x[0])
            for j in find:
                temp = find[x[2]]
                if find[j] == temp:
                    find[j] = find[x[1]]

print kruskal(graph,edges,k)