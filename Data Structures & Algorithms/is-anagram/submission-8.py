class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = [0] * 26
        ana1 = [0] * 26
        for i in range(len(s)):
            ana[ord(s[i])-ord('a')] += 1
            ana1[ord(t[i])-ord('a')] += 1
        
        return ana == ana1

        