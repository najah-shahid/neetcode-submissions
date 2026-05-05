class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_freqs = {}
        for num in nums:
            if nums_freqs.get(num):
                return True
            else:
                nums_freqs[num] = nums_freqs.get(num, 0) + 1
        return False
        