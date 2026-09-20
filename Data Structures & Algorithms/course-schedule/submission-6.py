class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adj = [[] for c in range(numCourses)]
        for pre, req in prerequisites:
            adj[pre].append(req)
            inDegree[req] += 1
        
        q = deque([c for c in range(numCourses) if inDegree[c] == 0])

        time = 0
        while q:
            course = q.popleft()
            time += 1
            for nextCourse in adj[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        return time == numCourses