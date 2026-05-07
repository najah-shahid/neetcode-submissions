class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_freqs = {}
        start = 0
        end = 0
        longest = 0
        while (end < len(s)):
            char_freqs[s[end]] = char_freqs.get(s[end], 0) + 1
            while start < len(s) and char_freqs[s[end]] > 1:
                char_freqs[s[start]] -= 1
                start += 1
            if (end - start + 1 > longest):
                longest = end - start + 1
            end += 1
        return longest
