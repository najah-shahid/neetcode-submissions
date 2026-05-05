class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while (j<k):
                sumOfNums = nums[i] + nums[j] + nums[k]
                if (sumOfNums == 0):
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while (j<len(nums) and nums[j] == nums[j-1]):
                        j+=1
                    k-=1
                    while (k>=i+1 and nums[k] == nums[k+1]):
                        k-=1
                elif (sumOfNums > 0):
                    k-=1
                    while (k>=i+1 and nums[k] == nums[k+1]):
                        k-=1
                else:
                    j+=1
                    while (j<len(nums) and nums[j] == nums[j-1]):
                        j+=1
            i+=1
            while (i<len(nums) and nums[i] == nums[i-1]):
                i+=1
        return result