class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        for pre, req in prerequisites:
            adj[pre].append(req)
            inDegree[req] += 1
        
        q = deque([c for c in range(numCourses) if inDegree[c] == 0])

        time = 0
        while q:
            node = q.popleft()
            time += 1
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return time == numCourses