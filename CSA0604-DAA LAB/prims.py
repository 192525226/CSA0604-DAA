n = int(input("Enter number of vertices: "))

print("Enter cost matrix:")
cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True

total_cost = 0

print("Edges in MST:")

for _ in range(n - 1):

    minimum = float('inf')
    x = y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and cost[i][j] != 0:
                    if cost[i][j] < minimum:
                        minimum = cost[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", minimum)

    total_cost += minimum
    selected[y] = True

print("Minimum cost:", total_cost)