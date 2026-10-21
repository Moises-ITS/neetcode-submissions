class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        minHeight, maxHeight = height[l], height[r]
        res = 0
        while l < r:
            if minHeight < maxHeight:
                l += 1
                minHeight = max(minHeight, height[l])
                res += minHeight - height[l]
            else:
                r -= 1
                maxHeight = max(maxHeight, height[r])
                res += maxHeight - height[r]
        return res