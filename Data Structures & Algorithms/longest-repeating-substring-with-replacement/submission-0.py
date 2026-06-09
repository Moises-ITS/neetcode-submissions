class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        res = 0
        maxed = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxed = max(maxed, seen[s[r]])
            while (r - l + 1) - maxed > k:
                seen[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res