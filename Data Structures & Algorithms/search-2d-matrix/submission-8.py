class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        l = 0
        r = ROWS * COLS - 1
        while l <= r:
            pivot = l + (r - l) // 2
            row, col = pivot // COLS, pivot % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = pivot + 1
            else:
                r = pivot - 1
        return False
