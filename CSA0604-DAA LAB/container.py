n = int(input("Enter number of containers: "))

weights = list(map(int, input("Enter container weights: ").split()))

capacity = int(input("Enter ship capacity: "))

weights.sort()

loaded = []
total = 0

for weight in weights:
    if total + weight <= capacity:
        loaded.append(weight)
        total += weight

print("Loaded containers:", loaded)
print("Total weight:", total)
print("Number of containers:", len(loaded))