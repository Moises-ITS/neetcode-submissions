class Solution:
    def trap(self, height: List[int]) -> int:
        #left
        #right
        #merge
        #min(left, right) - height
        if len(height) == 0:
            return 0

        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i - 1])
        
        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        
        res = 0
        for i in range(len(height)):
            res += (min(left[i], right[i]) - height[i])

        return res