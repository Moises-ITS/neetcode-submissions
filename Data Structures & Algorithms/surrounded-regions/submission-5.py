class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == "O":
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            if board[r][c] == "O":
                board[r][c] = "T"
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols):
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"