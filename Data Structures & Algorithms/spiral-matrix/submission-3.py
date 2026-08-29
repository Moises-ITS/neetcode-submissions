class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        right, left = len(matrix[0]), 0

        res = []

        while top < bottom and left < right:

            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for j in range(top, bottom): #0-2 top-bottom matrix[row][col]
                res.append(matrix[j][right - 1])
            right -= 1
            if not (bottom > top and right > left):
                break
            
            for k in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][k])
            bottom -= 1

            for p in range(bottom - 1, top - 1, -1):
                res.append(matrix[p][left])
            left += 1
        return res