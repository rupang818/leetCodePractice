# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # while next != NULL, create a node w/ the value and set its next to current head, then move the head
        reversedLL=None
        while head is not None:
            print(head.val)
            newHead=ListNode(head.val)
            newHead.next=reversedLL
            reversedLL=newHead
            head=head.next
        return reversedLL

# Second Solution
# Space: O(1), Time: O(n)
def reverseList(self, head):
    tail=prevNode=ListNode(None)
    while head is not None:
        tmp=head
        head=head.next
        tmp.next=prevNode
        prevNode=tmp
    return (tmp, tail)
