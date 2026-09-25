"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = cur = head
        m = {None:None}
        while cur:
            copy = Node(cur.val)
            m[cur] = copy
            cur = cur.next
        
        while curr:
            copy = m[curr]
            copy.next = m[curr.next]
            copy.random = m[curr.random]
            curr = curr.next
        return m[head]