n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter capacity: "))

items = []

for i in range(n):
    ratio = values[i] / weights[i]
    items.append((ratio, weights[i], values[i]))

items.sort(reverse=True)

profit = 0

for ratio, weight, value in items:
    if capacity >= weight:
        capacity -= weight
        profit += value
    else:
        profit += ratio * capacity
        break

print("Maximum profit:", profit)