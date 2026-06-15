class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        permutations = self.permute(nums[1:])
        result = []
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                permutation_copy = permutation.copy()
                permutation_copy.insert(i, nums[0])
                result.append(permutation_copy)
        return result