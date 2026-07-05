# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA = 0
        lengthB = 0
        currentA = headA
        currentB = headB
        pA = headA
        pB = headB

        while currentA:
            lengthA += 1
            currentA = currentA.next
        while currentB:
            lengthB += 1
            currentB = currentB.next

        if lengthA > lengthB:
            diff = lengthA - lengthB
            while diff:
                pA = pA.next
                diff -= 1
            while pA or pB:
                if pA == pB:
                    return pA
                pA = pA.next
                pB = pB.next

        if lengthB > lengthA:
            diff = lengthB - lengthA
            while diff:
                pB = pB.next
                diff -= 1
            while pA or pB:
                if pA == pB:
                    return pB
                pA = pA.next
                pB = pB.next
        
        while pA or pB:
            if pA == pB:
                return pB
            pA = pA.next
            pB = pB.next

                           
