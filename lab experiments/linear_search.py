def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


n = int(input("Enter number of elements: "))
print("Enter the elements:")
arr = list(map(int, input().split()))

key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")