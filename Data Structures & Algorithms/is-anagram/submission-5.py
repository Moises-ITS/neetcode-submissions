class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        map_t = {}
        map_s = {}
        for i in range(len(s)):
            map_t[t[i]] = map_t.get(t[i], 0) + 1
            map_s[s[i]] = map_s.get(s[i], 0) + 1
        return map_t == map_s
        