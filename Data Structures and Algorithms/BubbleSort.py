
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


