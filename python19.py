 # Triplet Sum Problem
# Time Complexity: O(n^2)

def tripletSum(arr, target):
    n = len(arr)
    
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Fix one element and use two pointers
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return False


# Example 1
print(tripletSum([1, 4, 45, 6, 10, 8], 13))

# Example 2
print(tripletSum([1, 2, 4, 3, 6, 7], 10))

# Example 3
print(tripletSum([40, 20, 10, 3, 6, 7], 24))
