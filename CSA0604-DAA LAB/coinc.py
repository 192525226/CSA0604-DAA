coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

coins.sort(reverse=True)

result = []

for coin in coins:
    while amount >= coin:
        amount -= coin
        result.append(coin)

print("Coins used:", result)
print("Number of coins:", len(result))