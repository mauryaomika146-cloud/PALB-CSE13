def minSwaps(arr, k):
    n = len(arr)
    
    good = 0
    for num in arr:
        if num <= k:
            good += 1
    
    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1
    
    ans = bad
    
    for i in range(good, n):
        if arr[i - good] > k:
            bad -= 1
        if arr[i] > k:
            bad += 1
        ans = min(ans, bad)
    
    return ans


arr1 = [2, 1, 5, 6, 3]
k1 = 3

arr2 = [2, 7, 9, 5, 8, 7, 4]
k2 = 6

arr3 = [2, 4, 5, 3, 6, 1, 8]
k3 = 6

print(
    "Output:", minSwaps(arr1, k1),
    "\nOutput:", minSwaps(arr2, k2),
    "\nOutput:", minSwaps(arr3, k3)
)