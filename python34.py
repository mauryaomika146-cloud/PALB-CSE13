def jump(nums):
    jumps = 0
    end = 0
    maxReach = 0
    
    for i in range(len(nums) - 1):
        maxReach = max(maxReach, i + nums[i])
        
        if i == end:
            jumps += 1
            end = maxReach
    
    return jumps


nums1 = [2,3,1,1,4]
nums2 = [2,3,0,1,4]

print(
    "Output:", jump(nums1),
    "\n Output:", jump(nums2))
