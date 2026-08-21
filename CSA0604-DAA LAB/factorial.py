n = int(input("Enter n: "))

dp = [1] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i * dp[i - 1]

print("Factorial:", dp[n])