# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Find middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #Save and cut
        second = slow.next
        prev = slow.next = None

        #Reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        first = head #
        second = prev #
        while second: #
            temp1 = first.next #
            temp2 = second.next # 
            first.next = second #
            second.next = temp1 #
            first = temp1 #
            second = temp2 #
        return second

        

