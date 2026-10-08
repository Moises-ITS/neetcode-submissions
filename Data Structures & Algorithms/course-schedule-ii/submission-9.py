class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            inDegree[v] += 1
        
        q = deque([c for c in range(numCourses) if inDegree[c] == 0])

        time, res = 0, []
        while q:
            node = q.popleft()
            time += 1
            res.append(node)
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return res[::-1] if time == numCourses else []