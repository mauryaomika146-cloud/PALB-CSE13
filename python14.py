# Find the Duplicate Number

def findDuplicate(nums):
    
    # Step 1: Detect cycle
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    slow = nums[0]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


# Example 1
print(findDuplicate([1,3,4,2,2]))

# Example 2
print(findDuplicate([3,1,3,4,2]))

# Example 3
print(findDuplicate([3,3,3,3,3]))
