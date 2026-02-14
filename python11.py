import heapq

def kthSmallestminHeap(arr, k):
    heapq.heapify(arr)
    for _ in range(k - 1):
        heapq.heappop(arr)
    return heapq.heappop(arr)

arr1 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k1 = 4
print("Output:", kthSmallestminHeap(arr1, k1))

arr2 = [7, 10, 4, 3, 20, 15]
k2 = 3

print("Output:", kthSmallestminHeap(arr2, k2))