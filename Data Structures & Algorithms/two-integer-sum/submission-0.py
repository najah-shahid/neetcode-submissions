class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i in range(len(nums)):
            num_needed = target - nums[i]
            if nums_hash.get(num_needed) is not None:
                idx = nums_hash[num_needed]
                return [idx, i]
            else:
                nums_hash[nums[i]] = i
        
        return []
        