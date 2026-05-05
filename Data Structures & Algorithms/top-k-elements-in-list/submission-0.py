from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in freqs.items():
            bucket[count].append(num)
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if (len(result) == k):
                    return result
            
        return []