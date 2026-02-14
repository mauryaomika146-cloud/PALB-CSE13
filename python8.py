# Search Insert Position

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If not found, left will be the correct insert position
    return left

nums = [1, 3, 5, 6]
target = 5
print("Output:", searchInsert(nums, target))
