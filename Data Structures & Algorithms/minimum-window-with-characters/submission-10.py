class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s): return ""
        count, window = {}, {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        need, have = len(count), 0
        res, res_len = (0, 0), float("inf")
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in count and count[c] == window[c]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = (l, r)
                out = s[l]
                window[out] -= 1
                if out in count and window[out] < count[out]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""