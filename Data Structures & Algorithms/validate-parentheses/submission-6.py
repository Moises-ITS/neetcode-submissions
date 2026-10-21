class Solution:
    def isValid(self, s: str) -> bool:
        pali = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for r in s:
            if r in pali:
                if stack and stack[-1] == pali[r]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(r)
        return True if not stack else False