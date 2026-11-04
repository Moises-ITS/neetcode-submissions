class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        minF = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            minF = max(minF, count[s[i]])
            while (i - l + 1) - minF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res