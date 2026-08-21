n = int(input("Enter number of vertices: "))

print("Enter cost matrix:")
cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True
total = 0

print("Edges:")

for _ in range(n - 1):
    minimum = float('inf')
    x = y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and cost[i][j] < minimum:
                    minimum = cost[i][j]
                    x = i
                    y = j

    print(x + 1, "-", y + 1, ":", minimum)
    total += minimum
    selected[y] = True

print("Minimum cost:", total)