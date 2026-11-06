class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(c, l, r):
            while l < r:
                if c[l] != c[r]:
                    return False
                l += 1
                r -= 1
            return True
        res = []
        def dfs(i, subset):
            if i >= len(s):
                res.append(subset.copy())
                return
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    subset.append(s[i:j+1])
                    dfs(j + 1, subset)
                    subset.pop()
        dfs(0, [])
        return res