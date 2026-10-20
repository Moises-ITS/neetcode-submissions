class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stack = [0] * 26

        for i in range(len(s)):
            stack[ord(s[i])-ord('a')] += 1
            stack[ord(t[i])-ord('a')] -= 1
        
        for let in stack:
            if let != 0:
                return False
        return True