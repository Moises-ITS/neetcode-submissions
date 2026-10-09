class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        q.append((0, -1))
        visit = set()
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if parent == nei:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
        return len(visit) == n