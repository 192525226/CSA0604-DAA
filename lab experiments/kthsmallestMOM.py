def kth_smallest(a, k):
    if len(a) <= 5:
        return sorted(a)[k - 1]

    groups = [a[i:i + 5] for i in range(0, len(a), 5)]
    medians = [sorted(g)[len(g) // 2] for g in groups]

    pivot = kth_smallest(medians, (len(medians) + 1) // 2)

    low = [x for x in a if x < pivot]
    high = [x for x in a if x > pivot]

    if k <= len(low):
        return kth_smallest(low, k)
    elif k == len(low) + 1:
        return pivot
    else:
        return kth_smallest(high, k - len(low) - 1)


a = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

print("Kth smallest element:", kth_smallest(a, k))