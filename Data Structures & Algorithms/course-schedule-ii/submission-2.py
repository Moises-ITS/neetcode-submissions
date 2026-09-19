class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        inLine = [0] * numCourses
        time, res = 0, []
        for pre, req in prerequisites:
            adj[pre].append(req)
            inLine[req] += 1
        
        q = deque([c for c in range(numCourses) if inLine[c] == 0])

        while q:
            course = q.popleft()
            time += 1
            res.append(course)
            for nextCourse in adj[course]:
                inLine[nextCourse] -= 1
                if inLine[nextCourse] == 0:
                    q.append(nextCourse)

        return [] if time != numCourses else res[::-1]