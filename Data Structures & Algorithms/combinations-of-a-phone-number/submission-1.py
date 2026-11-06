class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, subset):
            if len(subset) == len(digits):
                res.append(subset)
                return
            for j in digitToChar[digits[i]]: #abc
                backtrack(i + 1, subset + j)
        if digits:
            backtrack(0, "")
        return res
