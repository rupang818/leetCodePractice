class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        returnHead=head.next
        prev=None
        while head is not None:
            if not head.next:
                break
            tmp=head.next
            if prev:
                prev.next =tmp
            head.next=tmp.next
            tmp.next=head
            prev=head
            head=head.next
        
        return returnHead
