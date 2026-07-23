class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                c = board[row][col]
                if c == ".":
                    continue
                
                box = (row//3) * 3 + (col//3)

                if c in rows[row] or c in cols[col] or c in boxes[box]:
                    return False
                cols[col].add(c)
                rows[row].add(c)
                boxes[box].add(c)
        return True