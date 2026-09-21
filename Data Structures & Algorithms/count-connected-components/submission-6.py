class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        adj = [[] for c in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nxt in adj[cur]:
                    if not visit[nxt]:
                        visit[nxt] = True
                        q.append(nxt)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res
