def findMedian(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


arr1 = [90, 100, 78, 89, 67]
arr2 = [56, 67, 30, 79]
arr3 = [1, 2]

print(
    "Output:", findMedian(arr1),
    "\nOutput:", findMedian(arr2),
    "\nOutput:", findMedian(arr3)
)