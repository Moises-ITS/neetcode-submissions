class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #2 child nodes and 1 parent per node, there are NO connections between children
        #check children, parent and if a child id a parent then we switch parent to be root parent and
        #smaller child until we detect a cycle which is when a root child is smaller than another root
        #child

        if len(edges) != n - 1:
            return False
        parent = [c for c in range(n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        for x, y in edges:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
        return True