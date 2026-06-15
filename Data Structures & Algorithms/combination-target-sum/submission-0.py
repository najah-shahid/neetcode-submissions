class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        def findCombinations(i, curr_sum):
            if curr_sum == target:
                result.append(combination.copy())
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            combination.append(nums[i])
            findCombinations(i, curr_sum + nums[i])
            combination.pop()
            findCombinations(i+1, curr_sum)
        findCombinations(0, 0)
        return result

