class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        stack = []
        while l < r:
            #i=0 r = 7
            height = min(heights[l], heights[r])
            width = r-l
            stack.append(width*height)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1           
        return max(stack)
            
            
