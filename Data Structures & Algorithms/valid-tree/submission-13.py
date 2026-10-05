class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)] 
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visit = set()
        q = deque([(0, -1)])
        visit.add(0)

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

        
