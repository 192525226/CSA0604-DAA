n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (source destination weight):")
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))

dist = [float('inf')] * n
dist[source] = 0

# Dynamic relaxation
for _ in range(n - 1):
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

print("Shortest distances:")
for i in range(n):
    print(i, ":", dist[i])