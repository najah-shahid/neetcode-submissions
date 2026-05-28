from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = 0
        s1_freqs = Counter(s1)
        s2_freqs = {}
        while end < len(s2):
            s2_freqs[s2[end]] = s2_freqs.get(s2[end], 0) + 1
            while start < len(s2) and s2_freqs[s2[end]] > s1_freqs[s2[end]]:
                s2_freqs[s2[start]] -= 1
                start += 1
            if (end - start + 1) == len(s1):
                return True
            end += 1
        return False
            