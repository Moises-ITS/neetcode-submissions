class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find halfway point
        #reverse second half of list
        #merge together beginning with first half of list 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return
        #slow is midpoint
        second = slow.next
        #4->5->6->None
        #second CUTS slow into two sections, second half anf prev
        slow.next = None #prev points to none in slow.next
        prev = None
        #0->1->2->3->None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first = head
        second = prev
        while second:
            #1->2->3->None
            #6->5->4->None
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2



        