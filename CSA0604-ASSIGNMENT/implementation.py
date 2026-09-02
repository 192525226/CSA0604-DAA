import heapq
import time

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

def kruskal(vertices, edges):
    dsu = DSU(vertices)
    mst = []
    total = 0

    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == vertices - 1:
                break

    return mst, total

def prim(vertices, edges):
    adj = [[] for _ in range(vertices)]

    for w, u, v in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = [False] * vertices
    heap = [(0, 0, -1)]
    mst = []
    total = 0

    while heap and len(mst) < vertices - 1:
        w, v, parent = heapq.heappop(heap)

        if visited[v]:
            continue

        visited[v] = True

        if parent != -1:
            mst.append((parent, v, w))
            total += w

        for nw, nv in adj[v]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv, v))

    return mst, total

v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []

for _ in range(e):
    u, w, cost = map(int, input().split())
    edges.append((cost, u - 1, w - 1))

start = time.perf_counter()
kmst, kcost = kruskal(v, edges)
kend = time.perf_counter()

start2 = time.perf_counter()
pmst, pcost = prim(v, edges)
end2 = time.perf_counter()

print("\nKruskal MST:")
for u, w, cost in kmst:
    print(u + 1, w + 1, cost)
print("Total cost:", kcost)
print("Execution time:", kend - start, "seconds")

print("\nPrim MST:")
for u, w, cost in pmst:
    print(u + 1, w + 1, cost)
print("Total cost:", pcost)
print("Execution time:", end2 - start2, "seconds")
print("Minimum costs equal:", kcost == pcost)