def kthSmallest(arr, k):
    arr.sort()          # sort the array
    return arr[k - 1]   


arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

print(kthSmallest(arr, k))
