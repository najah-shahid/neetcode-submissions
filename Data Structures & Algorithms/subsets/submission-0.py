class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def makeSubset(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            makeSubset(idx + 1)
            subset.pop()
            makeSubset(idx + 1)
        makeSubset(0)
        return result