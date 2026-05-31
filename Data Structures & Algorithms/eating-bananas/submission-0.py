class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        result = upper
        while lower <= upper:
            k = (upper + lower)//2
            hrsTaken = 0
            for pile in piles:
                hrsTaken += (-(-pile // k))
            if hrsTaken > h:
                lower = k + 1
            else:
                result = k
                upper = k - 1

        return result
        
