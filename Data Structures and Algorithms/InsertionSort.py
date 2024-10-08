arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# InsertionSort
for i in range(1, len(arr)):
    print(i, end=" ")
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(arr)
