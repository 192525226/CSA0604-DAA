import heapq

freq = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}

heap = [[weight, [char, ""]] for char, weight in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    low = heapq.heappop(heap)
    high = heapq.heappop(heap)

    for pair in low[1:]:
        pair[1] = '0' + pair[1]

    for pair in high[1:]:
        pair[1] = '1' + pair[1]

    heapq.heappush(
        heap,
        [low[0] + high[0]] + low[1:] + high[1:]
    )

codes = sorted(heapq.heappop(heap)[1:], key=lambda x: x[0])

print("Huffman Codes:")

for char, code in codes:
    print(char, ":", code)