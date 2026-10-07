class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        st = [0] * 26
        for i in range(len(s)):
            st[ord(s[i])-ord('a')] += 1
            st[ord(t[i])-ord('a')] -= 1
        
        for j in st:
            if j != 0:
                return False
        return True