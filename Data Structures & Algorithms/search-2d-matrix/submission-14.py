class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = l + (r - l)//2 #12 > target = 10
            ro, co = mid//cols, mid%cols
            if matrix[ro][co] > target:
                r = mid - 1
            elif matrix[ro][co] < target:
                l = mid + 1
            else:
                return True
        return False
            