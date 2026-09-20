class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        inDegree = [0] * n
        adj = [[] for c in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            inDegree[u] += 1
            inDegree[v] += 1
        
        visit = set()
        visit.add(0)
        q = deque()
        q.append((0, -1))

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
        
        return len(visit) == n