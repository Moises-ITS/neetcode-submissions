class Solution:
    def climbStairs(self, n: int) -> int:
        past, curr = 1, 1

        for i in range(2, n + 1):
            past, curr = curr, curr + past

        return curr 

