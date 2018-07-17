class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None and n == 1:
            head = None
            return head
            
        left,right = head, head
        
        # Offset the right pointer first
        for _ in range(n):
            right = right.next
        
        if right is None: # remove first elem
            head = left.next
            left = None
            return head            
            
        while right.next:
            left = left.next
            right = right.next
            
        temp = left.next
        left.next = temp.next
        temp = None #Cleanup
        
        return head
