# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        current1 = l1
        current2 = l2

        carry = 0
        current = ListNode(0)
        dummy = current

        while current1 or current2 or carry:
            val1 = current1.val if current1 else 0
            val2 = current2.val if current2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if current1 :
                current1 = current1.next
            
            if current2:
                current2 = current2.next
        return dummy.next
        


