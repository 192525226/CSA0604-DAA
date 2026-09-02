import heapq

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

source = int(input("Enter source vertex: "))

dist = [float('inf')] * n
dist[source] = 0

pq = [(0, source)]

while pq:
    current_dist, u = heapq.heappop(pq)

    if current_dist > dist[u]:
        continue

    for v, weight in graph[u]:
        distance = current_dist + weight

        if distance < dist[v]:
            dist[v] = distance
            heapq.heappush(pq, (distance, v))

print("Shortest distances:")

for i in range(n):
    print(i, ":", dist[i])