n = int(input("Enter number of keys: "))

keys = list(map(int, input("Enter keys: ").split()))
freq = list(map(int, input("Enter frequencies: ").split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = freq[i]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')

        total = sum(freq[i:j + 1])

        for r in range(i, j + 1):
            left = dp[i][r - 1] if r > i else 0
            right = dp[r + 1][j] if r < j else 0

            dp[i][j] = min(dp[i][j], left + right + total)

print("Minimum search cost:", dp[0][n - 1])