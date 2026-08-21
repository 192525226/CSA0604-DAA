s = input("Enter string: ")
words = input("Enter dictionary words: ").split()

n = len(s)
dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    for j in range(i):
        if dp[j] and s[j:i] in words:
            dp[i] = True
            break

if dp[n]:
    print("Word can be segmented")
else:
    print("Word cannot be segmented")