class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            per = 0
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        per += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return per
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
        return 0
