# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lengthA = getLength(headA)
        lengthB = getLength(headB)

        pA = headA
        pB = headB

        if lengthA > lengthB:
            for _ in range(lengthA - lengthB):
                pA = pA.next
        else:
            for _ in range(lengthB - lengthA):
                pB = pB.next

        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next

        return None

                           
