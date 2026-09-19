class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        inLine = [0] * numCourses
        time = 0
        for pre, req in prerequisites:
            adj[pre].append(req)
            inLine[req] += 1
        
        q = deque([c for c in range(numCourses) if inLine[c] == 0])


        while q:
            time += 1
            course = q.popleft()
            for nextCourse in adj[course]:
                inLine[nextCourse] -= 1
                if inLine[nextCourse] == 0:
                    q.append(nextCourse)
        
        return time == numCourses