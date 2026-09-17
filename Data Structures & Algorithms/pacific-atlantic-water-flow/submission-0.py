class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #water moves in 4 cardinal directions except if it's water where it can flow
        #adjacent to the ocean
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def bfs(source, visited):
            q = deque(source)

            while q:
                r, c = q.popleft()
                visited[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                    not visited[nr][nc] and heights[nr][nc]
                    >= heights[r][c]
                    ):
                        q.append((nr, nc))
        
        pac = []
        atl = []

        for c in range(cols):
            pac.append((0, c))
            atl.append((rows - 1, c))
        
        for r in range(rows):
            pac.append((r, 0))
            atl.append((r, cols - 1))
        
        bfs(pac, pacific)
        bfs(atl, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res

