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
        #mm method

        mp = {None: None}
        cur = curr = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next
        
        while curr:
            copy = mp[curr]
            copy.next = mp[curr.next]
            copy.random = mp[curr.random]

            curr = curr.next
        return mp[head]