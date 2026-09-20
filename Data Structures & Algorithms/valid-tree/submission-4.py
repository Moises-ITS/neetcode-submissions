class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        adj = [[] for c in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visit = set()
        q = deque()
        q.append((0, -1))
        visit.add(0)
    
        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visit:
                    return False
                visit.add(neighbor)
                q.append((neighbor, node))
        
        return len(visit) == n