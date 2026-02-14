# Trapping Rain Water Problem

def trapWater(arr):
    n = len(arr)
    
    left = 0
    right = n - 1
    
    left_max = 0
    right_max = 0
    
    water = 0
    
    while left <= right:
        
        if arr[left] < arr[right]:
            
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            
            left += 1
        
        else:
            
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            
            right -= 1
    
    return water


# Example 1
print(trapWater([3, 0, 1, 0, 4, 0, 2]))

# Example 2
print(trapWater([3, 0, 2, 0, 4]))

# Example 3
print(trapWater([1, 2, 3, 4]))

# Example 4
print(trapWater([2, 1, 5, 3, 1, 0, 4]))
