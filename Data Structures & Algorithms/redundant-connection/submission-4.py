class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        inDegree = [0] * (n + 1)
        adj = [[] for i in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            inDegree[u] += 1
            inDegree[v] += 1
        
        q = deque([c for c in range(1, n + 1) if inDegree[c] == 1])

        while q:
            node = q.popleft()
            inDegree[node] -= 1
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 1:
                    q.append(nei)
        
        for u, v in edges[::-1]:
            if inDegree[v] and inDegree[u] == 2:
                return [u, v]
        return []