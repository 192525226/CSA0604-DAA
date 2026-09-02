n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        return True

    return False


total_cost = 0
count = 0

print("Edges in MST:")

for weight, u, v in edges:
    if union(u, v):
        print(u, "-", v, ":", weight)
        total_cost += weight
        count += 1

        if count == n - 1:
            break

print("Minimum cost:", total_cost)