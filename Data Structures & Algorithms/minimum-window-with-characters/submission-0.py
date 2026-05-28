from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freqs = Counter(t)
        start = 0
        end = 0
        chars_in_t = 0
        shortest = len(s) + 1
        shortest_start = 0
        shortest_end = -1
        s_freqs = {}
        while end < len(s):
            s_freqs[s[end]] = s_freqs.get(s[end], 0) + 1
            if s_freqs[s[end]] <= t_freqs.get(s[end], 0):
                chars_in_t += 1
            while (start <= end) and (s_freqs[s[start]] > t_freqs.get(s[start], 0)):
                s_freqs[s[start]] -= 1
                start +=1
            if chars_in_t == len(t) and (end - start + 1) < shortest:
                shortest = end - start + 1
                shortest_start = start
                shortest_end = end
            end += 1
        return s[shortest_start: shortest_end + 1]
