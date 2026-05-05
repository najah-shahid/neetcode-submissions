class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        largestLeft = height[i]
        largestRight = height[j]
        water = 0
        while (i<j):
            if (largestLeft < largestRight):
                i+=1
                if (height[i] > largestLeft):
                    largestLeft = height[i]
                water += (largestLeft - height[i])
            else:
                j-=1
                if (height[j] > largestRight):
                    largestRight = height[j]
                water += (largestRight - height[j])
        return water