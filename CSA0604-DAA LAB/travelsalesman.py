n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

N = 1 << n
dp = [[float('inf')] * n for _ in range(N)]

dp[1][0] = 0

for mask in range(N):
    for u in range(n):
        if mask & (1 << u):
            for v in range(n):
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + cost[u][v]
                    )

answer = float('inf')

for i in range(n):
    answer = min(answer, dp[N - 1][i] + cost[i][0])

print("Minimum cost:", answer)