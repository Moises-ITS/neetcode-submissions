class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for c in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                curr = q.popleft()
                visit[curr] = True
                for nei in adj[curr]:
                    if not visit[nei]:
                        q.append(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res