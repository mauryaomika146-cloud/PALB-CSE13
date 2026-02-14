def min_height(arr, k):
    n = len(arr)
    arr.sort()

    # Initial difference
    result = arr[-1] - arr[0]
    small = arr[0] + k
    big = arr[-1] - k

     #smaller tower will always smaller
    #small<big
    if small > big:
        small, big = big, small

    for i in range(1, n):
        subtract = arr[i] - k
        add = arr[i] + k
        if subtract <0:
            continue

        new_min = min(small, subtract)
        new_max = max(big, add)

        result = min(result, new_max - new_min)

    return result

arr1 = [1, 5, 8, 10]
k1 = 2
print("Output:", min_height(arr1, k1))

arr2 = [3, 9, 12, 16, 20]
k2 = 3
print("Output:", min_height(arr2, k2))