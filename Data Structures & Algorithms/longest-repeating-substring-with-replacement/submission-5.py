class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        curSum = 0
        res = 0
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1
            curSum = max(curSum, mp[s[i]])
            while (i - l + 1) - curSum > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res