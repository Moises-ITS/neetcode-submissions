class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        curSum = 0
        l = 0
        res = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            curSum = max(curSum, mp[s[r]])

            while (r - l + 1) - curSum > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res