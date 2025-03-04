
# Implementation
def bubble_sort(arr:list):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-1, i-1, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


# Driver Code
arr = [6,5,4,3,2,1]
print(arr)
bubble_sort(arr=arr)
print(arr)


# Early Exit Optimization for already sorted arrays
def bubble_sort_optimized(arr:list):
    l = len(arr)
    for i in range(l-1):
        swapped = False
        for j in range(l-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break  # If no two elements were swapped, the array is already sorted

