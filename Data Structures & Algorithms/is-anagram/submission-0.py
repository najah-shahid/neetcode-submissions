class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are different, return false
        if len(s) != len(t):
            return False
        
        s_freqs = {}
        t_freqs = {}
        for ch in s:
            s_freqs[ch] = s_freqs.get(ch, 0) + 1
        
        for ch in t:
            t_freqs[ch] = t_freqs.get(ch, 0) + 1
        
        for ch in t:
            if t_freqs[ch] != s_freqs.get(ch, 0):
                return False
        return True
        