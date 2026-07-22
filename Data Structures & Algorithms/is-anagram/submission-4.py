class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMapS = {}
        hashMapT = {}
        for i in range(len(s)):
            hashMapS[s[i]] = hashMapS.get(s[i], 0) + 1
            hashMapT[t[i]] = hashMapT.get(t[i], 0) + 1
        return hashMapS == hashMapT
