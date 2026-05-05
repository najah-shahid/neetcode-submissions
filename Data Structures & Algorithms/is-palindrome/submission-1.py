class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while (i<j):
            while (i<len(s) and s[i].isalnum() == False):
                i+=1
            while (j>=0 and s[j].isalnum() == False):
                j-=1
            if (i>=j):
                break
            lowercase_i = s[i].lower()
            lowercase_j = s[j].lower()
            if (lowercase_i != lowercase_j):
                return False
            i+=1
            j-=1
        
        return True
