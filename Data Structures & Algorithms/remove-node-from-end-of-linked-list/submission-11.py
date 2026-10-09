# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #beginning after the end method

        dummy = ListNode(0, head)
        cur, node = head, dummy

        while n != 0:
            cur = cur.next
            n -= 1
        
        while cur:
            node = node.next
            cur = cur.next
        
        node.next = node.next.next
        return dummy.next