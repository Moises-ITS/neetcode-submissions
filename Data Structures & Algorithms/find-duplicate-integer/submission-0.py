class Node:
    def Node(self, next, val):
        self.next = None
        self.val = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Input: Array of Numbers from range 1->n
        #Ouput: repeated number
        #Constraints: Solve with O(1) space complexity(Pointers), solve using linkedList
        #Matching Solution: Floyd's Cycle

        #n different possible values
        #len = n + 1

        #Each value will point at some position in the array at least once and at most n

        #index points to value
        #Ex. [1,3,4,2,2] -> 1 -> 3 -> 2 -> 4 -> 2 ( Cycle )
        #Multiple Nodes point to Node 2

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            

        

