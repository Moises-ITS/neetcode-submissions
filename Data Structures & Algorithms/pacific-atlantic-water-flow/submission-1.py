class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        atl = [[False] * cols for i in range(rows)]
        pac = [[False] * cols for i in range(rows)]

        def bfs(source, visited):
            q = deque(source)
            while q:
                r, c = q.popleft()
                visited[r][c] = True
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))
        
        pacific = []
        atlantic = []
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))
        
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
