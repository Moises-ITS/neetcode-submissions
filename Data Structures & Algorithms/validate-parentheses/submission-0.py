class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if i in paren:
                if stack and paren[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False