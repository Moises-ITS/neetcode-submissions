# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur3 = ListNode()
        # find the head
        cur1 = list1
        cur2 = list2
        
        while cur1 and cur2:
            
            val1 = cur1.val
            val2 = cur2.val
            if val1 <= val2:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next
                
            cur3 = cur3.next
        
        cur3.next = cur1 or cur2 
        
        return dummy.next