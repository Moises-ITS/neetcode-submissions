class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for c in range(numCourses)]
        inDegree = [0] * numCourses
        for src, dst in prerequisites:
            adj[src].append(dst)
            inDegree[dst] += 1
        
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
        return [] if time != numCourses else res[::-1]