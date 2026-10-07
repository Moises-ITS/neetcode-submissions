class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0
        for o in operations:
            if o == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif o == "C":
                res -= stack.pop()
            elif o == "D":
                res += (2 * stack[-1])
                stack.append(stack[-1] * 2)
            else:
                res += int(o)
                stack.append(int(o))
        return res

