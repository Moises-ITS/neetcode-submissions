class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        st = [0] * 26
        ts = [0] * 26

        for i in range(len(s)):
            st[ord(s[i])-ord('a')] += 1
            ts[ord(t[i])-ord('a')] += 1
        
        return st == ts