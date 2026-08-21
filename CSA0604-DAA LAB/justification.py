words = input("Enter words: ").split()
width = int(input("Enter line width: "))

n = len(words)

# dp[i] = minimum cost for first i words
dp = [float('inf')] * (n + 1)
dp[0] = 0

parent = [-1] * (n + 1)

for i in range(1, n + 1):
    length = 0

    for j in range(i, 0, -1):
        length += len(words[j - 1])

        spaces = i - j

        if length + spaces > width:
            break

        extra = width - (length + spaces)

        # Last line has no extra-space penalty
        cost = 0 if i == n else extra ** 2

        if dp[j - 1] + cost < dp[i]:
            dp[i] = dp[j - 1] + cost
            parent[i] = j - 1

# Reconstruct lines
lines = []
i = n

while i > 0:
    j = parent[i]
    lines.append(" ".join(words[j:i]))
    i = j

lines.reverse()

print("Formatted text:")
for line in lines:
    print(line)