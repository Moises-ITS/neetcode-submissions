from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        for pre, req in prerequisites:
            graph[pre].append(req)
            inDegree[req] += 1
        
        q = deque([c for c in range(numCourses) if inDegree[c] == 0])

        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        return taken == numCourses
        