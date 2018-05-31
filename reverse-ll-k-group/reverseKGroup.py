# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=prevNode=ListNode(0)
        dummy.next=l=r=head

        group=0
        while True:
            count=0
            while r and count < k:
                r=r.next
                count+=1
            if count == k:   # There are enough nodes to travel
                pre,curr = r, l
                for _ in range(k):
                    curr.next,curr,pre=pre,curr.next,curr
                prevNode.next,prevNode,l=pre,l,r
            else:
                return dummy.next
