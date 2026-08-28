from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each beginning number with its prerequisites
        #recursively dfs through the map
        preMap = defaultdict(list)
        for req in prerequisites:
            for i in range(len(req) - 2, -1, -1):
                preMap[req[-1]].append(req[i])
        
        visiting = set() #in dfs keep track on curr path
        
        def dfs(c):
            if c in visiting:
                return False #cycle detection
            if preMap[c] == []:
                return True

            visiting.add(c)
            for val in preMap[c]:
                if not dfs(val):
                    return False
                
            visiting.remove(c)
            preMap[c] = []
            return True     

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        