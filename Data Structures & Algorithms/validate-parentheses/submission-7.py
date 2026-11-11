class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        stack = []
        for r in s:
            if r in paren:
                if stack and paren[r] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(r)
        return True if not stack else False