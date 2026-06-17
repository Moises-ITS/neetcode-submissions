# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = node = ListNode()
        #ordered[2,4,6,8]
        #reversed[8,6,4,2]
        #need[2,8,4,6]

        #Find midpoint
        #Reverse second half
        #interweave og with reversed
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #save and cut
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #reversed second half

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return second

        

