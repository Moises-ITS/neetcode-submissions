class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxf = 0
        res = 0
        l = 0
        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            maxf = max(maxf, hashMap[s[r]])

            while (r - l + 1) - maxf > k:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res 