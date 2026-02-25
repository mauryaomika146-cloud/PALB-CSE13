def smallestSubWithSum(x, arr):
    n = len(arr)
    
    min_len = float('inf')
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        # Shrink the window while sum > x
        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    if min_len == float('inf'):
        return 0
    else:
        return min_len

x = 51
arr = [1, 4, 45, 6, 0, 19]

print("Smallest subarray length:", smallestSubWithSum(x, arr))

x1 = 100
arr1 = [1, 10, 5, 2, 7]
print("Smallest subarray length:", smallestSubWithSum(x1, arr1))