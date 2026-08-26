from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == "#"):
                return False
            
            board[r][c] = '#'

            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            board[r][c] = word[i]
            return res

                #enter recursive pipeline
                #i += 1

        for row in range(rows):
            for col in range(cols):
                c = board[row][col]
                if dfs(row, col, 0):
                    return True
        return False
