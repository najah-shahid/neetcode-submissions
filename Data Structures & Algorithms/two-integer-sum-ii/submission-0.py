class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        needed_nums = {}
        for i in range(len(numbers)):
            needed = target - numbers[i]
            if needed_nums.get(needed) != None:
                return [needed_nums[needed]+1, i+1]
            else:
                needed_nums[numbers[i]] = i
        return [-1,-1] 