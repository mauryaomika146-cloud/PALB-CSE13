class Solution:
    def largest(self, arr):
        maxi = arr[0]
        for num in arr:
            if num > maxi:
                maxi = num
        return maxi


arr = [1, 8, 7, 56, 90]

obj = Solution()
print(obj.largest(arr))
