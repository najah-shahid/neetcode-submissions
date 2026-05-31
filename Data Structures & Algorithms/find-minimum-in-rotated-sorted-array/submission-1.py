class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        res = nums[0]
        while left<=right:
            if nums[left] < nums[right]:
                return min(res, nums[left])
            mid = (left + right)//2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res
                