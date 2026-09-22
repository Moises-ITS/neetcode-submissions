class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        time, res = 0, []
        for pre, req in prerequisites:
            adj[pre].append(req)
            inDegree[req] += 1

        q = deque([c for c in range(numCourses) if inDegree[c] == 0])

        while q:

            time += 1
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return [] if time != numCourses else res[::-1]
         