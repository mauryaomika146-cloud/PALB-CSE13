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

    return left


nums1 = [1,3,5,6]
target1 = 5

nums2 = [1,3,5,6]
target2 = 2

nums3 = [1,3,5,6]
target3 = 7

print(
    "Output:", searchInsert(nums1, target1),
    "\nOutput:", searchInsert(nums2, target2),
    "\nOutput:", searchInsert(nums3, target3)
)