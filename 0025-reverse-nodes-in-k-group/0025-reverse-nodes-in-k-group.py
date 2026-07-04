# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy
        
        while True:

            kth = groupPrev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            current = groupPrev.next

            while current != groupNext:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        