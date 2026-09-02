n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))


parent = list(range(n))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if xroot != yroot:
        parent[yroot] = xroot
        return True

    return False


num_components = n
mst_cost = 0

print("Edges in MST:")

while num_components > 1:

    cheapest = [-1] * n

    for i, (u, v, w) in enumerate(edges):

        set1 = find(u)
        set2 = find(v)

        if set1 == set2:
            continue

        if cheapest[set1] == -1 or edges[cheapest[set1]][2] > w:
            cheapest[set1] = i

        if cheapest[set2] == -1 or edges[cheapest[set2]][2] > w:
            cheapest[set2] = i

    for node in range(n):

        if cheapest[node] != -1:

            u, v, w = edges[cheapest[node]]

            if union(u, v):
                print(u, "-", v, ":", w)
                mst_cost += w
                num_components -= 1

print("Minimum cost:", mst_cost)