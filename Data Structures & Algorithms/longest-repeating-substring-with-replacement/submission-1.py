class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        longest = 0
        freqs = {}
        max_freq = 0
        while (end < len(s)):
            freqs[s[end]] = freqs.get(s[end], 0) + 1
            if freqs[s[end]] > max_freq:
                max_freq = freqs[s[end]]
            
            while start < len(s) and ((end - start + 1) - max_freq) > k:
                freqs[s[start]] = freqs[s[start]] - 1
                start += 1
            substr_len = end - start + 1
            if longest < substr_len:
                longest = substr_len
            end += 1
        return longest

        