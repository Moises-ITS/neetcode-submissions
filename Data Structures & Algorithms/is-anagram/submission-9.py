class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x = [0] * 26
        for i in range(len(s)):
            x[ord(s[i])-ord('a')] += 1
            x[ord(t[i])-ord('a')] -= 1
        for j in x:
            if j != 0:
                return False
        return True