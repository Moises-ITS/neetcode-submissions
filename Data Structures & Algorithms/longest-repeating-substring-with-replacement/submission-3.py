class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        curSum = l = res = 0
        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            curSum = max(curSum, m[s[r]])

            while (r - l + 1) - curSum > k:
                m[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            