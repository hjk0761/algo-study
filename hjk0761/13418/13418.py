import sys, heapq
def input(): return sys.stdin.readline().strip()

n, m = map(int, input().split())
min_edges = []
max_edges = []
for _ in range(m+1):
    i, j, h = map(int, input().split())
    heapq.heappush(min_edges, (0 if h == 1 else 1, i, j)) # 내리막길 0
    heapq.heappush(max_edges, (h, i, j)) # 오르막길 0

min_parent = [i for i in range(n+1)]
max_parent = [i for i in range(n+1)]

def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]

def union(i, j, parent):
    pi, pj = find(parent, i), find(parent, j)
    parent[max(pi, pj)] = parent[min(pi, pj)]

def solve(parent, edges, is_max=False):
    count = 0
    result = 0
    while True:
        h, i, j = heapq.heappop(edges)
        if find(parent, i) == find(parent, j):
            continue
        union(i, j, parent)
        count += 1
        result += (1-h) if is_max else h
        if count == n:
            break
    return result

_min = solve(min_parent, min_edges, False)
_max = solve(max_parent, max_edges, True)

print(_max*_max - _min*_min)
