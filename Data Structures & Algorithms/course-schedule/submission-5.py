class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        inLine = [0] * numCourses
        for pre, req in prerequisites:
            graph[pre].append(req)
            inLine[req] += 1
        
        q = deque([c for c in range(numCourses) if inLine[c] == 0])
        time = 0

        while q:
            course = q.popleft()
            time += 1
            for nextCourse in graph[course]:
                inLine[nextCourse] -= 1
                if inLine[nextCourse] == 0:
                    q.append(nextCourse)
        
        return time == numCourses