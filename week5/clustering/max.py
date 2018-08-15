#Uses python3
import sys
import queue
from math import sqrt


def distance(a,b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def clustering(x, y, k):
    q = queue.PriorityQueue()
    sets = [set([i]) for i in range(len(x))]
    nb_sets = len(x)
    for i,aa in enumerate(x):
        for j in range(i+1, len(x)):
            q.put((distance( (x[i],y[i]), (x[j], y[j])), (i,j) ))

    dis = 0
    while not q.empty() and nb_sets >= k:
        e = q.get()
        u = e[1][0]
        v = e[1][1]
        dis = e[0]
        set_uv = [s for s in sets if u in s or v in s]

        if len(set_uv) > 1 and set_uv[0].isdisjoint(set_uv[1]):
            unionset = set_uv[0].union(set_uv[1])
            sets.remove(set_uv[0])
            sets.remove(set_uv[1])
            sets.append(unionset)
            nb_sets -= 1
    return dis


def solve_clustering(input):
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    return clustering(x, y, k)


if __name__ == '__main__':
    input = sys.stdin.read()

    print("{0:.9f}".format(solve_clustering(input)))
