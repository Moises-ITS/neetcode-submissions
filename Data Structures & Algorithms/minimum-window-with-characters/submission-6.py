class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        countT = {}
        window = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        have, need = 0, len(countT)
        res, resLen = (-1, -1), float('inf')
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = (l, r)
                out = s[l]
                window[out] -= 1
                if out in countT and window[out] < countT[out]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
