class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        for pre, req in prerequisites:
            adj[pre].append(req)
            inDegree[req] += 1
        
        q = deque([c for c in range(numCourses) if inDegree[c] == 0])

        time, res = 0, []

        while q:
            course = q.popleft()
            res.append(course)
            time += 1
            for nextCourse in adj[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        return [] if time != numCourses else res[::-1]

