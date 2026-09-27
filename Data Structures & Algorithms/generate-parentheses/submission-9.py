class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        current = []
        def dfs(opened, closed):
            if opened > n or closed > n:
                return
            if opened == n and closed == n:
                answer.append("".join(current))
            if opened < n:
                current.append("(")
                dfs(opened + 1, closed)
                current.pop()
            if closed < opened:
                current.append(")")
                dfs(opened, closed + 1)
                current.pop()
            return
        dfs(0, 0)
        return answer
