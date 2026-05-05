from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch)-ord('a')] += 1
            key = tuple(counts)
            anagrams[key].append(word)
        return list(anagrams.values())

