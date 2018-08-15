#Uses python3

import sys


def negative_cycle(adj, cost):
    result = 0
    dist = [sys.maxsize for _ in range(len(adj))]
    prev = [-1 for _ in range(len(adj))]
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for j, v in enumerate(adj[u]):
                d = dist[u] + cost[u][j]
                if dist[v] > d:
                    dist[v] = d
                    prev[v] = u
                    if i == len(adj) - 1:  # we have a negative weight cyclecycle
                        result = 1

    return result


def solve_negative_cycle(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    return negative_cycle(adj, cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    print(solve_negative_cycle(input))