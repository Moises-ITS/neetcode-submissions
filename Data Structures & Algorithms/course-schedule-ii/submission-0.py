from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #map key and value pairs to reqs
        #dfs same?
        #final step will be to loop through numCourses and print any extras else []

        #num of courses at least 1
        #prereq pairs are unique

        preReq = defaultdict(list)
        
        for a, b in prerequisites:
            preReq[a].append(b)

        output = []
        visit, cycle = set(), set()
        def dfs(courseNum):
            if courseNum in cycle:
                return False
            if courseNum in visit:
                return True
            cycle.add(courseNum)
            for pre in preReq[courseNum]:
                if not dfs(pre):
                    return False
            cycle.remove(courseNum)
            visit.add(courseNum)
            output.append(courseNum)
            return True

        for courseNum in range(numCourses):
            if not dfs(courseNum):
                return []
        return output

